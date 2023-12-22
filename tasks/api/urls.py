from django.urls import path
from .views import get_coolest_district, TravelRecomendation

urlpatterns = [
    path("coolest-districts/", get_coolest_district, name="coolest-districts"),
    path(
        "tarvel-recomendation/",
        TravelRecomendation.as_view(),
        name="travel-recomendation",
    ),
]
