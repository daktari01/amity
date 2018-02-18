import unittest

from src.people import Person, Staff, Fellow

class TestPeople(unittest.TestCase):
    """
    Class to test the people module
    """
    def setUp(self):
        """Method to initialize variables"""
        self.person = Person('Test Person')
        self.fellow = Fellow('Test Fellow')
        self.staff = Staff('Test Staff')

    def test_fellow_inherits_person(self):
        """Test whether class Fellow is a sub class of class Person"""
        self.assertTrue(issubclass(Fellow, Person))

    def test_staff_inherits_person(self):
        """Test whether class Staff is a sub class of class Person"""
        self.assertTrue(issubclass(Staff, Person))

    def test_person_instance(self):
        """Test whether person is an instance of class Person"""
        self.assertIsInstance(self.person, Person)

    def test_staff_instance(self):
        """Test whether staff is an instance of class Staff"""
        self.assertIsInstance(self.staff, Staff)

    def test_fellow_instance(self):
        """Test whether fellow is an instance of class Fellow"""
        self.assertIsInstance(self.fellow, Fellow)

if __name__ == '__main__':
    unittest.main(exit=False) 
