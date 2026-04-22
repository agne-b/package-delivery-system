from package import Package

class StandardPackage(Package):
    def __init__(self, package_id, weight, sender, receiver, base_rate=2.0):
        super().__init__(package_id, weight, sender, receiver)
        if base_rate <= 0:
            raise ValueError("Base rate must be positive")
        self._base_rate = base_rate

    def calculate_cost(self):
        return round(self._base_rate * self._weight, 2)

    def get_type(self):
        return "Standard"
