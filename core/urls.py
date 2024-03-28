from .views import index, register, login, negotiate, register
from django.urls import path


urlpatterns = [
    path("", index, name="index"),
]
