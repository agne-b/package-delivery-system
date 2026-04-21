import csv
from package_factory import PackageFactory
from address import Address

class DataManager:
  FILE_NAME = "packages.csv"

  @staticmethod
  def save_packages(packages):
    with open(DataManager.FILE_NAME, mode="w", newline="") as file:
      writer = csv.writer(file)

      
      
