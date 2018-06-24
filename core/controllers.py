#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

import pdfkit
from django.http import HttpResponse
from django.template import Context, TemplateDoesNotExist
from django.template.loader import get_template
from rest_framework.exceptions import NotFound, ValidationError

from tapacademy import settings


def render_to_pdf(template_src, context={}):
    try:
        template = get_template(template_src)
    except TemplateDoesNotExist:
        raise ValidationError('Template não encontrado.')

    html = template.render(context)
    # return HttpResponse(html)

    pdfkit.from_string(html, 'confirmation.pdf')
    pdf = open('confirmation.pdf')

    response = HttpResponse(pdf.read(), content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=confirmation.pdf'
    
    pdf.close()
    os.remove('confirmation.pdf')
    
    return response


def render(template_src, context={}):
    try:
        template = get_template(template_src)
    except TemplateDoesNotExist:
        raise ValidationError('Template não encontrado.')

    html = template.render(context)
    
    return HttpResponse(html)

