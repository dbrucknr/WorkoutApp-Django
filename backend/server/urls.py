from django.contrib import admin
from django.urls import path, include
from .views import data_test

urlpatterns = [
    path('', include('api.urls')),
    path('admin/', admin.site.urls),
    path('data/', data_test, name="data"),
]
