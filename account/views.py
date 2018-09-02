from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from .forms import LoginForm, RegisterForm
from django.http import JsonResponse
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from api.models import Package
from django_gravatar.helpers import has_gravatar, get_gravatar_url
from django.contrib.auth.mixins import LoginRequiredMixin
from ratelimit.decorators import ratelimit
from rest_framework.authtoken.models import Token


class AccountView(TemplateView):
    '''
    Profile page for user
    '''

    def get(self, request, username=""):
        context = {}
        user_details = get_object_or_404(User, username=username)
        user_packages = Package.objects.filter(user=user_details.id)

        if has_gravatar(user_details.email):
            context["profile_picture"] = get_gravatar_url(
                user_details.email, size=650)

        context["user_package_count"] = len(user_packages)
        context["username"] = user_details.username
        context["user_packages"] = user_packages
        return render(request, 'auth/account.html', context)


class AccountTokenView(LoginRequiredMixin, TemplateView):

    def get(self, request):
        context = {}
        return render(request, 'auth/get_token.html', context)

    @ratelimit(key="ip", rate="2/d", block=True)
    def post(self, request):
        token = Token.objects.filter(user=request.user)
        if token.exists() and not request.POST.get('generate_new_token'):
            return JsonResponse({"status": False, "message": "Your account has already a token.", "key": token.get(user=request.user).key})
        elif request.POST.get('generate_new_token'):
            update_token = Token.objects.filter(user=request.user)
            update_token.delete()

        create_token = Token.objects.create(user=request.user)
        if create_token:
            return JsonResponse({"status": True, "message": "You successfully generated your new key!", "key": create_token.key})

class LoginView(TemplateView):
    def get(self, request):
        context = {
            "form": LoginForm
        }
        return render(request, 'auth/login.html', context)

    def post(self, request):
        form = AuthenticationForm(None, request.POST)
        response_data = {
            'form': form
        }


        if request.user.is_authenticated:
            return self.__returnMessage(request, False, "You're already logged in!")

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            try_login = login(request, user)
            return self.__returnMessage(request, True, 'Successfully logged in, you\'ll be redirected soon')
        else:
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            if not username or not password:
                return self.__returnMessage(request, False, 'You have empty field(s). Please fill them if you want to contiune')

            errors = [i for i in form.errors.get('__all__')]

            errors = '\n'.join(errors)
            return self.__returnMessage(request, False, errors)

        if request.is_ajax():
            return self.__returnMessage(request, True, "tamam")
        else:
            response_data['form'] = form

        return render(request, 'auth/login.html', response_data)


    def __returnMessage(self, request, status, message):
        if request.is_ajax():
            return JsonResponse({
                "status": status,
                "message": message
            })
        else:
            context = {
                "message": message
            }
            if status:
                context["success"] = True
            else:
                context["error"] = True

            print(context)
            return render(request, 'auth/login.html', context)



class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy('PackagesPage')

    def form_valid(self, form):
        created = form.create_user(self.request)
        if created:
            auth = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password1'))
            login_to_system = login(self.request, auth)
            messages.success(self.request, 'You have successfully registered.')
        else:
            messages.error(
                self.request, 'Could not register, please try again another time.')
        return super().form_valid(form)


@login_required
def logout_view(request):
    logout(request)
    return redirect(reverse('PackagesPage'))
