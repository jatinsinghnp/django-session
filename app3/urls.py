from django.urls import path
from .views import settestcookie, deltestcookie, checktestcookie

urlpatterns = [
    path("set/", settestcookie),
    path("del/", deltestcookie),
    path("check/", checktestcookie),
]
