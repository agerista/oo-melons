"""This file should have our order classes in it."""
from random import randint
from datetime import datetime
import time

class AbstractMelonOrder(object):
    """Calculates cost of melon orders."""

    def __init__(self, species, qty, country_code=None):
        """Initializes melon order attributes"""

        self.species = species
        self.qty = qty
        self.country_code = country_code
        self.shipped = False

    def get_base_price(self):
        """Adds Splurge pricing"""

        splurge_price = randint(5, 9)
        weekday = False
        rush_hour = False

        order_time = datetime.now()
        if order_time.weekday != 5 or order_time.weekday != 6:
            weekday = True

        if order_time.hour >= 8 and order_time.hour <= 12:
            rush_hour = True

        if weekday is True and rush_hour is True:
            splurge_price = splurge_price + 4

        return splurge_price

    def get_total(self):
        """Calculate price."""

        base_price = self.get_base_price()

        if self.country_code is not None and self.qty < 10:
            base_price = base_price + 3.0

        if self.species == "christmas melon":
            base_price = base_price * 1.5      

        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""
        super(DomesticMelonOrder, self).__init__(species, qty)
        self.order_type = "domestic"
        self.tax = 0.08

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""
        
        super(InternationalMelonOrder, self).__init__(species, qty, country_code)

        self.order_type = "international"
        self.tax = 0.17

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    """Government Melon Orders"""

    def __init__(self, species, qty):
        """Initizalize government melon order attributes"""
        super(GovernmentMelonOrder, self).__init__(species, qty)

        self.order_type = "government"
        self.tax = 0
        self.passed_inspection = False

    def mark_inspection(self):
        """Checks to see if melon passed inspection"""

        self.passed_inspection = True
