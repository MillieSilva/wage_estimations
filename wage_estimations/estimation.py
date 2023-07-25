# Standard Imports
import typing
import textwrap

# Local Imports

# External Imports


class Estimation:

    @property
    def currency_kind(self):
        return self.currency_kind

    @currency_kind.setter
    def currency_kind(self, kind):
        raise NotImplementedError

    @property
    def per_hour(self) -> float:
        return self.amount_per_second * 60

    @property
    def per_day(self) -> float:
        return self.per_hour * 8

    @property
    def per_week(self) -> float:
        return self.per_day * 7

    @property
    def per_week_no_weekend(self) -> float:
        return self.per_day * 5

    @property
    def per_month(self) -> float:
        return self.per_week * 4

    @property
    def per_half_year(self) -> float:
        return self.per_month * 6

    @property
    def per_year(self) -> float:
        return self.per_half_year * 2

    @classmethod
    def with_per_hours(cls, monetary_amount: float, hours: int) -> typing.Self:
        per_second = monetary_amount / hours / 60
        return Estimation(per_second)

    @classmethod
    def with_per_days(cls, monetary_amount: float, days: int) -> typing.Self:
        per_second = monetary_amount / days / 8 / 60
        return Estimation(per_second)

    @classmethod
    def with_per_weeks(cls, monetary_amount: float, weeks: int) -> typing.Self:
        per_second = monetary_amount / weeks / 7 / 8 / 60
        return Estimation(per_second)

    @classmethod
    def with_per_months(cls, monetary_amount: float, months: int) -> typing.Self:
        per_second = monetary_amount / months / 4 / 7 / 8 / 60
        return Estimation(per_second)

    @classmethod
    def with_per_years(cls, monetary_amount: float, years: int) -> typing.Self:
        per_second = monetary_amount / (years * 12) / 4 / 7 / 8 / 60
        return Estimation(per_second)

    def __init__(self, amount_per_second: float):
        """Makes estimations on value per time based on given monetary amount"""
        self.amount_per_second = amount_per_second
        self.__currency_kind = "€"

    def to_value_in_time(self, time: int) -> str:
        ...

    def __repr__(self):
        return textwrap.dedent(f"""\
          {self.amount_per_second}{self.__currency_kind}/per second
          {self.per_hour}{self.__currency_kind}/per hour
          {self.per_day}{self.__currency_kind}/per day
          {self.per_week}{self.__currency_kind}/per week
          {self.per_week_no_weekend}{self.__currency_kind}/per week (without weekend)
          {self.per_month}{self.__currency_kind}/per month
          {self.per_half_year}{self.__currency_kind}/per 6 months
          {self.per_year}{self.__currency_kind}/per year
        """)

