from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class CarMain(models.Model):
    make = models.CharField(max_length=16)
    models = models.CharField(max_length=32)

class CarDetail(models.Model):
    CAR_TRANSMISSION = [
        ("AUTOMATIC", "Automatic"),
        ("MANUAL", "Manual"),
    ]

    CAR_FUELS=[
        ("PET", "Petrol"),
        ("LPG", "LPG"),
        ("ELE", "Electric"),
    ]



    production_date = models.DateField()
    transmission = models.CharField(max_length=9, choices=CAR_TRANSMISSION)
    seats = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    fuel = models.CharField(max_length=3, choices=CAR_FUELS)
    power = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2, validators=[MinValueValidator(0.00)])



class Car(models.Model):
    main = models.ForeignKey(CarMain, on_delete=models.CASCADE)
    detail = models.OneToOneField(CarDetail, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.main.make} {self.main.models}"
