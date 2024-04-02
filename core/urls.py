from .views import index, login, negotiate, signup
from django.urls import path


urlpatterns = [
    path("", index, name="index"),
    path("signup/", signup, name="signup"),
    path("login/", login, name="login"),
    path("negotiate/", negotiate, name='negotiate'),
]
