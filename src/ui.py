import time
import os
from dijkstra import Dijkstra
from jps import JumpPointSearch
import apufunktiot


class Ui:
    def __init__(self):
        self.aloitus_solmu = None
        self.lopetus_solmu = None
        self.kartta = None
        self.kartan_nimi = None
        self.kartta_liian_suuri = False

    def kysy_aloitus_lopetus(self):
        """Kysytään aloitus- ja lopetus-solmut"""
        self.kartan_nimi = input('Anna karttatiedoston nimi: ')

        try:
            self.kartta = apufunktiot.alusta_kartta(f'./{self.kartan_nimi}')
        except FileNotFoundError:
            print('Karttaa ei löytynyt, syötä nimi uudelleen!')
            self.kysy_aloitus_lopetus()

        self.kirjoita_tiedostoon('sydney', self.kartta)
        self.tarkista_kartan_koko()

        if self.kartta_liian_suuri is True:
            self.avaa_kartta(self.kartan_nimi)
        else:
            print('\n')
            print('***Kartta***')
            for rivi in self.kartta:
                print(rivi)
            print('\n')

        aloitus_solmu_x = int(input(
            f'Anna aloitus-solmun rivi väliltä 0 - {len(self.kartta)-1}: '
            ))
        aloitus_solmu_y = int(input(
            f'Anna aloitus-solmun sarake väliltä 0 - {len(self.kartta[0])-1}: '
            ))

        while not self.tarkista_rivi_ja_sarake(aloitus_solmu_x, aloitus_solmu_y):
            aloitus_solmu_x = int(input(
                f'Anna aloitus-solmun rivi väliltä 0 - {len(self.kartta)-1}: '
                ))
            aloitus_solmu_y = int(input(
                f'Anna aloitus-solmun sarake väliltä 0 - {len(self.kartta[0])-1}: '
                ))

        self.aloitus_solmu = (aloitus_solmu_x, aloitus_solmu_y)

        lopetus_solmu_x = int(input(
            f'Anna lopetus-solmun rivi väliltä 0 - {len(self.kartta)-1}: '
            ))
        lopetus_solmu_y = int(input(
            f'Anna lopetus-solmun sarake väliltä 0 - {len(self.kartta[0])-1}: '
            ))

        while not self.tarkista_rivi_ja_sarake(lopetus_solmu_x, lopetus_solmu_y):
            lopetus_solmu_x = int(input(
                f'Anna lopetus-solmun rivi väliltä 0 - {len(self.kartta)-1}: '
                ))
            lopetus_solmu_y = int(input(
                f'Anna lopetus-solmun sarake väliltä 0 - {len(self.kartta[0])-1}: '
                ))

        self.lopetus_solmu = (lopetus_solmu_x, lopetus_solmu_y)

    def aloita(self):
        """" Ohjelman käyttöliittymä """
        self.aja_dijkstra()
        self.aja_jps()

    def aja_dijkstra(self):
        """Dijkstran algoritmin suoritus"""
        alkuaika_dijkstra = time.time()
        print('\n')
        print('Dijkstran algoritmin ja Jump Point Search-algoritmin vertailu\n')
        verkko = apufunktiot.kaarilista(self.kartta)
        print('Dijkstran algoritmin tulos')
        print('*******************************')
        dijkstra = Dijkstra(self.aloitus_solmu, self.lopetus_solmu, verkko, self.kartta)
        edellinen = dijkstra.etsi_reitti()
        reitti_dijkstra = dijkstra.tulosta_reitti(edellinen)
        loppuaika_dijkstra = time.time()
        print('Algoritmi suoriutui ajassa: ', round(
            loppuaika_dijkstra-alkuaika_dijkstra, 3), 'sekuntia')
        print('Algoritmi kävi', len(dijkstra.kasitellyt), 'solmussa')
        print('Kuljettu matka:', round(dijkstra.etaisyys[
            self.lopetus_solmu[0]*len(self.kartta[0])+self.lopetus_solmu[1]
            ], 5))
        print('\n')
        kuljettu_reitti = apufunktiot.piirra_kartalle(self.kartta, reitti_dijkstra)
        self.nayta_reitti_dijkstra(kuljettu_reitti)

    def aja_jps(self):
        """Jump Point Search-algoritmin suoritus"""
        self.kartta = apufunktiot.alusta_kartta(f'./{self.kartan_nimi}')
        alkuaika_jps = time.time()
        verkko = apufunktiot.kaarilista(self.kartta)
        jps = JumpPointSearch(self.aloitus_solmu, self.lopetus_solmu, verkko, self.kartta)
        print('JPS-algoritmin tulos')
        print('*******************************')
        edeltavat = jps.hae_reitti()
        reitti_jps = jps.tulosta_reitti(edeltavat, self.lopetus_solmu)
        loppuaika_jps = time.time()
        print('Algoritmi suoriutui ajassa: ', round(loppuaika_jps - alkuaika_jps, 3), 'sekuntia')
        print('Algoritmi kävi', len(jps.kasitellyt), 'solmussa')
        print('Kuljettu matka:', round(jps.etaisyys_solmuun.get(self.lopetus_solmu), 5))
        print('\n')
        self.nayta_reitti_jps(reitti_jps)

    def nayta_reitti_dijkstra(self, kuljettu_reitti):
        """Piirretään Dijkstran reitti joko terminaaliin tai tiedostoon"""
        if self.kartta_liian_suuri is True:
            self.kirjoita_tiedostoon('dijkstra', kuljettu_reitti)
            self.avaa_kartta('dijkstra.txt')
        else:
            print('Dijkstran reitti:')
            for i in kuljettu_reitti:
                print(i)
            print('\n')

    def nayta_reitti_jps(self, reitti_jps):
        """Piirretään reitti joko terminaaliin tai tiedostoon"""
        lisattavat = []
        for i in range(len(reitti_jps)-1):
            if apufunktiot.puuttuu_solmuja(reitti_jps[i], reitti_jps[i+1]):
                lisattavat = lisattavat + apufunktiot.laske_puuttuvat_solmut(
                    reitti_jps[i], reitti_jps[i+1])
        reitti_jps = reitti_jps + lisattavat
        kuljettu_reitti = apufunktiot.piirra_kartalle(self.kartta, reitti_jps)
        if self.kartta_liian_suuri is True:
            self.kirjoita_tiedostoon('jps', kuljettu_reitti)
            self.avaa_kartta('jps.txt')
        else:
            print('JPS:n reitti:')
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

        if self.kartta[rivi][sarake] == '@':
            print('Valittu solmu on seinäsolmu, valitse jokin toinen solmu')
            return False
        return True

    def tarkista_kartan_koko(self): # pylint: disable=useless-return
        """Tarkistetaan voidaanko kartta näyttää komentorivillä"""
        if len(self.kartta[0]) > 30:
            self.kartta_liian_suuri = True
        return

    def avaa_kartta(self, kartta):
        """Avataan kartta tekstieditorissa"""
        os.system(f'gio open ./{kartta}')

    def kirjoita_tiedostoon(self, algoritmi, kartta):
        """Kirjoitetaan kartta tekstitiedostoksi näyttämistä varten"""
        with open(f'{algoritmi}.txt', 'w', encoding='utf-8') as kirjoittaja:
            for rivi in kartta:
                kirjoittaja.write(rivi)
                kirjoittaja.write('\n')
            kirjoittaja.close()
