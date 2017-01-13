"""This file should have our order classes in it."""


class AbstractMelonOrder(object):
    """Calculates cost of melon orders."""

    def __init__(self, species, qty, country_code=None):
        """Initializes melon order attributes"""

        self.species = species
        self.qty = qty
        self.country_code = country_code
        self.shipped = False

    def get_total(self):
        """Calculate price."""

        base_price = 5
        if self.species == "christmas melon":
            base_price = base_price * 1.5
            total = (1 + self.tax) * self.qty * base_price

        elif self.country_code is not None and self.qty < 10:
            base_price = base_price + 3.0
            total = (1 + self.tax) * self.qty * base_price
        
        else:
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
