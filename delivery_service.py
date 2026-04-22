from standard_package import StandardPackage
from express_package import ExpressPackage
from courier import Courier
from data_manager import DataManager

class DeliveryService:
    def __init__(self):
        self._couriers = []
        self._packages = DataManager.load_packages()

    def save_state(self):
        DataManager.save_packages(self._packages)

    def add_courier(self, courier):
        if courier in self._couriers:
            raise ValueError("This courier already exists")
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
        if courier not in self._couriers:
            raise ValueError("Courier not registered in the system")
        courier.assign_package(package)

    def calculate_total_shipping_cost(self):
       return sum(p.calculate_cost() for p in self._packages)

    def list_all_packages(self):
        for p in self._packages:
            print(f"Package {p.package_id}, Status: {p.get_status()}, Type: {p.get_type()}")
