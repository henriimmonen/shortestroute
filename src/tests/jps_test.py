import unittest
import math
from jps import JumpPointSearch

class TestRoute(unittest.TestCase):
    def setUp(self):
        self.kartta = ['...', '.@@', '...']
        self.verkko = [[(0, 1), (1, 0)], [(0, 0), (0, 2)], [(0, 1)], [(0, 0), (2, 0), (2, 1)], [],
                       [], [(1, 0), (2, 1)], [(2, 0), (2, 2)], [(2, 1)]]
        self.jps = JumpPointSearch((0, 0), (2, 2), self.verkko, self.kartta)
        
    def test_euklidinen_etaisyys(self):
        self.assertEqual(self.jps.euklidinen_etaisyys((0, 0), (2, 2)), 2*math.sqrt(2))

    def test_maalissa_funktio(self):
        self.assertTrue(self.jps.maalissa((2, 2)))

    def test_jps_hakee_oikean_reitin(self):
        edeltavat = self.jps.hae_reitti()
        self.assertEqual(edeltavat.get((2, 2)), (2, 1))

    def test_etsittaessa_horisontaalisesti_tunnistetaan_kun_ollaan_maalissa(self):
        self.assertTrue(self.jps.etsi_horisontaalisesti((2, 1), 0, 1))

    def test_reitin_tulostus(self):
        edeltavat = self.jps.hae_reitti()
        self.assertEqual(self.jps.tulosta_reitti(edeltavat, (2, 2)), [(0, 0), (1, 0), (2, 1), (2, 2)])