import datetime
from unittest import TestCase
from unittest.mock import patch, MagicMock, PropertyMock

from exception.HttpRequestException import HttpRequestException
from http_client.get_data import get_data


class Test(TestCase):
    date_format = "%Y-%m-%d"

    @patch("http.client.HTTPConnection")
    @patch("http.client.HTTPResponse")
    def test_should_return_valid_data(self, mock_conn, mock_res):
        mock_res.status = 200
        mock_conn.getresponse = MagicMock.return_value = mock_res

        with patch('json.loads', new_callable=PropertyMock) as mock_loads:
            given = {"test_data": "test"}
            mock_loads.return_value = given
            result = get_data(datetime.datetime.strptime("2021-03-03", self.date_format), "usd")
            self.assertIsInstance(result, dict)
            self.assertEquals(given, result)

    @patch("http.client.HTTPConnection")
    @patch("http.client.HTTPResponse")
    def test_should_throw_exception_when_status_is_4xx(self, mock_conn, mock_res):
        mock_res.status = 400
        mock_conn.getresponse = MagicMock.return_value = mock_res

        result = lambda: get_data(datetime.datetime.strptime("2021-03-03", self.date_format), "usd")
        self.assertRaises(HttpRequestException, result)

    @patch("http.client.HTTPConnection")
    @patch("http.client.HTTPResponse")
    def test_should_throw_exception_when_status_is_4xx(self, mock_conn, mock_res):
        mock_res.status = 500
        mock_conn.getresponse = MagicMock.return_value = mock_res

        result = lambda: get_data(datetime.datetime.strptime("2021-03-03", self.date_format), "usd")
        self.assertRaises(HttpRequestException, result)
