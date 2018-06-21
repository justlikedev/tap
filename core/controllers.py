#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from io import BytesIO

from django.http import HttpResponse
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from rest_framework.exceptions import NotFound, ValidationError
from xhtml2pdf import pisa

from tapacademy import settings


def render_to_pdf(template_src, context={}):
    # TEMPLATE_DIR = os.path.join(settings.TEMPLATE_DIRS[0], template_src)
    
    try:
        template = get_template(template_src)
    except TemplateDoesNotExist:
        raise ValidationError('Template não encontrado.')

    html = template.render(context)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode('ISO-8859-1')), result)
    
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    
    return None
