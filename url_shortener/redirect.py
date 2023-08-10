from django.http import HttpRequest, HttpResponseGone, HttpResponseRedirect
from django.shortcuts import get_object_or_404

from links.models import Link


def link_redirect(request: HttpRequest, hash: str):
    link = get_object_or_404(Link, hash=hash)
    link.visits += 1
    link.save()
    return HttpResponseRedirect(link.url)
