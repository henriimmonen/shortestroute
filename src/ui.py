import time
from dijkstra import Dijkstra
from jps import JumpPointSearch
import apufunktiot


class Ui:
    def __init__(self):
        self.aloitus_solmu = None
        self.lopetus_solmu = None
        self.kartta = None

    def kysy_aloitus_lopetus(self):
        """Kysytään aloitus- ja lopetus-solmut"""
        self.kartta = apufunktiot.alusta_kartta('./test.map')
        print('\n')
        print('***Kartta***')
        for rivi in self.kartta:
            print(rivi)
        print('\n')

        aloitus_solmu_x = int(input(f'Anna aloitus-solmun rivi väliltä 0 - {len(self.kartta)-1}: '))
        aloitus_solmu_y = int(input(f'Anna aloitus-solmun sarake väliltä 0 - {len(self.kartta[0])-1}: '))

        while not self.tarkista_rivi_ja_sarake(aloitus_solmu_x, aloitus_solmu_y):
            aloitus_solmu_x = int(input(f'Anna aloitus-solmun rivi väliltä 0 - {len(self.kartta)-1}: '))
            aloitus_solmu_y = int(input(f'Anna aloitus-solmun sarake väliltä 0 - {len(self.kartta[0])-1}: '))

        self.aloitus_solmu = (aloitus_solmu_x, aloitus_solmu_y)

        lopetus_solmu_x = int(input(f'Anna lopetus-solmun rivi väliltä 0 - {len(self.kartta)-1}: '))
        lopetus_solmu_y = int(input(f'Anna lopetus-solmun sarake väliltä 0 - {len(self.kartta[0])-1}: '))

        while not self.tarkista_rivi_ja_sarake(lopetus_solmu_x, lopetus_solmu_y):
            lopetus_solmu_x = int(input(f'Anna lopetus-solmun rivi väliltä 0 - {len(self.kartta)-1}: '))
            lopetus_solmu_y = int(input(f'Anna lopetus-solmun sarake väliltä 0 - {len(self.kartta[0])-1}: '))

        self.lopetus_solmu = (lopetus_solmu_x, lopetus_solmu_y)

    def aloita(self):
        """" Ohjelman käyttöliittymä """
        verkko = apufunktiot.kaarilista(self.kartta)
        print('\n')
        print('Dijkstran algoritmin ja Jump Point Search-algoritmin vertailu\n')
        alkuaika_dijkstra = time.time()
        print('Dijkstran algoritmin tulos')
        print('*******************************')
        dijkstra = Dijkstra(self.aloitus_solmu, self.lopetus_solmu, verkko, self.kartta)
        etaisyys = dijkstra.etsi_reitti()
        reitti_dijkstra = dijkstra.tulosta_reitti(etaisyys)
        print(reitti_dijkstra)
        loppuaika_dijkstra = time.time()
        print('Algoritmi suoriutui ajassa: ', loppuaika_dijkstra-alkuaika_dijkstra, 'sekuntia')
        print('\n')
        print('Dijkstran reitti:')
        kuljettu_reitti = apufunktiot.piirra_kartalle(self.kartta, reitti_dijkstra)
        for i in kuljettu_reitti:
            print(i)
        print('\n')

        self.kartta = apufunktiot.alusta_kartta('./test.map')
        verkko = apufunktiot.kaarilista(self.kartta)
        alkuaika_jps = time.time()
        jps = JumpPointSearch(self.aloitus_solmu, self.lopetus_solmu, verkko, self.kartta)
        print('JPS-algoritmin tulos')
        print('*******************************')
        edeltavat = jps.hae_reitti()
        reitti_jps = jps.tulosta_reitti(edeltavat, self.lopetus_solmu)
        print(reitti_jps)
        loppuaika_jps = time.time()
        print('Algoritmi suoriutui ajassa: ', loppuaika_jps - alkuaika_jps, 'sekuntia')
        print('\n')
        print('JPS:n reitti:')
        lisattavat = []
        for i in range(len(reitti_jps)-1):
            if apufunktiot.puuttuu_solmuja(reitti_jps[i], reitti_jps[i+1]):
                lisattavat = lisattavat + apufunktiot.laske_puuttuvat_solmut(
                    reitti_jps[i], reitti_jps[i+1])
        reitti_jps = reitti_jps + lisattavat
        kuljettu_reitti = apufunktiot.piirra_kartalle(self.kartta, reitti_jps)
        for i in kuljettu_reitti:
            print(i)
        print('\n')

    def tarkista_rivi_ja_sarake(self, rivi, sarake):
        """Tarkistetaan annettujen solmujen kuuluminen kartan sisälle"""
        if rivi >= len(self.kartta) or rivi < 0:
            print('Rivinumeroa ei hyväksytty, anna välillä 0 -', len(self.kartta)-1)
            return False

        if sarake >= len(self.kartta[0]) or sarake < 0:
            print('Sarakenumeroa ei hyväksytty, anna välillä 0 -', len(self.kartta[0])-1)
            return False

        return True
