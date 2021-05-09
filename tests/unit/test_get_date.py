from datetime import datetime
from unittest import TestCase
from unittest.mock import patch

from input.get_date import get_date


class Test(TestCase):
    date_format = "%Y-%m-%d"

    def test_should_return_datetime_object(self):
        given = "2021-03-03"
        with patch('builtins.input', return_value=given):
            expect = datetime.strptime(given, self.date_format)
            result = get_date()
            self.assertEqual(expect, result)

    def test_should_be_called_twice_if_format_is_invalid(self):
        given = "2021-03-53"
        with patch('builtins.input', return_value=given, wraps=input) as wrapped_input:
            expect = 2
            get_date(2)
            self.assertEqual(expect, wrapped_input.call_count)
