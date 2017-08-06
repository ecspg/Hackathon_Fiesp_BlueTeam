# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser

from . managers import UserManager


# Create your models here.
class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name=_('created on'))
    modified = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name=_('modified in'))

    class Meta:
        abstract = True


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    data = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('data'))

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)
    
    @property
    def is_staff(self):
        return self.is_superuser


class Payload(TimeStampedModel):
    user = models.ForeignKey('User', default='1', verbose_name=_('user'))
    data = models.CharField(max_length=255, verbose_name=_('data'))  
    neutral = models.BooleanField(_('neutral'), default=True)

    class Meta:
        ordering = ['-id']
        verbose_name = _('Payload')
        verbose_name_plural = _('Payloads')
    
    def __unicode__(self):
        return unicode(self.id)

