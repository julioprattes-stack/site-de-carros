from django.shortcuts import render, redirect
from cars.models import CarModel
from cars.forms import CarForm

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

def new_car_views(request):
    if request.method == 'POST':
        new_car_form = CarForm(request.POST, request.FILES)

        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars:cars_list')
        
    else:
        new_car_form = CarForm()

    context = {
        'new_car_form': new_car_form
    }

    return render(
        request,
        'cars/new_car.html',
        context
    )