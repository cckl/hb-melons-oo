"""Classes for melon orders."""
class AbstractMelonOrder():

    def __init__(self, species, qty, country_code=None):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False

        if country_code:
            self.country_code = country_code


    def get_total(self):
        """Calculate price, including tax."""
        base_price = 5

        if self.species == "Christmas melon":
            base_price *= 1.5
        
        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True



class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    order_type = "domestic"
    tax = 0.08



class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    order_type = "international"
    tax = 0.17
    # qty = 0

    def get_total(self):
        initial_total = super().get_total()

        if self.qty < 10:
            return initial_total + 3
        else: 
            return initial_total

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
