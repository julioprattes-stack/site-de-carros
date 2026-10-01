from django.db.models.signals import post_save, post_delete
from django.db.models import Sum
from django.dispatch import receiver
from cars.models import CarModel, CarInventoryModel


def car_inventory_update():
    cars_count = CarModel.objects.all().count()
    cars_value = CarModel.objects.aggregate(
        total_value=Sum('value')
    )['total_value'] or 0

    CarInventoryModel.objects.create(
        cars_count=cars_count,
        cars_value=cars_value
    )

@receiver(post_save, sender=CarModel)
def car_post_save(sender, instance, **kwargs):
    car_inventory_update()

@receiver(post_delete, sender=CarModel)
def car_post_delete(sender, instance, **kwargs):
    car_inventory_update()