from django.shortcuts import render
from cars.models import CarModel

def cars_views(request):
    cars = CarModel.objects.all().order_by('model')
    search = request.GET.get('search')

    if search:
        cars = CarModel.objects.filter(model__icontains=search).order_by('model')
    
    context = {
        'cars':cars
    }

    return render(
        request,
        'cars/cars.html',
        context
    )