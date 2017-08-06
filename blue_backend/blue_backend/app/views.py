# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db.models import Sum
from django.shortcuts import render, resolve_url
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.formats import number_format

class DashboardView(TemplateView):
    template_name = 'dashboard.html'