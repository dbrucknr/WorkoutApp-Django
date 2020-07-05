from django.contrib import admin
from django.urls import path
from .views import data_test

urlpatterns = [
    path('admin/', admin.site.urls),
    path('data/', data_test, name="data")
]
