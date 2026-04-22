from abc import ABC, abstractmethod

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
        if status == "Delivered":
            raise ValueError("Cannot change delivered package")
        self._status = new_status

    @abstractmethod
    def calculate_cost(self):
        pass
