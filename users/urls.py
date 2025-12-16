from django.urls import path
from django.contrib.auth.views import LoginView
from .views import RegisterView, CustomLogoutView
from .forms import EmailAuthenticationForm


app_name = 'users'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(
        template_name='users/login.html',
        authentication_form=EmailAuthenticationForm
    ), name='login'),
]
