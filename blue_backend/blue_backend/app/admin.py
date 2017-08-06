# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . models import User, Payload
from . forms import UserCreationForm

class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    list_display = ("email",)
    ordering = ("email",)
    list_filter = ("is_active", "is_superuser",)

    fieldsets = (
        (None, {'fields': ('is_superuser', 'is_active', 'email', 'password', 'first_name', 'last_name',)}),)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password', 'first_name', 'last_name', 'is_superuser', 'is_active')}
            ),
        )

    filter_horizontal = ()


@admin.register(Payload)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('id', 'created', 'data', 'neutral',)
    list_filter = ('neutral',)

admin.site.register(User, CustomUserAdmin)
