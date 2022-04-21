from django.urls import path
from .views import setcookie, getcookie, setSignedCookie, getsignedcookie, delcookies

urlpatterns = [
    path("", setcookie),
    path("get", getcookie),
    path("setsign", setSignedCookie),
    path("getsign", getsignedcookie),
    path("del", delcookies),
]
