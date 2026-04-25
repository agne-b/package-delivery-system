import unittest
from courier import Courier
from address import Address
from standard_package import StandardPackage

class TestCourier(unittest.TestCase):
  def setup(self):
    sender = Address("Street 1", "City", "12345")
    receiver = Address("Street 2", "City", "56789")
    self.package = StandardPackage("22222", 2.0, sender, receiver)
    self.courier = Courier("John", 10)

def test_assign_package(self):
  self.courier.assign_package(self.package)
  self.assertEqual(self.package.get_status(), "Assigned to courier")

def test_exceed_capacity(self):
  heavy_package = StandardPackage("33333", 50, self.package.sender, self.package.receiver)
  with self.assertRaises(ValueError):
    self.courier.assign_package(heavy_package)

def test_deliver_package(self):
  self.courier.assign_package(self.package)
  self.courier.deliver_package(self.package)
  self.assertEqual(self.package.get_status(), "Delivered")
  
