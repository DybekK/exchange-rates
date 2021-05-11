from exception.HttpRequestException import HttpRequestException
from exception.InvalidJsonSchemaException import InvalidJsonSchemaException
from http_client.get_data import get_data
from http_client.mapper import mapper
from input.get_currency import get_currency
from input.get_date import get_date


def main():
    """Inside the main function, the entire application is initialized, the user input is retrieved, and the response
    is displayed. If an error occurs while running the application, it is caught. """
    if __name__ == '__main__':
        while True:
            # getting data from user
            date = get_date()
            currency = get_currency()
            try:
                # fetching results from external api based on date and currency
                # then mapper function maps json response to python array
                result = get_data(date, currency)
                rates = mapper(result)
                print(rates)
            except HttpRequestException as error:
                print(f"Http request error, Status: {error.status}, Reason: {error.message}")
                continue
            except InvalidJsonSchemaException():
                print("Searched key does not exist in the response, try again")
                continue


main()
