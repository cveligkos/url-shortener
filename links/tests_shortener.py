from django.test import TestCase
from .shortener import encode_int_to_base62


class ShortenerTestCase(TestCase):
    def test_convert_int_to_base62(self):
        self.assertEqual(encode_int_to_base62(1), "b")
        self.assertEqual(encode_int_to_base62(61), "9")
        self.assertEqual(encode_int_to_base62(62), "ba")
        self.assertEqual(encode_int_to_base62(123), "b9")
        self.assertEqual(encode_int_to_base62(124), "ca")
