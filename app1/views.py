from email.policy import default
from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse("hellow world i am a hacker man 124 ")


def setsession(request):

    request.session["name"] = "jatin singh"
    request.session["cart"] = "hellow world"
    return render(request, "setsession.html")


def getseeion(request):
    name = request.session.get("name",default=None)
    cart = request.session.get("cart",default=None)
    return render(
        request,
        "getsession.html",
        {
            "name": name,
            "cart": cart,
        },
    )
