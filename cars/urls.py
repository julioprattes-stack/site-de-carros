from django.urls import path
from cars import views

app_name = 'cars'

urlpatterns = [
    path('cars/',views.cars_views, name='car')
]