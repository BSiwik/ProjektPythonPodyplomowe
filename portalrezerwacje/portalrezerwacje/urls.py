from django.contrib import admin
from django.urls import path, include
from .views import HomePageView

app_name = 'portalrezerwacje'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', include('cars.urls')),
    path('accounts/', include('accounts.urls')),
    path('', HomePageView.as_view(), name='homepage'),
    path('rental/', include('rental.urls', namespace='rental')),


]
