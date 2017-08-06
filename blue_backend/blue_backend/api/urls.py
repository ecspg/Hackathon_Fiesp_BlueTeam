# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from . import views

urlpatterns = [
     url(r'^v1/accounts/login/$', views.APILoginView.as_view(), name="api_login"),
     url(r'^v1/accounts/user/profile/$', views.APIUserProfileView.as_view(), name="api_profile"),
     url(r'^v1/payloads/$', views.APIPayloadView.as_view(), name="api_payload"),
     url(r'^', include('rest_framework_docs.urls'))
]