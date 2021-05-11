import http.client
import json
from datetime import datetime

from exception.HttpRequestException import HttpRequestException


def get_data(date: datetime, currency: str) -> dict:
    """
    Makes http call to external api and gets data based on given datetime and currency.

    Args:
         date (datetime): Datetime object.
         currency (str): Currency.

    Raises:
        HttpRequestException

    Returns:
         Parsed json response as a dictionary.
    """
    date_string = date.strftime("%Y-%m-%d")

    query = f"/api/exchangerates/rates/a/{currency}/{date_string}/?format=json"
    connection = http.client.HTTPConnection("api.nbp.pl")
    connection.request("GET", query)

    response = connection.getresponse()
    if 200 <= response.status < 300:
        return json.loads(response.read().decode())
    else:
        raise HttpRequestException(response.reason, response.status)
