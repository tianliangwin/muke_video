#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from mako.lookup import TemplateLookup
from django.template import RequestContext
from django.conf import settings
from django.template.context import Context
from django.http import HttpResponse

def render_to_response(request,template,data=None):
    context_instance = RequestContext(request)
    path = settings.TEMPLATES[0]['DIRS'][0]
    lookup = TemplateLookup(
        directories=[path],
        input_encoding='utf-8',
        output_encoding='utf-8'
    )
    moko_template = lookup.get_template(template)
    if not data:
        data ={}
    if context_instance:
        context_instance.update(data)
    else:
        context_instance=Context(data)
    result ={}
    for d in context_instance:
        result.update(d)
    result['request'] =request
    result['csrf_token'] = (
        '<input type="hidden" '
        'name="csrfmiddlewaretoken" '
        'value="{0}" />'.format(
            request.META.get('CSRF_COOKIE', '')),)

    return HttpResponse(moko_template.render(**result))