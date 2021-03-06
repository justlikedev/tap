#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers

from core.models import User, Token, Event, Seat, Reserv


class UserSerializer(serializers.HyperlinkedModelSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()
    is_admin = serializers.BooleanField()
    is_active = serializers.BooleanField()
    last_login = serializers.DateTimeField(format='%d/%m/%Y %H:%M')

    class Meta:
        model = User
        fields = ('url', 'first_name', 'last_name', 'email', 'phone', 'is_admin', 'is_active', 'last_login')


class TokenSerializer(serializers.HyperlinkedModelSerializer):
    hashcode = serializers.CharField()
    validity = serializers.DateField(format='%d/%m/%Y')
    validate_in = serializers.DateField(format='%d/%m/%Y')
    validate_by = serializers.HyperlinkedRelatedField(required=False, allow_null=True,
        queryset=User.objects.all(), view_name='user-detail')
    
    class Meta:
        model = Token
        fields = ('url', 'hashcode', 'validity', 'validate_in', 'validate_by')


class EventSerializer(serializers.HyperlinkedModelSerializer):
    title = serializers.CharField()
    date = serializers.DateTimeField(format='%d/%m/%Y %H:%M')
    max_seatings = serializers.IntegerField()
    max_tickets = serializers.IntegerField()
    
    class Meta:
        model = Event
        fields = ('url', 'title', 'date', 'max_seatings', 'max_tickets')

class SeatSerializer(serializers.HyperlinkedModelSerializer):
    row = serializers.CharField()
    column = serializers.IntegerField()
    type = serializers.ChoiceField(choices=((0, 'Balcão'), (1, 'Palco')))
    slug = serializers.CharField()
    is_reserved = serializers.BooleanField()

    class Meta:
        model = Seat
        fields = ('url', 'row', 'column', 'type', 'slug', 'is_reserved')


class ReservSerializer(serializers.HyperlinkedModelSerializer):
    alumn = serializers.HyperlinkedRelatedField(required=False, allow_null=True, queryset=User.objects.all(), view_name='user-detail')
    event = serializers.HyperlinkedRelatedField(required=False, allow_null=True, queryset=Event.objects.all(), view_name='event-detail')
    seats = serializers.HyperlinkedRelatedField(many=True, queryset=Seat.objects.all(), view_name='seat-detail')
    
    class Meta:
        model = Reserv
        fields = ('url', 'alumn', 'event', 'seats')