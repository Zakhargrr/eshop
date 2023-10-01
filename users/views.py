from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from users.forms import UserRegisterForm, UserProfileForm
from users.models import User
import secrets


# Create your views here.
class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        new_user = form.save()
        new_user.generated_key = secrets.token_urlsafe(16)
        new_user.user_key = None
        new_user.save()
        send_mail(
            subject="Ключ для верификации почты",
            message=f"{new_user.generated_key} - ваш ключ для верификации почты",
            from_email="noreply@oscarbot.ru",
            recipient_list=[new_user.email]
        )
        return super().form_valid(form)


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        edit_user = form.save()
        if edit_user.user_key == edit_user.generated_key:
            edit_user.is_verified = True
        else:
            edit_user.user_key = None
        return super().form_valid(form)


def generate_new_password(request):
    new_password = secrets.token_urlsafe(16)
    send_mail(
        subject="Новый пароль",
        message=f"Ваш новый пароль: {new_password}",
        from_email="noreply@oscarbot.ru",
        recipient_list=[request.user.email]
    )
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse('catalog:home'))
