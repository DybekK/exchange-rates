from unittest import TestCase

from exception.InvalidJsonSchemaException import InvalidJsonSchemaException
from http_client.mapper import mapper


class Test(TestCase):
    def test_should_map_dict(self):
        given = {
            'rates': [{'no': '042/A/NBP/2021', 'effectiveDate': '2021-03-03', 'mid': 3.7509}]
        }
        expect = ['Stawka: 3.7509, Data: 2021-03-03']
        result = mapper(given)
        self.assertEqual(expect, result)

    def test_should_throw_exception_if_dict_is_invalid(self):
        given = {"ratess": []}
        self.assertRaises(InvalidJsonSchemaException, mapper, given)

        given = {"rates": [{}]}
        self.assertRaises(InvalidJsonSchemaException, mapper, given)
