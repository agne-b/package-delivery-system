import csv
from package_factory import PackageFactory
from address import Address


class DataManager:
    FILE_NAME = "packages.csv"

    @staticmethod
    def save_packages(packages):
        file = open(DataManager.FILE_NAME, "w", newline="")
        writer = csv.writer(file)

        writer.writerow(["id", "type", "weight", "sender", "receiver", "status"])

        for p in packages:
            writer.writerow([
                p.package_id,
                p.get_type(),
                p._weight,
                p._sender,
                p._receiver,
                p.get_status()
            ])

        file.close()

    @staticmethod
    def load_packages():
        packages = []

        try:
            file = open(DataManager.FILE_NAME, "r")
            reader = csv.reader(file)

            next(reader)

            for row in reader:
                package_id = row[0]
                package_type = row[1]
                weight = float(row[2])
                sender = row[3]
                receiver = row[4]
                status = row[5]

                package = PackageFactory.create_package(
                    package_type,
                    package_id,
                    weight,
                    sender,
                    receiver
                )

                package.update_status(status)
                packages.append(package)

            file.close()

        except FileNotFoundError:
            return []

        return packages
