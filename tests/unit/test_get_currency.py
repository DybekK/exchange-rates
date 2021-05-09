from unittest import TestCase
from unittest.mock import patch

from input.get_currency import get_currency


class Test(TestCase):
    def test_should_return_currency_code_if_lowercase(self):
        given = "usd"
        with patch('builtins.input', return_value=given):
            expect = "USD"
            result = get_currency()
            self.assertEqual(expect, result)

    def test_should_return_currency_code_if_uppercase(self):
        given = "USD"
        with patch('builtins.input', return_value=given):
            expect = "USD"
            result = get_currency()
            self.assertEqual(expect, result)

    def test_should_be_called_twice_if_currency_is_invalid(self):
        given = "invalid currency"
        with patch('builtins.input', return_value=given, wraps=input) as wrapped_input:
            expect = 2
            get_currency(2)
            self.assertEqual(expect, wrapped_input.call_count)
