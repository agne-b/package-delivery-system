import unittest 
from address import address

class TestAddress(unittest.TestCase):
  def test_valid_address(self):
    address=Address("Antakalnio g. 75", "Vilnius", "10214")
    self.assertEqual(address.street, "Antakalnio g. 75")
    self.assertEqual(address.city, "Vilnius")
    self.assertEqual(address.postal_code, "10214")

  def test_invalid_postal_code_letters(self):
    with self.assertRaises(ValueError):
      Address("Antakalnio g.", "Vilnius", "12A45")

def test_invalid_postal_code_length(self):
  with self.assertRaises(ValueError):
    Adress("Antakalnio g.", "Vilnius", "1234")
