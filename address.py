class Address:
    def __init__(self, street, city, postal_code):
        self.street = street
        self.city = city
        self.postal_code = postal_code

    def get_full_address(self):
        return f"{self.street}, {self.city}, {self.postal_code}"
