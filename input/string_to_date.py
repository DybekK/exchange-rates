from datetime import datetime

from exception.InvalidDateFormatException import InvalidDateFormatException


def string_to_date(date_string: str) -> datetime:
    """
     Validates if the given value has correct date format and returns datetime object.

     Args:
          date_string (str): Date in string format.

      Raises:
          InvalidDateFormatException

     Returns:
          Datetime object based on user input.
     """
    date_format = "%Y-%m-%d"
    try:
        return datetime.strptime(date_string, date_format)
    except ValueError:
        raise InvalidDateFormatException()
