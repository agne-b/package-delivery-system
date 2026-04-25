import unittest
from standard_package import StandardPackage
from address import Address

class TestPackage(unittest.TestCase):

  def setup(self):
    self.sender = Address("Street 1", "City 1", "12345")
    self.receiver = Address("Street 2", "City 2", "56789")
    
  def test_valid_package_creation(self):
    package = StandardPackage("12345", 2.5, self.sender, self.receiver)
    self.assertEqual(package.package_id, "12345")
    self.assertEqual(package.weight, 2.5)
    self.assertEqual(package.get_status(), "Created")

def test_invalid_package_id_letters(self):
  with self.assertRaises(ValueError):
    StandardPackage("12A45", 2.5, self.sender, self.receiver)

def test_invalid_weight(self):
  with self.assertRaises(ValueError):
    StandardPackage("12345", -2.5, self.sender, self.receiver)
    
