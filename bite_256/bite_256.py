""" 
Bite 256. Scrape PyCon events
"""
import json
from collections import namedtuple
from typing import List

import requests
from bs4 import BeautifulSoup as Soup
from dateutil.parser import parse

PYCON_DATA = "https://bites-data.s3.us-east-2.amazonaws.com/pycons.html"

PyCon = namedtuple("PyCon", "name city country start_date end_date url")

country_lookup = {
    "Africa": [
        "Algeria",
        "Angola",
        "Benin",
        "Botswana",
        "Burkina Faso",
        "Burundi",
        "Cameroon",
        "Cape Verde",
        "Central African Republic",
        "Chad",
        "Comoros",
        "Democratic Republic of the Congo",
        "Djibouti",
        "Egypt",
        "Equatorial Guinea",
        "Eritrea",
        "Ethiopia",
        "Gabon",
        "Ghana",
        "Guinea",
        "Guinea-Bissau",
        "Ivory Coast",
        "Kenya",
        "Lesotho",
        "Liberia",
        "Libya",
        "Madagascar",
        "Malawi",
        "Mali",
        "Mauritania",
        "Mauritius",
        "Morocco",
        "Mozambique",
        "Namibia",
        "Niger",
        "Nigeria",
        "Republic of the Congo",
        "Rwanda",
        "São Tome and Principe",
        "Senegal",
        "Seychelles",
        "Sierra Leone",
        "Somalia",
        "South Africa",
        "South Sudan",
        "Sudan",
        "Swaziland",
        "Tanzania",
        "The Gambia",
        "Togo",
        "Tunisia",
        "Uganda",
        "Zambia",
        "Zimbabwe",
    ],
    "Asia": [
        "Afghanistan",
        "Armenia",
        "Azerbaijan",
        "Bahrain",
        "Bangladesh",
        "Bhutan",
        "Brunei",
        "Cambodia",
        "China",
        "East Timor",
        "Georgia",
        "India",
        "Indonesia",
        "Iran",
        "Iraq",
        "Israel",
        "Japan",
        "Jordan",
        "Kazakhstan",
        "Kuwait",
        "Kyrgyzstan",
        "Laos",
        "Lebanon",
        "Malaysia",
        "Maldives",
        "Mongolia",
        "Myanmar",
        "Nepal",
        "North Korea",
        "Oman",
        "Pakistan",
        "Palestinian territories",
        "Philippines",
        "Qatar",
        "Saudi Arabia",
        "Singapore",
        "South Korea",
        "Sri Lanka",
        "Syria",
        "Taiwan",
        "Tajikistan",
        "Thailand",
        "Turkey",
        "Turkmenistan",
        "United Arab Emirates",
        "Uzbekistan",
        "Vietnam",
        "Yemen",
    ],
    "Australia and Oceania": [
        "Australia",
        "Federated States of Micronesia",
        "Fiji",
        "Kiribati",
        "Marshall Islands",
        "Nauru",
        "New Zealand",
        "Palau",
        "Papua New Guinea",
        "Samoa",
        "Solomon Islands",
        "Tonga",
        "Tuvalu",
        "Vanuatu",
    ],
    "Europe": [
        "Albania",
        "Andorra",
        "Austria",
        "Belarus",
        "Belgium",
        "Bosnia and Herzegovina",
        "Bulgaria",
        "Croatia",
        "Cyprus",
        "Czech Republic",
        "Denmark",
        "Estonia",
        "Finland",
        "France",
        "Germany",
        "Greece",
        "Hungary",
        "Iceland",
        "Italy",
        "Latvia",
        "Liechtenstein",
        "Lithuania",
        "Luxembourg",
        "Malta",
        "Moldova",
        "Monaco",
        "Montenegro",
        "Netherlands",
        "Norway",
        "Poland",
        "Portugal",
        "Republic of Ireland",
        "Republic of Macedonia",
        "Romania",
        "Russia",
        "San Marino",
        "Serbia",
        "Slovakia",
        "Slovenia",
        "Spain",
        "Sweden",
        "Switzerland",
        "Ukraine",
        "United Kingdom",
        "U.K.",
        "Vatican City",
    ],
    "North America": [
        "Antigua and Barbuda",
        "Barbados",
        "Belize",
        "Canada",
        "Costa Rica",
        "Cuba",
        "Dominica",
        "Dominican Republic",
        "El Salvador",
        "Grenada",
        "Guatemala",
        "Haiti",
        "Honduras",
        "Jamaica",
        "Mexico",
        "Nicaragua",
        "Panama",
        "Saint Kitts and Nevis",
        "Saint Lucia",
        "Saint Vincent and the Grenadines",
        "The Bahamas",
        "Trinidad and Tobago",
        "United States of America",
        "U.S.A.",
    ],
    "South America": [
        "Argentina",
        "Bolivia",
        "Brazil",
        "Chile",
        "Colombia",
        "Ecuador",
        "Guyana",
        "Paraguay",
        "Peru",
        "Suriname",
        "Uruguay",
        "Venezuela",
    ],
}


def get_continent(country: str) -> str:
    """
    Given a country name returns the associated continent of the country.

    :param country: The name of the country
    :type country: str
    :returns: The continent of the country
    :rtype: str
    """
    for continent, countries in country_lookup.items():
        for c in countries:
            if country.lower() in c.lower():
                return continent


def _get_pycon_data():
    """Helper function that retrieves the required PyCon data"""
    with requests.Session() as session:
        return session.get(PYCON_DATA).content.decode("utf-8")


def get_pycon_events(data=_get_pycon_data()) -> List[PyCon]:
    """
    Scrape the PyCon events from the given website data and
    return a list of PyCon namedtuples. Pay attention to the
    application/ld+json data structure website data.
    """
    bs = Soup(data, "html.parser")

    pycon_events = []

    # NOTE: find all script tags as they contain a json string
    for x in bs.findAll("script"):
        parse_json = json.loads(x.text.strip())

        # JSON DATA
        event_name = parse_json["name"]
        if "PyCon" not in event_name:
            continue

        event_city = parse_json["location"]["address"]["addressLocality"]
        event_country = parse_json["location"]["address"]["addressCountry"]
        event_start_date = parse_json["startDate"]
        event_end_date = parse_json["endDate"]
        event_url = parse_json["url"]

        # PARSE TIMES
        start_date_dt = parse(event_start_date)
        end_date_dt = parse(event_end_date)

        # NEW PYCON
        new_pycon = PyCon(name=event_name,
                          city=event_city,
                          country=event_country,
                          start_date=start_date_dt,
                          end_date=end_date_dt,
                          url=event_url)

        pycon_events.append(new_pycon)

    # SORTED BY CITY
    return sorted(pycon_events, key=lambda x: x.city)


def filter_pycons(pycons: List[PyCon],
                  year: int = 2019,
                  continent: str = "Europe") -> List[PyCon]:
    """
    Given a list of PyCons a year and a continent return
    a list of PyCons that take place in that year and on
    that continent.
    """

    results = []

    for con in pycons:
        con_year = con.start_date.year
        con_continent = get_continent(con.country)

        if con_year == year and con_continent == continent:
            results.append(con)

    return results


if __name__ == "__main__":
    pycon_data = _get_pycon_data()
    cons = get_pycon_events(pycon_data)

    for con in filter_pycons(pycons=cons):
        print(con.city)