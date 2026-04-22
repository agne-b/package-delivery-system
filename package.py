from abc import ABC, abstractmethod

class Package(ABC):
    def __init__(self, package_id, weight, sender, receiver):
        if not package_id:
            raise ValueError("Package ID cannot be empty")
        if weight <= 0:
            raise ValueError("Weight must be positive")
        if not sender:
            raise ValueError("Sender cannot be empty")
        if not receiver:
            raise ValueError("Receiver cannot be empty")
            
        self._package_id = package_id
        self._weight = weight
        self._sender = sender
        self._receiver = receiver
        self._status = "Created"

    @property
    def package_id(self):
        return self._package_id

    def get_status(self):
        return self._status
    
    def update_status(self, new_status):
        if self._status == "Delivered":
            raise ValueError("Cannot change delivered package")

        allowed_statuses = ["Created", "Assigned to courier", "Delivered"]

        if new_status not in allowed_statuses:
            raise ValueError("Invalid status update")
                             
        self._status = new_status

    @abstractmethod
    def calculate_cost(self):
        pass
