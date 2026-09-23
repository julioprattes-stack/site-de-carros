from django.shortcuts import render
from cars.models import CarModel

def cars_views(request):
    cars = CarModel.objects.all()

    context = {
        'cars':cars
    }

    return render(
        request,
        'cars/cars.html',
        context
    )
