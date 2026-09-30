from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

class CustomLogoutView(LogoutView):
    next_page = 'cars:cars_list'

class RegisterView(View):

    def post(self, request):
        if request.method == 'POST':
            user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('accounts:login')
        context = {'user_form':user_form}
        return render(
        request,
        'accounts/register.html',
        context
        )

    def get(self, request):
        user_form = UserCreationForm()
        context = {'user_form':user_form}
        return render(
        request,
        'accounts/register.html',
        context
        )