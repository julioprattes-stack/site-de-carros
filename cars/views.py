from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from cars.models import CarModel
from cars.forms import CarForm


class CarsListView(ListView):
     model = CarModel  #queryset
     template_name = 'cars/cars.html'
     context_object_name = 'cars'

     def get_queryset(self):
        queryset = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(model__icontains=search)
        return queryset

class CarDetailView(DetailView):
    model = CarModel
    template_name = 'cars/car_detail.html'
    
class NewCarCreateView(LoginRequiredMixin, CreateView):
    model = CarModel
    form_class = CarForm
    template_name = 'cars/new_car.html'
    success_url = reverse_lazy('cars:cars_list')

class CarUpdateView(LoginRequiredMixin, UpdateView):
    model = CarModel
    form_class = CarForm
    template_name = 'cars/car_update.html'

    def get_success_url(self):
        return reverse_lazy(
            'cars:car_detail',
            kwargs={'pk': self.object.pk}
        )

class CarDeleteView(LoginRequiredMixin, DeleteView):
    model = CarModel
    template_name = 'cars/car_delete.html'
    success_url = reverse_lazy('cars:cars_list')




# class NewCarView(View):
#     def post(self, request):
#             new_car_form = CarForm(request.POST, request.FILES)
#             if new_car_form.is_valid():
#                 new_car_form.save()
#                 return redirect('cars:cars_list')
#             context = {'new_car_form': new_car_form}
#             return render(
#                 request,
#                 'cars/new_car.html',
#                 context
#             )

#     def get(self, request):
#         new_car_form = CarForm()
#         context = {'new_car_form': new_car_form}
#         return render(
#             request,
#             'cars/new_car.html',
#             context
#         )