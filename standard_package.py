from package import Package

class StandardPackage(Package):
    def __init__(self, package_id, weight, sender, receiver):
        super().__init__(package_id, weight, sender, receiver)
        self.base_rate = 2.0

    def calculate_cost(self):
        return self.base_rate * self._weight

    def get_type(self):
        return "Standard"
