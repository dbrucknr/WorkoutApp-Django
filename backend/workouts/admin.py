from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from .models import Run

@admin.register(Run)
class RunAdmin(admin.ModelAdmin):
    fields = ("total_time", "total_distance", "date",)
    list_display = ("total_time", "total_distance", "date",)
