from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponseNotAllowed,
    HttpResponseRedirect,
    response,
)
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from users.forms import RegisterForm

from django.contrib import messages


def user_login(request: HttpRequest):
    if request.method == "GET":
        return TemplateResponse(request, "users/login.html", {})
    elif request.method != "POST":
        return HttpResponseNotAllowed(["GET", "POST"])

    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("home"))
    else:
        # Todo: return invalid error message
        return TemplateResponse(request, "users/login.html", {})


def user_logout(request: HttpRequest):
    logout(request)
    return redirect("home")


def user_register(request: HttpRequest):
    if request.method == "GET":
        return TemplateResponse(request, "users/register.html", {})
    elif request.method != "POST":
        return HttpResponseNotAllowed(["GET", "POST"])

    form = RegisterForm(request.POST)
    if form.is_valid():
        user = form.save()
        messages.success(request, "You registered successfully!")  # noqa: F821
        login(request, user)
        return redirect("home")
    else:
        return TemplateResponse(request, "users/register.html", {})
