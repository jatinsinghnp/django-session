from django.urls import path
from .views import home, setsession, getseeion

urlpatterns = [
    path("", home),
    path("set/", setsession),
    path("get/", getseeion),
]
