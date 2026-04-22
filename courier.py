class Courier:
    def __init__(self, name, vehicle_capacity):
        if not name:
            raise ValueError("Courier name cannot be empty")
        if vehicle_capacity<=0:
            raise ValueError("Vehicle capacity must be positive")
        self._name = name
        self._vehicle_capacity = vehicle_capacity
        self._assigned_packages = []

    def _current_load(self):
        return sum(package._weight for package in self._assigned_packages)

    def assign_package(self, package):
        if package in self._assigned_packages:
            raise ValueError("This package is already assigned to this courier")
        if self._current_load() + package._weight > self._vehicle_capacity:
            raise ValueError("Package exceeds courier vehicle capacity")
        self._assigned_packages.append(package)
        package.update_status("Assigned to courier")

    def deliver_package(self, package):
        if package not in self._assigned_packages:
            raise ValueError("This package not assigned to this courier")
            
        package.update_status("Delivered")
        self._assigned_packages.remove(package)

    def get_assigned_packages(self):
        return list(self._assigned_packages)  
