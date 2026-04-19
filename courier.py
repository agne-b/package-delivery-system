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
