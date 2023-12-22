import asyncio
from rest_framework import status
from asgiref.sync import sync_to_async
from adrf.decorators import api_view
from rest_framework.response import Response
from tasks.models import District
from tasks.utils.open_meteo import get_coolest_districts


@api_view(["GET"])
async def get_coolest_district(request):
    districts = [
        district async for district in District.objects.values("name", "lat", "lon")
    ]
    coolest_district = await get_coolest_districts(districts)

    return Response(data=coolest_district)
