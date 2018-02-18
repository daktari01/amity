import unittest

from src.rooms import Room, Office, LivingSpace

class TestRooms(unittest.TestCase):
    """
    Class to test the rooms module
    """
    def setUp(self):
        """Method to initialize variables"""
        self.room = Room('Test_room', 2, 4)
        self.living = LivingSpace('Test_living')
        self.office = Office('Test_office')

    def test_livingspace_inherits_room(self):
        """Test whether class LivingSpace is a sub class of class Room"""
        self.assertTrue(issubclass(LivingSpace, Room))

    def test_office_inherits_room(self):
        """Test whether class Office is a sub class of class Room"""
        self.assertTrue(issubclass(Office, Room))

    def test_room_instance(self):
        """Test whether room is an instance of class Room"""
        self.assertIsInstance(self.room, Room)

    def test_living_instance(self):
        """Test whether living is an instance of class LivingSpace"""
        self.assertIsInstance(self.living, LivingSpace)

    def test_office_instance(self):
        """Test whether office is an instance of class Office"""
        self.assertIsInstance(self.office, Office)

    def test_is_full(self):
        """Test the is_full method functions correctly"""
        not_full = Room('Not Full', 3, 6)
        full = Room('Test_Full', 4, 4)
        self.assertFalse(not_full.is_full(3, 6))
        self.assertTrue(full.is_full(4, 4))


if __name__ == '__main__':
    unittest.main(exit=False) 