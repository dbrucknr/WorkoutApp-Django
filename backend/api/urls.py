from django.urls import path

from .views import RunList, RunDetail

urlpatterns = [
    path("api/workouts/runs/", RunList.as_view()),
    path("api/workouts/runs/<int:pk>/", RunDetail.as_view()),
]