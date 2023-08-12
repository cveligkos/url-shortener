from django.http import HttpRequest, HttpResponse, HttpResponseNotAllowed
from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse

from links.forms import LinkForm
from links.models import Link
from .shortener import shorten_url
from django.contrib import messages


def link_list(request: HttpRequest):
    links = Link.objects.all()
    context = {"links": links, "host_url": request.get_host()}
    return TemplateResponse(request, "links/list.html", context)


def link_create(request: HttpRequest):
    if request.method == "GET":
        return TemplateResponse(request, "links/create.html", {"link": Link()})
    elif request.method != "POST":
        return HttpResponseNotAllowed(["GET", "POST"])

    form = LinkForm(request.POST)
    form.is_valid()
    if "url" not in form.errors:
        data = form.data.copy()
        data["hash"] = shorten_url(request.POST.get("url"))
        form = LinkForm(data)

    if form.is_valid():
        form.save()
        return redirect("link_list")
    else:
        form = LinkForm()

    return TemplateResponse(request, "links/create.html", {"form": form})


def link_delete(request: HttpRequest, pk: int):
    if request.method != "DELETE":
        return HttpResponseNotAllowed(["DELETE"])

    link = get_object_or_404(Link, pk=pk)

    link.delete()

    response = HttpResponse()
    response.headers["HX-Redirect"] = reverse("link_list")
    return response
