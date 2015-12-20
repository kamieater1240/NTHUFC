#-*- encoding=UTF-8 -*-
from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    #current_student = models.BooleanField(default=True)

    def __unicode__(self):
        return self.user.username


class Account(models.Model):
    username = models.CharField(max_length=20, default='', unique=True)
    nickname = models.CharField(max_length=20, default='', unique=True)

    TEACHER = 'TE'
    STUDENT = 'ST'
    OFFICER = 'OF'
    ALUMNUS = 'AL'
    IDENTITY_CHOICES = (
        (ALUMNUS, '校友'),
        (OFFICER, '職員'),
        (STUDENT, '學生'),
        (TEACHER, '教師')
    )

    identity = models.CharField(max_length=2, choices=IDENTITY_CHOICES, default=None)
    major = models.CharField(max_length=20, default='', blank=True, null=True)
    email = models.EmailField(max_length=250, unique=True)
    cellphone = models.CharField(max_length=10, unique=True, validators=[RegexValidator(regex='^\d{10}$', message='Invalid number', code='Invalid number')])
    def __unicode__(self):
        return self.username

    '''custom authentication resolve 'is_authenticated' problem'''
    def is_authenticated(self):
        return True
