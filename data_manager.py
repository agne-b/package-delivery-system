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
                p.weight,
                p.sender.get_full_address(),
                p.receiver.get_full_address(),
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

                sender_parts = row[3].split(",")
                receiver_parts = row[4].split(",")

                sender = Address(
                    sender_parts[0].strip(),
                    sender_parts[1].strip(),
                    sender_parts[2].strip()
                )

                receiver = Address(
                    receiver_parts[0].strip(),
                    receiver_parts[1].strip(),
                    receiver_parts[2].strip()
                )
                package = PackageFactory.create_package(
                    package_type,
                    package_id,
                    weight,
                    sender,
                    receiver
                )

                package.update_status(row[5])
                packages.append(package)

            file.close()

        except FileNotFoundError:
            return []

        return packages
