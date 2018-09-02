from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ("username", "password",)

class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    def create_user(self, request):
        if self.is_valid():
            username = self.cleaned_data.get("username")
            password = self.cleaned_data.get("password1")

            if request.user.is_authenticated:
                messages.add_message(request, messages.ERROR, 'You already have a account!')
                return False

            try:
                createUser = self.save()
            except Exception as e:
                print(e)
                return False

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )
