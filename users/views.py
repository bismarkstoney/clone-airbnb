import email
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, SignUpForm
# Create your views here.

class Login(FormView):
    
    template_name = "users/login.html"
    form_class = LoginForm

    def form_valid(self, form):
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password"]
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        # user.verify_email(email)
        return super().form_valid(form)

    def get_success_url(self):
        next_arg = self.request.GET.get("next")
        if next_arg is not None:
            return next_arg
        else:
            return reverse("core:home")
def log_out(request):
    logout(request)
    return redirect(reverse('core:home'))

class Sigup(FormView):
    template_name = "users/signup.html"
    form_class = SignUpForm
    success_url=reverse_lazy('core:home')
    
        