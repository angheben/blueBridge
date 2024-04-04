from .views import login,  signup # about, negotiate, index,
from .views import ControlView
from django.urls import path


urlpatterns = [
    path("", ControlView.as_view(), name="control"),
    path("signup/", signup, name="signup"),
    path("login/", login, name="login"),
]

"""
    path("", index, name="index"),

    path("negotiate/", negotiate, name='negotiate'),
    path("about/", about, name='negotiate'),
"""
