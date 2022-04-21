from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("hellow world i am a hacker man 124 ")


def setsession(request):

    request.session["name"] = "jatin singh"
    return render(request, "setsession.html")


def getseeion(request):

    # cart get method added
    name = request.session["name"]
    return render(
        request,
        "getsession.html",
        {
            "name": name,
           
        },
    )


def delseeion(request):
    # if "name" and "cart" in request.session:
    #     del request.session["name"]
    #     del request.session["cart"]

    request.session.flush()
    return render(request, "delsession.html")
