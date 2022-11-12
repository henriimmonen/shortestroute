import unittest
from apumetodit import Apumetodit
from dijkstra import Dijkstra

class TestRoute(unittest.TestCase):
    def setUp(self):
        self.a = Apumetodit()
        self.kartta = ['...','.@@','...']
        self.verkko = [[(0,1), (1,0)], [(0,0), (0,2)], [(0,1)], [(0,0), (2,0)], [],
                        [], [(1,0), (2,1)], [(2,0), (2,2)], [(2,1)]]
        self.d = Dijkstra((0,0), (4,4), self.verkko, self.kartta)
    
    def test_kartan_alustaminen(self):
        alustettu_kartta = self.a.alusta_kartta('./test.map')
        self.assertEqual(alustettu_kartta[0][0], '.')

    def test_kaarilistan_muodostaminen(self):
        verkko = self.a.kaarilista(self.kartta)
        self.assertEqual(verkko[0], [(0,1), (1,0)])

    def test_solmu_ei_ole_verkon_sisalla(self):
        solmu = (6,6)
        self.assertFalse(self.a._verkon_sisalla(solmu, self.kartta))

    def test_solmu_on_verkon_sisalla(self):
        solmu = (0,2)
        self.assertTrue(self.a._verkon_sisalla(solmu, self.kartta))

    def test_solmun_naapuuriin_ei_voi_kulkea(self):
        self.assertFalse(self.a._solmun_naapuriin_voi_kulkea((1,1), self.kartta))

    def test_solmun_naapuriin_voi_kulkea(self):
        self.assertTrue(self.a._solmun_naapuriin_voi_kulkea((1,0), self.kartta))

    def test_dijkstra_luo_verkon(self):
        self.assertTrue(self.d.verkko, self.verkko)

    def test_dijkstra_luo_kartan(self):
        self.assertTrue(self.d.kartta, self.kartta)

    def test_dijkstra_etsii_oikean_reitin(self):
        self.assertEqual(self.d.etsi_reitti(), [-1, 0, 1, 0, -1, -1, 3, 6, 7])

