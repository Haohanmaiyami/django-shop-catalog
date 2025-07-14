from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import UserRegisterForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.views import LogoutView
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import View

class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        response = super().form_valid(form)
        send_mail(
            subject='Добро пожаловать!',
            message='Вы успешно зарегистрировались на DjangoShop!',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[form.cleaned_data['email']],
        )
        return response

class CustomLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('products:products_list')