from abc import ABC, abstractmethod
from address import Address

class Package(ABC):

    allowed_statuses = ["Created", "Assigned to courier", "Delivered"] 
    
    def __init__(self, package_id, weight, sender, receiver):
        if not package_id:
            raise ValueError("Package ID cannot be empty")
        if not isinstance(package_id, str):
            raise ValueError("Package ID must be a string")
        if len(package_id) != 5:
            raise ValueError("Package ID must be exactly 5 digits")
        if not package_id.isdigit():
            raise ValueError("Package ID must contain only digits")
        if not isinstance(weight, (int, float)):
            raise ValueError("Weight must be a number") 
        if weight <= 0:
            raise ValueError("Weight must be positive")
        if not isinstance(sender, Address):
            raise ValueError("Sender must be an Address object")
        if not isinstance(receiver, Address):
            raise ValueError("Receiver must be an Address object")
            
        self._package_id = package_id
        self._weight = weight
        self._sender = sender
        self._receiver = receiver
        self._status = "Created"

    @property
    def package_id(self):
        return self._package_id

    @property
    def weight(self):
        return self._weight

    @property
    def sender(self):
        return self._sender

    @property
    def receiver(self):
        return self._receiver

    def get_status(self):
        return self._status
    
    def update_status(self, new_status):
        if self._status == "Delivered":
            raise ValueError("Cannot change delivered package")

        if new_status not in self.allowed_statuses:
            raise ValueError("Invalid status update")
                             
        self._status = new_status

    @abstractmethod
    def calculate_cost(self):
        pass
