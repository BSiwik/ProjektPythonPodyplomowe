from django.shortcuts import render
from .models import Car
from django.shortcuts import get_object_or_404

def car_list(request):
    cars = Car.objects.all().order_by('id')
    return render(request, 'cars/car_list.html', { 'cars': cars })

def car_detail(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    return render(request, 'cars/car_details.html', {'car': car})
