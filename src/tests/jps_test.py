import unittest
import math
import apufunktiot
from jps import JumpPointSearch

class TestRoute(unittest.TestCase):
    def setUp(self):
        self.kartta = ['...', '.@@', '...']
        self.verkko = [[(0, 1), (1, 0)], [(0, 0), (0, 2)], [(0, 1)], [(0, 0), (2, 0)], [],
                       [], [(1, 0), (2, 1)], [(2, 0), (2, 2)], [(2, 1)]]
        self.jps = JumpPointSearch((0, 0), (2, 2), self.verkko, self.kartta)
        
    def test_euklidinen_etaisyys(self):
        self.assertEqual(self.jps.euklidinen_etaisyys((0, 0), (2, 2)), 2*math.sqrt(2))