from unittest import TestCase

from jalaali import Jalaali


class JalaaliTest(TestCase):
    def test_to_jalaali(self):
        self.assertEqual({'jy': 1367, 'jm': 11, 'jd': 8}, Jalaali.to_jalaali(1989, 1, 28))
        self.assertEqual({'jy': 1394, 'jm': 7, 'jd': 18}, Jalaali.to_jalaali(2015, 10, 10))
        self.assertEqual({'jy': 1395, 'jm': 7, 'jd': 15}, Jalaali.to_jalaali(2016, 10, 6))

    def test_to_gregorian(self):
        self.assertEqual({'gy': 1989, 'gm': 1, 'gd': 28}, Jalaali.to_gregorian(1367, 11, 8))
        self.assertEqual({'gy': 2015, 'gm': 10, 'gd': 10}, Jalaali.to_gregorian(1394, 7, 18))
        self.assertEqual({'gy': 2016, 'gm': 10, 'gd': 6}, Jalaali.to_gregorian(1395, 7, 15))

    def test_is_valid_jalaali_date(self):
        self.assertFalse(Jalaali.is_valid_jalaali_date(3178, 1, 1))
        self.assertTrue(Jalaali.is_valid_jalaali_date(-61, 1, 1))
        self.assertTrue(Jalaali.is_valid_jalaali_date(3177, 12, 29))

    def test_is_leap_jalaali_year(self):
        self.assertFalse(Jalaali.is_leap_jalaali_year(1393))
        self.assertFalse(Jalaali.is_leap_jalaali_year(1394))
        self.assertTrue(Jalaali.is_leap_jalaali_year(1395))
        self.assertFalse(Jalaali.is_leap_jalaali_year(1396))

    def test_jalaali_month_length(self):
        self.assertEqual(31, Jalaali.jalaali_month_length(1393, 1))
        self.assertEqual(31, Jalaali.jalaali_month_length(1393, 3))
        self.assertEqual(31, Jalaali.jalaali_month_length(1393, 6))
        self.assertEqual(30, Jalaali.jalaali_month_length(1393, 8))
        self.assertEqual(30, Jalaali.jalaali_month_length(1393, 10))
        self.assertEqual(29, Jalaali.jalaali_month_length(1393, 12))
        self.assertEqual(29, Jalaali.jalaali_month_length(1394, 12))
        self.assertEqual(30, Jalaali.jalaali_month_length(1395, 12))
