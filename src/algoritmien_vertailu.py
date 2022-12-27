import time
from dijkstra import Dijkstra
from jps import JumpPointSearch
import apufunktiot

def main():
    """Ohjelman tarkoitus on vertailla
    Dijkstran ja Jps-algoritmin toimintaa"""

    algoritmien_reitin_pituusvertailu()
    algoritmien_aikavertailu()

def algoritmien_reitin_pituusvertailu():
    """Metodi algoritmien tuottamien reittien pituusvertailuun"""

    alkuaika = time.time()
    kartta = apufunktiot.alusta_kartta('./sydney.map')
    aloitus_solmu = (0, 0)
    lopetus_solmu = (255, 255)

    for ajo in range(100):
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

    loppuaika = time.time() - alkuaika
    print(f'Kuljetut matkat ovat yhtä pitkiä. Aikaa kului {loppuaika} sekuntia.')

def algoritmien_aikavertailu():
    """Vertaillaan Dijkstran ja JPS-algoritmin suorituskykyä"""

    kartta = apufunktiot.alusta_kartta('./sydney.map')
    aloitus_solmu = (0, 0)
    lopetus_solmu = (255, 255)
    aika_dijkstra, aika_jps, vieraillut_dijkstra, vieraillut_jps = aikavertailun_suoritus(
        aloitus_solmu, lopetus_solmu, kartta)
    print('Dijkstran keskiarvo vasemmasta yläkulmasta oikeaan alakulmaan',
    aika_dijkstra)
    print('Vieraillut solmut:', vieraillut_dijkstra)
    print('Jps:n keskiarvo vasemmasta yläkulmasta oikeaan alakulmaan',
    aika_jps)
    print('Vieraillut solmut:', vieraillut_jps)

    aloitus_solmu = (0, 0)
    lopetus_solmu = (0, 255)
    aika_dijkstra, aika_jps, vieraillut_dijkstra, vieraillut_jps = aikavertailun_suoritus(
        aloitus_solmu, lopetus_solmu, kartta)
    print('Dijkstran keskiarvo vasemmasta yläkulmasta oikeaan yläkulmaan',
    aika_dijkstra)
    print('Vieraillut solmut:', vieraillut_dijkstra)
    print('Jps:n keskiarvo vasemmasta yläkulmasta oikeaan yläkulmaan',
    aika_jps)
    print('Vieraillut solmut:', vieraillut_jps)

    aloitus_solmu = (0, 0)
    lopetus_solmu = (140, 255)
    aika_dijkstra, aika_jps, vieraillut_dijkstra, vieraillut_jps = aikavertailun_suoritus(
        aloitus_solmu, lopetus_solmu, kartta)
    print('Dijkstran keskiarvo vasemmasta yläkulmasta oikeaan puoliväliin',
    aika_dijkstra)
    print('Vieraillut solmut:', vieraillut_dijkstra)
    print('Jps:n keskiarvo vasemmasta yläkulmasta oikeaan puoliväliin',
    aika_jps)
    print('Vieraillut solmut:', vieraillut_jps)

    aloitus_solmu = (0, 0)
    lopetus_solmu = (14, 50)
    aika_dijkstra, aika_jps, vieraillut_dijkstra, vieraillut_jps = aikavertailun_suoritus(
        aloitus_solmu, lopetus_solmu, kartta)
    print('Dijkstran keskiarvo lyhyellä matkalla', aika_dijkstra)
    print('Vieraillut solmut:', vieraillut_dijkstra)
    print('Jps:n keskiarvo lyhyellä matkalla', aika_jps)
    print('Vieraillut solmut:', vieraillut_jps)


def aikavertailun_suoritus(aloitus_solmu, lopetus_solmu, kartta):
    """Moduuli, jossa mitataan ajan keskiarvo 100 matkalle annettujen solmujen välillä
    sekä palautetaan ajon aikana vierailtujen solmujen keskiarvo"""
    vieraillut_solmut_dijkstra = 0
    aloitus_aika_dijkstra = time.time()
    for ajo in range(100): # pylint: disable=unused-variable
        verkko = apufunktiot.kaarilista(kartta)
        dijkstra = Dijkstra(aloitus_solmu, lopetus_solmu, verkko, kartta)
        dijkstra.etsi_reitti()
        vieraillut_solmut_dijkstra += len(dijkstra.kasitellyt)
    aika_dijkstra = (time.time() - aloitus_aika_dijkstra)/100
    vieraillut_solmut_dijkstra = vieraillut_solmut_dijkstra/100

    vieraillut_solmut_jps = 0
    aloitus_aika_jps = time.time()
    for ajo in range(100):
        verkko = apufunktiot.kaarilista(kartta)
        jps = JumpPointSearch(aloitus_solmu, lopetus_solmu, verkko, kartta)
        jps.hae_reitti()
        vieraillut_solmut_jps += jps.etaisyys_solmuun.get(lopetus_solmu)
    aika_jps = (time.time() - aloitus_aika_jps)/100
    vieraillut_solmut_jps = vieraillut_solmut_jps/100

    return aika_dijkstra, aika_jps, vieraillut_solmut_dijkstra, vieraillut_solmut_jps

if __name__ == '__main__':
    main()
