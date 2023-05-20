from django.db import models
from cars.models import Car
from django.conf import settings

class Rental(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def total_price(self):
        days = (self.end_date - self.start_date).days + 1
        return days * self.car.detail.price
