from django.urls import path
from cars.views import (
CarsListView,
NewCarCreateView,
CarDetailView,
CarUpdateView,
CarDeleteView
)

app_name = 'cars'

urlpatterns = [
    path('cars/', CarsListView.as_view(), name='cars_list'),
    path('new_cars/', NewCarCreateView.as_view(), name='new_car'),
    path('car/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('car/<int:pk>/update/', CarUpdateView.as_view(), name='car_update'),
    path('cars/<int:pk>delete/', CarDeleteView.as_view(), name='car_delete')
]