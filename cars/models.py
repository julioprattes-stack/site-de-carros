from django.db import models


class BrandModel(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class CarModel(models.Model):
    model = models.CharField(max_length=200)
    brand = models.ForeignKey(
        BrandModel,
        on_delete=models.PROTECT,
        null=True,
        related_name='car_brand'
    )
    factory_year = models.IntegerField(
        blank=True,
        null=True
    )
    model_year = models.IntegerField(
        blank=True,
        null=True
    )
    plate = models.CharField(
        max_length=10,
        blank=True,
        null=True
    )
    value = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    photo = models.ImageField(
        upload_to='cars/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.model