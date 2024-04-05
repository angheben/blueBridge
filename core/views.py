from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import SignupForm, LoginForm
from django.urls import reverse_lazy
from django.views.generic import RedirectView, FormView
from django.contrib.auth import logout, authenticate, login


class ControlView(TemplateView):
    template_name = "control.html"


class LoginView(FormView):
    """
    This class will serve as the login view
    """
    template_name = "login.html"
    form_class = LoginForm
    success_url = reverse_lazy("core:control")

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            return self.form_invalid(form)


class SignupView(FormView):
    """
    This class will serve to check some dependencies in the project accordingly to the forms provided
    """
    template_name = 'signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('core:login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return render(self.request, self.template_name, {'form': form})


class LogoutView(RedirectView):
    url = reverse_lazy('core:control')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)
