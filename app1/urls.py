from django.urls import path
from .views import home, setsession, getseeion,delseeion

urlpatterns = [
    path("", home),
    path("set/", setsession),
    path("get/", getseeion),
    path("del/", delseeion),
]
