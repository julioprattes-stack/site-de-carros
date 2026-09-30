from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

class CustomLogoutView(LogoutView):
    next_page = 'cars:cars_list'

class RegisterCreateView(CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:login')



# class RegisterView(View):

#     def post(self, request):
#         user_form = UserCreationForm(request.POST)
#         if user_form.is_valid():
#             user_form.save()
#             return redirect('accounts:login')
#         context = {'user_form':user_form}
#         return render(
#         request,
#         'accounts/register.html',
#         context
#         )

#     def get(self, request):
#         user_form = UserCreationForm()
#         context = {'user_form':user_form}
#         return render(
#         request,
#         'accounts/register.html',
#         context
#         )