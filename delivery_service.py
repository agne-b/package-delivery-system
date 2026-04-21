from standard_package import StandardPackage
from express_package import ExpressPackage
from courier import Courier
from data_manager import DataManager

class DeliveryService:
    def __init__(self):
        self._packages = []
        self._couriers = []
        self.packages = DataManager.load_packages()

    def save_state(self):
    DataManager.save_packages(self.packages)

    def add_courier(self, courier):
        self._couriers.append(courier)

    def create_standard_package(self, package_id, weight, sender, receiver):
        package = StandardPackage(package_id, weight, sender, receiver)
        self._packages.append(package)
        return package

    def create_express_package(self, package_id, weight, sender, receiver):
        package = ExpressPackage(package_id, weight, sender, receiver)
        self._packages.append(package)
        return package

    def assign_package_to_courier(self, package, courier):
        courier.assign_package(package)

    def calculate_total_shipping_cost(self):
        total = 0
        for p in self._packages:
            total += p.calculate_cost()
        return total

    def list_all_packages(self):
        for p in self._packages:
            print(f"Package {p._package_id}, Status: {p.get_status()}, Type: {p.get_type()}")
