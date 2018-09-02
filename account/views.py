from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import TemplateView


class LoginView(TemplateView):
    def get(self, request):
        context = {
            "form": LoginForm
        }
        return render(request, 'auth/login.html', context)

    def post(self, request):
        form = AuthenticationForm(None, request.POST)
        response_data = {}


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

            errors = []
            for i in form.errors.get('__all__'):
                errors.append(i)

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
