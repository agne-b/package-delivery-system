import unittest
from package_factory import PackageFactory
from address import Address

class TestPackageFactory(unittest.TestCase):
  def setup(self):
    self.sender = Address("Street 1", "City", "12345")
    self.receiver = Address("Street 2", "City", "56789")

def test_create_standard(self):
  package = PackageFactory.create_package("Standard", "44444", 1.0, self.sender, self.receiver)
  self.assertEqual(package.get_type(), "Standard")

def test_create_express(self):
  package = PackageFactory.create_package("Express", "55555", 1.0, self.sender, self.receiver)
  self.assertEqual(package.get_type(), "Express")

def test_invalid_type(self):
   with self.assertRaises(ValueError):
     PackageFactory.create_package("Fast", "66666", 1.0, self.sender, self.receiver)
