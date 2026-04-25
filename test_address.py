import unittest 
from address import Address

class TestAddress(unittest.TestCase):
  def test_valid_address(self):
    addr = Address("Street", "City", "12345")
    self.assertEqual(addr.street, "Street")
    self.assertEqual(addr.city, "City")
    self.assertEqual(addr.postal_code, "12345")

  def test_invalid_postal_code_letters(self):
    with self.assertRaises(ValueError):
      Address("Street", "City", "12A45")

  def test_invalid_postal_code_length(self):
    with self.assertRaises(ValueError):
      Address("Street", "City", "1234")

  def test_empty_street(self):
    with self.assertRaises(ValueError):
        Address("", "City", "12345")

  def test_empty_city(self):
    with self.assertRaises(ValueError):
        Address("Street", "", "12345")

if __name__ == "__main__": 
  unittest.main()
