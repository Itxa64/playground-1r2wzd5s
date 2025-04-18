import unittest
from universe import stars_in_galaxy

class TestStarsInGalaxy(unittest.TestCase):
    def test_stars_in_galaxy(self):
        self.assertEqual(stars_in_galaxy("Milky Way"), 100000000000)
        self.assertEqual(stars_in_galaxy("Andromeda"), 100000000000)

if __name__ == "__main__":
    unittest.main()
