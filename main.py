from exception.HttpRequestException import HttpRequestException
from exception.InvalidJsonSchemaException import InvalidJsonSchemaException
from http_client.get_data import get_data
from http_client.mapper import mapper
from input.get_currency import get_currency
from input.get_date import get_date

if __name__ == '__main__':
    while True:
        date = get_date()
        currency = get_currency()
        try:
            result = get_data(date, currency)
            rates = mapper(result)
        except HttpRequestException as error:
            print(f"Http request error, Status: {error.status}, Reason: {error.message}")
            continue
        except InvalidJsonSchemaException() as error:
            print("Searched key does not exist in the response, try again")
            continue


