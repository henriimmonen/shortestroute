import unittest
import math
import apufunktiot
from dijkstra import Dijkstra

class TestRoute(unittest.TestCase):
    def setUp(self):
        self.kartta = ['...', '.@@', '...']
        self.tyhja_kartta = ['.....', '.....', '.....', '.....', '.....']
        self.este_kartta = ['......', '@@@@..','......']
        self.apufunktiot = apufunktiot
        self.verkko = self.apufunktiot.kaarilista(self.kartta)
        self.dijkstra = Dijkstra((0, 0), (2, 2), self.verkko, self.kartta)

    def test_dijkstra_luo_verkon(self):
        self.assertTrue(self.dijkstra.verkko, self.verkko)

    def test_dijkstra_luo_kartan(self):
        self.assertTrue(self.dijkstra.kartta, self.kartta)

    def test_dijkstra_etsii_oikean_reitin(self):
        self.assertEqual(self.dijkstra.etsi_reitti(), [-1, 0, 1, 0, -1, -1, 3, 3, 7])

    def test_dijkstra_tulostaa_oikean_reitin(self):
        edellinen = self.dijkstra.etsi_reitti()
        self.assertEqual(self.dijkstra.tulosta_reitti(edellinen), [(0, 0), (1, 0), (2, 1), (2, 2)])

    def test_laske_etaisyys_toimii_oikein(self):
        etaisyys = self.dijkstra.laske_etaisyys((0, 1), (0, 2))
        self.assertEqual(etaisyys, 1)

    def test_laske_etaisyys_toimii_oikein_diagonaalisesti(self):
        etaisyys = self.dijkstra.laske_etaisyys((0, 1), (1, 2))
        self.assertEqual(etaisyys, math.sqrt(2))

    def test_maalissa_tunnistaa_maaliruudun(self):
        self.assertTrue(self.dijkstra.maalissa((2, 2)))

    def test_maalissa_tunnistaa_kun_ei_olla_maalissa(self):
        self.assertFalse(self.dijkstra.maalissa((1, 1)))

    def test_oikea_reitti_tyhjalla_kartalla(self):
        verkko_tyhja = self.apufunktiot.kaarilista(self.tyhja_kartta)
        dijkstra_tyhja = Dijkstra((0, 0), (4, 4), verkko_tyhja, self.tyhja_kartta)
        edellinen = dijkstra_tyhja.etsi_reitti()
        reitti = dijkstra_tyhja.tulosta_reitti(edellinen)
        self.assertEqual(reitti, [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)])

    def test_oikea_reitti_tyhjalla_kartalla_oikealta_vasemmalle(self):
        verkko_tyhja = self.apufunktiot.kaarilista(self.tyhja_kartta)
        dijkstra_tyhja = Dijkstra((0, 4), (4, 0), verkko_tyhja, self.tyhja_kartta)
        edellinen = dijkstra_tyhja.etsi_reitti()
        reitti = dijkstra_tyhja.tulosta_reitti(edellinen)
        self.assertEqual(reitti, [(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)])

    def test_estekartta_antaa_oikean_lopputuloksen(self):
        verkko_este = self.apufunktiot.kaarilista(self.este_kartta)
        dijkstra_este = Dijkstra((0, 0), (2, 0), verkko_este, self.este_kartta)
        edellinen = dijkstra_este.etsi_reitti()
        reitti = dijkstra_este.tulosta_reitti(edellinen)
        self.assertEqual(reitti, [(0, 0), (0, 1), (0, 2), (0, 3), (1, 4), (2, 3), (2, 2), (2, 1), (2, 0)])