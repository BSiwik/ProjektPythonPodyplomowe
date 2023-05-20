from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.views import View
from cars.models import Car
from django.shortcuts import render, redirect
from .models import Rental


class RentalDetailView(View):
    def post(self, request, car_id):
        car = get_object_or_404(Car, id=car_id)
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        user = request.user
        allrentalsforcar = Rental.objects.filter(car=car, start_date__gte=start_date,end_date__lte=end_date)
        if not allrentalsforcar:
            rental = Rental(car=car, user=user, start_date=start_date, end_date=end_date)
            rental.save()
            messages.success(request, 'Car rental request submitted successfully!')
            return redirect('rental:rent_confirmation', rental_id=rental.id)
        else:
            return redirect('rental:incorrect_dates')






    def get(self, request, car_id):
        car = get_object_or_404(Car, id=car_id)
        return render(request, 'rental_detail.html', {'car': car})



def rent_confirmation(request, rental_id):
    rental = get_object_or_404(Rental, pk=rental_id)
    return render(request, 'rent_confirmation.html', {'rental': rental})

def incorrect_dates(request):
    return render(request, 'incorrect_dates.html')