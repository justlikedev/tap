#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.views.static import serve as static_serve
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.models import Group

urlpatterns = [
    url(r'^rest/', include('rest.urls')),
]
