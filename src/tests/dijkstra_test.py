import unittest
import math
from dijkstra import Dijkstra

class TestRoute(unittest.TestCase):
    def setUp(self):
        self.kartta = ['...', '.@@', '...']
        self.verkko = [[(0, 1), (1, 0)], [(0, 0), (0, 2)], [(0, 1)], [(0, 0), (2, 0)], [],
                       [], [(1, 0), (2, 1)], [(2, 0), (2, 2)], [(2, 1)]]
        self.dijkstra = Dijkstra((0, 0), (2, 2), self.verkko, self.kartta)

    def test_dijkstra_luo_verkon(self):
        self.assertTrue(self.dijkstra.verkko, self.verkko)

    def test_dijkstra_luo_kartan(self):
        self.assertTrue(self.dijkstra.kartta, self.kartta)

    def test_dijkstra_etsii_oikean_reitin(self):
        self.assertEqual(self.dijkstra.etsi_reitti(), [-1, 0, 1, 0, -1, -1, 3, 6, 7])

    def test_dijkstra_tulostaa_oikean_reitin(self):
        etaisyys = self.dijkstra.etsi_reitti()
        self.assertEqual(self.dijkstra.tulosta_reitti(etaisyys), [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)])

    def test_laske_etaisyys_toimii_oikein(self):
        etaisyys = self.dijkstra.laske_etaisyys((0, 1), (0, 2))
        self.assertEqual(etaisyys, 1)

    def test_laske_etaisyys_toimii_oikein_diagonaalisesti(self):
        etaisyys = self.dijkstra.laske_etaisyys((0, 1), (1, 2))
        self.assertEqual(etaisyys, math.sqrt(2))

    def test_euklidinen_etaisyys_toimii_oikein(self):
        self.assertEqual(self.dijkstra.euklidinen_etaisyys((0, 0), (2, 2)), 2*math.sqrt(2))

    def test_maalissa_tunnistaa_maaliruudun(self):
        self.assertTrue(self.dijkstra.maalissa((2, 2)))

    def test_maalissa_tunnistaa_kun_ei_olla_maalissa(self):
        self.assertFalse(self.dijkstra.maalissa((1, 1)))