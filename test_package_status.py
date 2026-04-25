import unittest
from address import Address

class TestPackageStatus(unittest.TestCase):
  def create_sender_receiver_package(self):
    sender = Address("Street 1", "City", "12345")
    receiver = Address("Street 2", "City", "56789")
    self.package = StandardPackage("11111", 1.0, sender, receiver)

def test_valid_status_change(self):
  self.package.update_status("Assigned to courier")
  self.assertEqual(self.package.get_status(), "Assigned to courier")

def test_invalid_status(self):
  with self.assertRaises(ValueError):
    self.package.update_status("Flying")

def test_cannot_change_after_delivered(self):
  self.package.update_status("Delivered")
  with self.assertRaises(ValueError):
    self.package.update_status("Created")
