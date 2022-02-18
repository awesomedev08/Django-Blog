from django.urls import path

from .views import LoginView, RegisterView

app_name = 'account'

urlpatterns = [ 
    path('register', RegisterView.as_view(), name='register_page'),
    path('login',LoginView.as_view(), name='login_page')
]