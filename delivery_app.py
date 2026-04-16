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

class ExpressPackage(Package):
  def __init__(self, package_id, weight, sender, receiver):
    super().__init__(package_id, weight, sender, receiver)
    self.base_rate = 2.0
    self.express_fee = 10.0

  def calculate_cost(self):
  return self.base_rate * self._weight + self.express_fee

class Courier:
  
  
