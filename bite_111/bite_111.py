"""
Bite 111. Use the ipinfo API to lookup IP country 
"""
import requests
from typing import Optional

IPINFO_URL = 'http://ipinfo.io/{ip}/json'

ADDRESSES = ['187.190.38.36', '185.161.200.10']


def get_ip_country(ip_address: str) -> Optional[str]:
    """Receives ip address string, use IPINFO_URL to get geo data,
       parse the json response returning the country code of the IP
    """
    with requests.Session() as session:
        j_data = session.get(IPINFO_URL.format(ip=ip_address)).json()
        if 'country' in j_data:
            return j_data['country']
    return None


if __name__ == "__main__":
    for address in ADDRESSES:
        country_code = get_ip_country(address)
        if country_code:
            print(country_code)