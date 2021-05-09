from datetime import datetime

from exception.InvalidDateFormatException import InvalidDateFormatException
from input.string_to_date import string_to_date


def get_date(test_loop_count=None) -> datetime:
    """Gets value from user about date"""
    loop_count = 0
    while True:
        try:
            date_value = input("Enter date:")
            return string_to_date(date_value)
        except InvalidDateFormatException:
            loop_count += 1
            if test_loop_count == loop_count:
                break
            print("This is the incorrect date string format. It should be YYYY-MM-DD")
            continue
