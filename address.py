class Address:
    def __init__(self, street, city, postal_code):
        if not street:
            raise ValueError("Street cannot be empty")
        if not city:
            raise ValueError("City cannot be empty")
        if not postal_code:
            raise ValueError("Postal code cannot be empty")

        postal_code = str(postal_code).strip()
        
        if not postal_code.isdigit():
            raise ValueError("Postal code must only contain numbers")
        if len(postal_code) != 5:
            raise ValueError("Postal code must contain exactly 5 digits")
        self._street = street
        self._city = city
        self._postal_code = postal_code

    @property
    def street(self):
        return self._street

    @property
    def city(self):
        return self._city

    @property
    def postal_code(self):
        return self._postal_code

    def get_full_address(self):
        return f"{self.street}, {self.city}, {self.postal_code}"
