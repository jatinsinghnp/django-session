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
    try:
        print(request.session)  # session object is here
        # name = request.session.get("name", default=None)
        # cart = request.session.get("cart", default=None)
        keys = request.session.keys()
        items = request.session.items()
        age = request.session.setdefault("age", "26")
    except NameError:
        print("error the session is empty")

    return render(
        request,
        "getsession.html",
        {
            # "name": name,
            # "cart": cart,
            "keys": keys,
            "items": items,
            "age": age,
        },
    )


def delseeion(request):
    if "name" and "cart" in request.session:
        del request.session["name"]
        del request.session["cart"]

    return render(request, "delsession.html")
