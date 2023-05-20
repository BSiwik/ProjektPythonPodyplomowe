from django.urls import path
from .views import  rent_confirmation, RentalDetailView, incorrect_dates

app_name = 'rental'

urlpatterns = [
    path('<int:car_id>/', RentalDetailView.as_view(), name='rental_detail'),
    path('rent_confirmation/<int:rental_id>/', rent_confirmation, name='rent_confirmation'),
    path('incorrect_dates', incorrect_dates, name='incorrect_dates')
]
