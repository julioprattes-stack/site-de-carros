from django.db.models.signals import post_save, post_delete, pre_save
from django.db.models import Sum
from django.dispatch import receiver
from cars.models import CarModel, CarInventoryModel
from openai_api.client import get_car_ai_bio


def car_inventory_update():
    cars_count = CarModel.objects.all().count()
    cars_value = CarModel.objects.aggregate(
        total_value=Sum('value')
    )['total_value'] or 0

    CarInventoryModel.objects.create(
        cars_count=cars_count,
        cars_value=cars_value
    )

@receiver(pre_save, sender=CarModel)
def car_pre_save(sender, instance, **kwargs):
    if not instance.bio:
        ia_bio = get_car_ai_bio(
            instance.brand,
            instance.model,
            instance.model_year
        )
        
        instance.bio = ia_bio

@receiver(post_save, sender=CarModel)
def car_post_save(sender, instance, **kwargs):
    car_inventory_update()

@receiver(post_delete, sender=CarModel)
def car_post_delete(sender, instance, **kwargs):
    car_inventory_update()