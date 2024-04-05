from .views import ControlView, SignupView, LoginView
from django.urls import path

urlpatterns = [
    path("", ControlView.as_view(), name="control"),
    path("signup/", SignupView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
]
