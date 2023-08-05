from django.template.response import TemplateResponse
from django.shortcuts import render


def index(request):
    return TemplateResponse(request, "console/index.html", {})
