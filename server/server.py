from pprint import pprint
from twisted.web import server, resource
from twisted.internet import reactor, task
from twisted.python.log import err
from twisted.web.client import Agent
from twisted.web.http_headers import Headers
from watson_developer_cloud import NaturalLanguageClassifierV1
import config
import json
import sys
import os
import urllib
import requests

if 'PORT' in os.environ:
    PORT = int(os.environ['PORT'])
else:
    PORT = 8880

def notify_parent():
    sys.stderr.write("Sending notification to parent\n")
    # Send text message

    r = requests.post(
        "https://graph.facebook.com/v2.6/me/messages?access_token={}".format(
            config.MESSENGER_PAGE_TOKEN),
        data=json.dumps({
            "recipient": {
                "name": config.TEST_USER_NAME,
                "phone_number": config.TEST_USER_PHONE
            },
            "message": {
                "text":
                "Attention! Someone is talking about suspicious themes with your child."
            }
        }),
        headers={"Content-Type": "application/json"})
    sys.stderr.write(
        "Resulting code for message to parent: {}\n".format(r.status_code))



def notify_dashboard(msg, klass):
    # Send info to dashboard
    r = requests.put(
        config.DASHBOARD_API_URL,
        data=json.dumps({
            "data": msg,
            "neutral": True if klass == "Neutro" else False
        }),
        headers={
            "Content-type": "application/json",
            "Authorization": config.DASHBOARD_AUTHORIZATION_TOKEN
        })
    sys.stderr.write("Resulting code for message to dashboard: {}\n".format(r.status_code))


def classify_msg(msg):
    natural_language_classifier = NaturalLanguageClassifierV1(
        username=config.WATSON_USERNAME, password=config.WATSON_PASSWORD)

    classifiers = natural_language_classifier.list()


    classifier_id = classifiers["classifiers"][-1]["classifier_id"]
    #print(json.dumps(classifiers, indent=2))

    status = natural_language_classifier.status(classifier_id)
    #print(json.dumps(status, indent=2))
    sys.stderr.write(
        "Request to server received status '{}'\n".format(status["status"]))

    if status['status'] == 'Available':
        classes = natural_language_classifier.classify(
            classifier_id, msg)

        top_class = classes['classes'][0]

        sys.stderr.write("For text '''{}''' class was '{}' ({})\n".format(
            msg, classes['top_class'], top_class['confidence']))

        notify_dashboard(msg, top_class['class_name'])

        if top_class['class_name'] == "Ruim" and top_class['confidence'] >= .95:
            notify_parent()  #warn parent


class FormPage(resource.Resource):
    isLeaf=True

    def render_POST(self, request):

        request.setHeader('Access-Control-Allow-Origin', '*')
        request.setHeader('Access-Control-Allow-Headers',
                          'x-prototype-version,x-requested-with')

        try:
            data = json.loads(request.content.getvalue())
            sys.stderr.write(
                "Received POST request from {}\n".format(request.getHost()))
            t = task.deferLater(reactor, 1.0, classify_msg, data["text"])
        except Exception as e:
            sys.stderr.write("ERROR TRYING TO DECODE DATA '{}'\n".format(e))
        return ''

    def render_GET(self, request):
        # for messenger webhook
        if request.path == '/webhook':
            # for messenger bot
            args = request.args
            received_token = args['hub.verify_token'][0]
            if args['hub.mode'][0] == 'subscribe' and \
                    received_token == config.MESSENGER_TOKEN:
                sys.stderr.write("Validating webhook\n")

                return args['hub.challenge'][0]
            else:
                sys.stderr.write("Messenger Webhook: Invalid token = '{}'\n".
                                 format(received_token))


        return ''


if __name__ == "__main__":
    sys.stderr.write("Starting server...\n")
    site = server.Site(FormPage())
    reactor.listenTCP(PORT, site)
    reactor.run()
