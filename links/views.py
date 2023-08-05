from django.template.response import TemplateResponse
from django.shortcuts import render


def list(request):
    return TemplateResponse(request, "links/list.html", {})
