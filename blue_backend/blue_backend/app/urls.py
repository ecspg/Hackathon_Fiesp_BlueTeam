# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from blue_backend.app import views as c

urlpatterns = [
    url(r'^dashboard/', c.DashboardView.as_view()),
]