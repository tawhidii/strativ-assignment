import requests
import asyncio
import aiohttp
import heapq
from typing import List, Dict
from datetime import datetime, timedelta


API_ENDPOINT = "https://api.open-meteo.com/v1/forecast?latitude={0}&longitude={1}&datetime={2}&hourly=temperature_2m&timezone=auto"


def get_district_wise_data(districts, session):
    start_date = datetime.today() + timedelta(days=1)
    api_data = []
    for district in districts:
        api_data.append(
            session.get(
                url=API_ENDPOINT.format(
                    district["lat"], district["lon"], start_date.isoformat()
                )
            ),
        )
    return api_data


async def get_coolest_districts(districts):
    district_temperature = []
    async with aiohttp.ClientSession() as session:
        api_data = get_district_wise_data(districts=districts, session=session)
        responses = await asyncio.gather(*api_data)
        for res in responses:
            result = await res.json()
            district_temperature.append(
                {
                    "lat": result["latitude"],
                    "lon": result["longitude"],
                    "minimum_temperature": min(result["hourly"]["temperature_2m"]),
                }
            )
    coolest_district = heapq.nsmallest(
        10, district_temperature, key=lambda x: x["minimum_temperature"]
    )
    return coolest_district


def travel_recommender(location_lat_lon, destination_lat_lon, travel_date):
    _location_response = requests.get(
        API_ENDPOINT.format(
            location_lat_lon["lat"], location_lat_lon["lon"], travel_date
        )
    )
    _destination_response = requests.get(
        API_ENDPOINT.format(
            destination_lat_lon["lat"], destination_lat_lon["lon"], travel_date
        )
    )
    location_min_temp = min(_location_response.json()["hourly"]["temperature_2m"])
    destination_min_temp = min(_destination_response.json()["hourly"]["temperature_2m"])
    if location_min_temp > destination_min_temp:
        return {"message": "Dont Travel !"}
    if destination_min_temp > location_min_temp:
        return {"message": "Hurray !! You can travel !"}
