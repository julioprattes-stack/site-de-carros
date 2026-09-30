from django.urls import path
from cars.views import CarsListView, CarCreateView

app_name = 'cars'

urlpatterns = [
    path('cars/', CarsListView.as_view(), name='cars_list'),
    path('new_cars/', CarCreateView.as_view(), name='new_car')
]