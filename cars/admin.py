from django.contrib import admin
from cars.models import CarModel, BrandModel

@admin.register(CarModel)
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model',)

@admin.register(BrandModel)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)