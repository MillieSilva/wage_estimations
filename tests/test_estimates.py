# Standard Imports
import unittest

# Local Imports
from wage_estimations.estimation import Estimation

# External Imports


class HourTestCase(unittest.TestCase):
    def test_hours(self):
        self.assertEquals(Estimation.with_per_hours(10, 1).per_hour, 10)
        self.assertEquals(Estimation.with_per_hours(10, 2).per_hour, 5)
        self.assertNotEquals(Estimation.with_per_hours(10, 3).per_hour, 5)

    def test_days(self):
        self.assertEquals(Estimation.with_per_days(80, 1).per_day, 80)
        self.assertEquals(Estimation.with_per_days(80, 2).per_day, 40)
        self.assertNotEquals(Estimation.with_per_days(80, 3).per_day, 40)

    def test_weeks(self):
        self.assertEquals(Estimation.with_per_weeks(560, 1).per_week, 560)
        self.assertEquals(Estimation.with_per_weeks(560, 2).per_week, 280)
        self.assertNotEquals(Estimation.with_per_weeks(560, 3).per_week, 280)

    def test_months(self):
        self.assertEquals(Estimation.with_per_months(2240, 1).per_month, 2240)
        self.assertEquals(Estimation.with_per_months(2240, 2).per_month, 1120)
        self.assertNotEquals(Estimation.with_per_months(2240, 3).per_month, 1120)

    def test_half_year(self):
        self.assertEquals(Estimation.with_per_months(2240, 1).per_half_year, 13440)
        self.assertEquals(Estimation.with_per_months(2240, 2).per_half_year, 6720)
        self.assertNotEquals(Estimation.with_per_months(2240, 3).per_half_year, 6720)

    def test_years(self):
        self.assertEquals(Estimation.with_per_years(26880, 1).per_year, 26880)
        self.assertEquals(Estimation.with_per_years(26880, 2).per_year, 13440)
        self.assertNotEquals(Estimation.with_per_years(26880, 3).per_year, 13440)


