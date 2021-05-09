from datetime import datetime

from exception.InvalidDateFormatException import InvalidDateFormatException
from input.string_to_date import string_to_date


def get_date() -> datetime:
    """Gets value from user about date"""
    while True:
        try:
            date_value = input("Enter date:")
            return string_to_date(date_value)
        except InvalidDateFormatException:
            print("This is the incorrect date string format. It should be YYYY-MM-DD")
            continue
