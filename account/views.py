from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login
from django.contrib import messages

from .forms import LoginForm, RegisterForm

class RegisterView(FormView):
    template_name = 'account/register.html'
    form_class = RegisterForm
    

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse('account:login_page'))

        return super(RegisterView, self).dispatch(request, *args, **kwargs)
    
    def get_success_url(self) -> str:
        return reverse('account:login_page')
    
    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Registered!!!!')
        return redirect(reverse('account:login_page'))
    
    
class LoginView(FormView):
    template_name = 'account/login.html'
    form_class = LoginForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse('dashboard:dashboard_index'))

        return super(LoginView, self).dispatch(request, *args, **kwargs)
    
    def get_success_url(self) -> str:
        return reverse('account:login_page')
    
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        validate = authenticate(username=username, password=password)
        if validate:
            login(request, validate)
            return redirect(reverse('dashboard:dashboard_index'))
            
        messages.warning(request, 'invalid username/password')
        return redirect(reverse('account:login_page'))    

