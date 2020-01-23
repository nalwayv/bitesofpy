""" 
Bite 261. Visit all PyCons in Europe 
"""
import json
from dataclasses import dataclass
from datetime import datetime
from math import acos, cos, radians, sin
import os
from pathlib import Path
# from urllib.request import urlretrieve

from dateutil.parser import parse
from typing import List

# URL = "https://bites-data.s3.us-east-2.amazonaws.com/pycons-europe-2019.json"
# RESPONSES = "https://bites-data.s3.us-east-2.amazonaws.com/nominatim_responses.json"

tmp = Path(os.path.join(os.path.dirname(__file__), "tmp"))

pycons_file = tmp / "pycons-europe-2019.json"
nominatim_responses = tmp / "nominatim_responses.json"

# if not pycons_file.exists() or not nominatim_responses.exists():
#     urlretrieve(URL, pycons_file)
#     urlretrieve(RESPONSES, nominatim_responses)


@dataclass
class PyCon:
    name: str
    city: str
    country: str
    start_date: datetime
    end_date: datetime
    URL: str
    lat: float = None
    lon: float = None


@dataclass
class Trip:
    origin: PyCon
    destination: PyCon
    distance: float


def _get_pycons():
    """Helper function that retrieves required PyCon data
       and returns a list of PyCon objects
    """
    with open(pycons_file, "r", encoding="utf-8") as f:
        return [
            PyCon(
                pycon["name"],
                pycon["city"],
                pycon["country"],
                parse(pycon["start_date"]),
                parse(pycon["end_date"]),
                pycon["url"],
            ) for pycon in json.load(f)
        ]


def _km_distance(origin, destination):
    """ Helper function that retrieves the air distance in kilometers for two pycons """
    lon1, lat1, lon2, lat2 = map(
        radians, [origin.lon, origin.lat, destination.lon, destination.lat])
    return 6371 * (
        acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lon1 - lon2)))


# Your code #
def update_pycons_lat_lon(pycons: List[PyCon]):
    """
    Update the latitudes and longitudes based on the city and country
    the PyCon takes places. Use requests from the Nominatim API stored in the
    nominatim_responses json file.
    """
    with open(nominatim_responses, "r") as f:

        json_cons = json.load(f)
        for py in pycons:
            key = f"https://nominatim.openstreetmap.org/search?q={py.city},{py.country}&format=json&accept-language=en"
            for d in json_cons[key]:
                if d["type"] == "city" and d["class"] == "place":
                    py.lat = float(d["lat"])
                    py.lon = float(d["lon"])
                    break


def create_travel_plan(pycons):
    """
    Create your travel plan to visit all the PyCons.
    Assume it's now the start of 2019!
    Return a list of Trips with each Trip containing the origin PyCon,
    the destination PyCon and the travel distance between the PyCons.
    """
    sorted_by_date = sorted(pycons, key=lambda x: x.start_date)
    trips: List[Trip] = []

    for i in range(1, len(sorted_by_date)):
        first = sorted_by_date[i - 1]
        dest = sorted_by_date[i]
        trips.append(
            Trip(
                origin=first,
                destination=dest,
                distance=_km_distance(first, dest),
            ))

    return trips


def total_travel_distance(journey):
    """
    Return the total travel distance of your PyCon journey in kilometers
    rounded to one decimal.
    """
    return round(sum([j.distance for j in journey]), 1)
