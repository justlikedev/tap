#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import string
from datetime import datetime

from dateutil.relativedelta import relativedelta

from core.models import Event, Reserv, Seat, Token, User


def create_tokens(quantity=100):
    for token in range(0, quantity):
        hashcode = random.getrandbits(32)
        validity = (datetime.now() + relativedelta(days=15)).date()
        Token.objects.create(hashcode=hashcode, validity=validity)
        print u'{0} token created: {1} validity until {2}'.format(token, hashcode, validity)


def create_seats():
    # create seats for stage
    print u'seats for stage'
    for row in string.ascii_letters.upper()[0:20]:
        if row == 'A':
            columns = range(1, 27)
        elif row in ('S', 'T'):
            columns = range(5, 29)
        else:
            columns = range(1, 29)
        for column in columns:
            print u'seat {0}{1}'.format(row, column)
            Seat.objects.create(type=1, row=row, column=column)

    # create seats for balcon
    print u'seats for balcon'
    for row in string.ascii_letters.upper()[0:14]:
        columns = range(1, 30)
        if row in ('A', 'B', 'C', 'D', 'E', 'F'):
            columns = range(9, 30)
        elif row in ('G', 'H', 'I', 'J'):
            columns = range(1, 30)
        elif row == 'K':
            columns.remove(28)
        elif row == 'L':
            columns.remove(28)
            columns.remove(26)
            columns.remove(24)
        elif row in ('M', 'N'):
            columns.remove(28)
            columns.remove(26)
            columns.remove(24)
            columns.remove(22)
        for column in columns:
            print u'seat {0}{1}'.format(row, column)
            Seat.objects.create(type=0, row=row, column=column)

def populate():
    # clearing database
    User.objects.all().delete()
    Token.objects.all().delete()
    Event.objects.all().delete()
    Seat.objects.all().delete()
    Reserv.objects.all().delete()

    # create tokens
    print u'creating some tokens'
    create_tokens()
    
    # create seats
    print u'creating some seats'
    create_seats()

    # create a superuser
    print u'creating a superuser admin@tap.com / tapacademy'
    User.objects.create_superuser(email='admin@tap.com', password='tapacademy', first_name='Admin')

    # create alumns
    print u'creating some alumns with passwords <name>123'
    luigi = User.objects.create_user(first_name='Luigi', password='luigi123', email='luigi@tap.com')
    mario = User.objects.create_user(first_name='Mario', password='mario123', email='mario@tap.com')
    User.objects.create_user(first_name='Peach', password='peach123', email='peach@tap.com')
    User.objects.create_user(first_name='Yoshi', password='yoshi123', email='yoshi@tap.com')

    # create events
    print u'creating some events'
    event_1 = Event.objects.create(title='A princesa Peach no reino encantado do sapateado.', 
    date=datetime(2018, 12, 10, 20), max_seatings=100, max_tickets=3)

    print u'%s created' % event_1.title

    event_2 = Event.objects.create(title='Mario e Luigi salvam a princesa Peach sapateando.', 
    date=datetime(2018, 12, 10, 20), max_seatings=100, max_tickets=3)

    print u'%s created' % event_2.title

    # create reservations
    print u'creating some reservations'

    # mario = User.objects.filter(first_name='Mario').get()
    # luigi = User.objects.filter(first_name='Luigi').get()

    # event_1 = Event.objects.first()
    # event_2 = Event.objects.last()

    reserv = Reserv.objects.create(alumn=mario, event=event_1)
    reserv.seats.add(Seat.objects.filter(row='A', column='9', type='0').get())
    reserv.seats.add(Seat.objects.filter(row='A', column='11', type='0').get())
    reserv.seats.add(Seat.objects.filter(row='A', column='13', type='0').get())
    reserv.save()

    reserv = Reserv.objects.create(alumn=luigi, event=event_2)
    reserv.seats.add(Seat.objects.filter(row='F', column='18', type='1').get())
    reserv.seats.add(Seat.objects.filter(row='F', column='16', type='1').get())
    reserv.seats.add(Seat.objects.filter(row='F', column='14', type='1').get())
    reserv.save()

if __name__ == "__main__":
    populate()
