import unittest

from src.rooms import Office, LivingSpace
from src.people import Staff, Fellow

class TestAmity(unittest.TestCase):
    """Test the Amity class"""
    def setUp(self):
        office1 = Office("office", "office1")
        living1 = LivingSpace("living", "living1")
        
    # def test_create_duplicate_room(self):
    #     office2 = Office("office", "office1")
    #     assertEqual(office2, "Error message")