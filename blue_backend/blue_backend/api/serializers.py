# -*- coding: utf-8 -*-
from rest_framework import serializers
from blue_backend.app.models import User, Payload

class UserRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'password',)
        extra_kwargs = {'password': {'write_only': True}}

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'is_active', 'first_name', 'last_name', 'date_joined',)
        read_only_fields = ('is_active',)

class ResetPasswordSerializer(serializers.ModelSerializer):

    id = serializers.CharField()
    token = serializers.CharField()

    class Meta:
        model = User
        fields = ('id', 'token', 'password',)
        extra_kwargs = {'password': {'write_only': True}}


class PayloadSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Payload
        fields = ('data', 'neutral',)