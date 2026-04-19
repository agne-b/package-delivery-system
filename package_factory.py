from standard_package import StandardPackage
from express_package import ExpressPackage

class PackageFactory:
    @staticmethod
    def create_package(package_type, package_id, weight, sender, receiver):
        if package_type == "Standard":
            return StandardPackage(package_id, weight, sender, receiver)
        elif package_type == "Express":
            return ExpressPackage(package_id, weight, sender, receiver)
        else:
            raise ValueError("Unknown package type")
