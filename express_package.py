from package import Package

class ExpressPackage(Package):
    def __init__(self, package_id, weight, sender, receiver, base_rate=2.0, express_fee=10.0):
        super().__init__(package_id, weight, sender, receiver)
        if base_rate <= 0:
            raise ValueError("Base rate must be positive")
        if express_fee <= 0:
            raise ValueError("Express fee must be positive")
            
        self._base_rate = base_rate
        self._express_fee = express_fee

    def calculate_cost(self):
        return round(self._base_rate * self._weight + self._express_fee, 2)

    def get_type(self):
        return "Express"
