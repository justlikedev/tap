#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from rest_framework import routers
from rest_framework.authtoken import views as rf_views

from rest import views

router = routers.DefaultRouter()

# Register TAP's viewsets
router.register(r'users', views.UserViewSet, base_name='user')
router.register(r'tokens', views.TokenViewSet, base_name='token')
router.register(r'events', views.EventViewSet, base_name='event')
router.register(r'seats', views.SeatViewSet, base_name='seat')
router.register(r'reservations', views.ReservViewSet, base_name='reserv')

# Wire up our API using automatic URL routing
# Additionally the URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
