from abc import ABC, abstractmethod
import json

class Address:
    def __init__(self, street, city, postal_code):
        self.street = street
        self.city = city
        self.postal_code = postal_code

    def get_full_address(self):
        return f"{self.street}, {self.city}, {self.postal_code}"
    
class Package(ABC):
    def __init__(self, package_id, weight, sender, receiver):
        self._package_id = package_id
        self._weight = weight
        self._sender = sender
        self._receiver = receiver
        self._status = "Created"

    def get_status(self):
        return self._status
    
    def update_status(self, new_status):
        self._status = new_status

    @abstractmethod
    def calculate_cost(self):
        pass

class StandardPackage(Package):
    def __init__(self, package_id, weight, sender, receiver):
    super().__init__(package_id, weight, sender, receiver)
    self.base_rate = 2.0

    def calculate_cost(self):
        return self.base_rate * self._weight

    def get_type(self):
        return "Standard"

class ExpressPackage(Package):
    def __init__(self, package_id, weight, sender, receiver):
    super().__init__(package_id, weight, sender, receiver)
    self.base_rate = 2.0
    self.express_fee = 10.0

    def calculate_cost(self):
      return self.base_rate * self._weight + self.express_fee

    def get_type(self):
        return "Express"

class PackageFactory:'
    @staticmethod
    def create_package(package_type, package_id, weight, sender, receiver)
        if package_type == "Standard":
            return StandardPackage(package_id, weight, sender, receiver)
        elif package_type == "Express":
            return ExpressPackage(package_id, weight, sender, receiver)
        else:
            raise ValueError("Unknown package type")
      
class Courier:
    def __init__(self, name, vehicle_capacity):
        self._name = name
        self._vehicle_capacity = vehicle_capacity
        self._assigned_packages = []
    def assign_package(self, package):
        self._assigned_packages.append(package)
        package.update_status("Assigned to courier")
    def deliver_package(self, package):
        if package in self._assigned_packages:
            package.update_status("Delivered")
            self._assigned_packages.remove(package)
    def get_assigned_packages(self):
        return self._assigned_packages

class DeliveryService:
    def __init__ (self):
        self._packages = []
        self._couriers = []

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
            total += package.calculate_cost()
        return total
    def list_all_packages(self):
        for p in self._packages
            print (f"Package {p._package_id}, Status: {p.get_status()}, Type: {p.get_type()}")

    
        
  
  
