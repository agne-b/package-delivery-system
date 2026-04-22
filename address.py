class Address:
    def __init__(self, street, city, postal_code):
        if not street:
            raise ValueError("Street cannot be empty")
        if not city:
            raise ValueError("City cannot be empty")
        if not postal_code:
            raise ValueError("Postal code cannot be empty")
        self.street = street
        self.city = city
        self.postal_code = postal_code

    def get_full_address(self):
        return f"{self.street}, {self.city}, {self.postal_code}"
