# -*- coding: utf-8 -*-
import requests
from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView
from rest_framework import parsers, renderers, generics, status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer, UserProfileSerializer, PayloadSerializer
from blue_backend.app.models import Payload

class APILoginView(APIView):
    """
    A view that allows users to login providing their email and password.
    """

    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})

class APIUserProfileView(generics.RetrieveUpdateAPIView):
    """
    An endpoint for users to view and update their profile information.
    """

    serializer_class = UserProfileSerializer

    def get_object(self):
        return self.request.user


class APIPayloadView(generics.RetrieveUpdateAPIView):
    """
    An endpoint for users to view and update their payload information.
    """

    serializer_class = PayloadSerializer
        

    def get_object(self):
        pass