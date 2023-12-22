from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from asgiref.sync import sync_to_async
from adrf.decorators import api_view
from rest_framework.response import Response
from tasks.models import District
from tasks.utils.open_meteo import get_coolest_districts, travel_recommender


@api_view(["GET"])
async def get_coolest_district(request):
    """api view for getting 10 coolest districts"""
    districts = [
        district async for district in District.objects.values("name", "lat", "lon")
    ]
    coolest_district = await get_coolest_districts(districts)

    return Response(data=coolest_district, status=status.HTTP_200_OK)


class TravelRecomendation(APIView):
    """api view for travel recommendation"""

    def post(self, request):
        location_obj = get_object_or_404(District, name=request.data["location"])
        destination_obj = get_object_or_404(District, name=request.data["destination"])
        location_lat_lon = {"lat": location_obj.lat, "lon": location_obj.lon}
        destination_lat_lon = {"lat": destination_obj.lat, "lon": destination_obj.lon}

        result = travel_recommender(
            location_lat_lon=location_lat_lon,
            destination_lat_lon=destination_lat_lon,
            travel_date=request.data["travel_date"],
        )

        return Response(data=result, status=status.HTTP_200_OK)
