#Berkay Başyılmaz 20222905056
import unittest
from compp.AgeCheck import agecheck
class TestAgeCheck(unittest.TestCase):

    # Test for drivers younger than or equal to the young driver age
    def test_1(self):
        # Testing age = 20 and experience = 1
        # Expecting young driver premium multiplier * young driver experience multiplier
        self.assertEqual(agecheck(20, 1), 2 * 2,)

    # Test for drivers older than the young driver age but younger than the older driver age
    def test_2(self):
        # Testing age = 40 and experience = 3
        # Expecting young driver premium multiplier
        self.assertEqual(agecheck(40, 3), 2,)

    # Test for drivers older than the older driver age but younger than the elderly driver age
    def test_3(self):
        # Testing age = 75 and experience = 4
        # Expecting older driver premium multiplier
        self.assertEqual(agecheck(75, 4), 1.5,)

    # Test for drivers older than or equal to the elderly driver age
    def test_4(self):
        # Testing age = 85 and experience = 6
        # Expecting elderly driver premium multiplier
        self.assertEqual(agecheck(85, 6), 2,)

    # Test for all age and experience boundaries
    def test_5(self):
        # Testing age = 25 and experience = 2
        # Expecting young driver premium multiplier * young driver experience multiplier
        self.assertEqual(agecheck(25, 2), 2 * 2,)
        # Testing age = 70 and experience = 5
        # Expecting older driver premium multiplier
        self.assertEqual(agecheck(70, 5), 1.5,)
        # Testing age = 80 and experience = 5
        # Expecting elderly driver premium multiplier
        self.assertEqual(agecheck(80, 5), 2,)

if __name__ == '__main__':
     unittest.main()