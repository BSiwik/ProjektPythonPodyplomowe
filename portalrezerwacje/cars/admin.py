from django.contrib import admin
from .models import Car, CarDetail, CarMain
# Register your models here.

class CarAdmin(admin.ModelAdmin):
    model = Car
    list_display = ["get_main_make", "get_main_model", "get_detail_production_date"]

    def get_main_make(self, obj):
        return obj.main.make

    def get_main_model(self, obj):
        return obj.main.models

    def get_detail_production_date(self, obj):
        return obj.detail.production_date

admin.site.register(Car, CarAdmin)
admin.site.register(CarDetail)
admin.site.register(CarMain)