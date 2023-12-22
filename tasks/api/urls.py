from django.urls import path
from .views import get_coolest_district

urlpatterns = [
    path("coolest-districts/", get_coolest_district, name="coolest-districts"),
]
