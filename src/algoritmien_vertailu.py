import time
from dijkstra import Dijkstra
from jps import JumpPointSearch
import apufunktiot

def main():
    algoritmien_reitin_pituusvertailu()

def algoritmien_reitin_pituusvertailu():
    alku = time.time()
    kartta = apufunktiot.alusta_kartta('./sydney.map')
    aloitus_solmu = (0, 0)
    lopetus_solmu = (255, 255)

    for ajo in range(101):
        if ajo == 10:
            aloitus_solmu = (255, 255)
            lopetus_solmu = (0, 0)

        if ajo == 20:
            aloitus_solmu = (0, 0)
            lopetus_solmu = (0, 255)

        if ajo == 30:
            aloitus_solmu = (0, 255)
            lopetus_solmu = (0, 0)

        if ajo == 40:
            aloitus_solmu = (0, 0)
            lopetus_solmu = (140, 255)

        if ajo == 50:
            aloitus_solmu = (140, 255)
            lopetus_solmu = (0, 0)

        if ajo == 60:
            aloitus_solmu = (140, 255)
            lopetus_solmu = (255, 0)

        if ajo == 70:
            aloitus_solmu = (255, 0)
            lopetus_solmu = (140, 255)

        if ajo == 80:
            aloitus_solmu = (255, 0)
            lopetus_solmu = (255, 255)

        if ajo == 90:
            aloitus_solmu = (255, 255)
            lopetus_solmu = (255, 0)

        verkko = apufunktiot.kaarilista(kartta)
        dijkstra = Dijkstra(aloitus_solmu, lopetus_solmu, verkko, kartta)
        dijkstra.etsi_reitti()
        kuljettu_matka_dijkstra = round(dijkstra.etaisyys[
            lopetus_solmu[0]*len(kartta[0])+lopetus_solmu[1]
            ], 5)

        jps = JumpPointSearch(aloitus_solmu, lopetus_solmu, verkko, kartta)
        jps.hae_reitti()
        kuljettu_matka_jps = round(jps.etaisyys_solmuun.get(lopetus_solmu), 5)

        if kuljettu_matka_dijkstra != kuljettu_matka_jps:
            print(ajo, kuljettu_matka_dijkstra, kuljettu_matka_jps)
            print('Kuljettu matka ei ole yhtä pitkä!')
            break
        print(ajo, aloitus_solmu, lopetus_solmu)
    loppuaika = time.time()
    print(loppuaika-alku, 's')
    print('Kuljetut matkat vastaavat molemmilla algoritmeilla toisiaan')

if __name__ == '__main__':
    main()
