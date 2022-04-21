from datetime import datetime, timedelta
from unicodedata import name
from urllib import request, response
from django.shortcuts import render

# Create your views here.
def setcookie(request):
    response = render(request, "student/setcookie.html")
    response.set_cookie("name", "sonam")
    return response


def getcookie(request):
    name = request.COOKIES.get("name", None)
    return render(request, "student/getcookies.html", {"name": name})


def setSignedCookie(request):
    response = render(request, "signedcookie/setsignedcookie.html")
    response.set_signed_cookie(
        "name", "jatin", salt="nm", expires=datetime.utcnow() + timedelta(days=2)
    )
    return response


def getsignedcookie(request):
    name = request.get_signed_cookie("name", salt="nm")
    return render(request, "signedcookie/getsigncookie.html", {"name": name})


def delcookies(request):
    response = render(request, "signedcookie/delcookies.html")
    response.delete_cookie("name")
    return response
