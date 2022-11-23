import unittest
import apufunktiot

class TestRoute(unittest.TestCase):
    def setUp(self):
        self.apufunktiot = apufunktiot
        self.kartta = ['...', '.@@', '...']
        self.verkko = [[(0, 1), (1, 0)], [(0, 0), (0, 2)], [(0, 1)], [(0, 0), (2, 0)], [],
                       [], [(1, 0), (2, 1)], [(2, 0), (2, 2)], [(2, 1)]]

    def test_kartan_alustaminen(self):
        alustettu_kartta = self.apufunktiot.alusta_kartta('./test.map')
        self.assertEqual(alustettu_kartta[0][0], '.')

    def test_kaarilistan_muodostaminen(self):
        verkko = self.apufunktiot.kaarilista(self.kartta)
        self.assertEqual(verkko[0], [(0, 1), (1, 0)])

    def test_solmu_ei_ole_verkon_sisalla(self):
        solmu = (6, 6)
        self.assertFalse(self.apufunktiot.verkon_sisalla(solmu, self.kartta))

    def test_solmu_on_verkon_sisalla(self):
        solmu = (0, 2)
        self.assertTrue(self.apufunktiot.verkon_sisalla(solmu, self.kartta))

    def test_solmun_naapuuriin_ei_voi_kulkea(self):
        self.assertFalse(self.apufunktiot.solmun_naapuriin_voi_kulkea((1, 1), self.kartta))

    def test_solmun_naapuriin_voi_kulkea(self):
        self.assertTrue(self.apufunktiot.solmun_naapuriin_voi_kulkea((1, 0), self.kartta))
