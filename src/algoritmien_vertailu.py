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
            print('Kuljettu matka ei ole yht?? pitk??!')
            break

    loppuaika = time.time() - alkuaika
    print(f'Kuljetut matkat ovat yht?? pitki??. Aikaa kului {loppuaika} sekuntia.')

def algoritmien_aikavertailu():
    """Vertaillaan Dijkstran ja JPS-algoritmin suorituskyky??"""

    kartta = apufunktiot.alusta_kartta('./sydney.map')
    print('\n')
    aloitus_solmu = (0, 0)
    lopetus_solmu = (255, 255)
    aika_dijkstra, aika_jps = aikavertailun_suoritus(
        aloitus_solmu, lopetus_solmu, kartta)
    vieraillut_dijkstra, vieraillut_jps = aikavaativuuden_vertailu(
        aloitus_solmu, lopetus_solmu, kartta)
    print('Dijkstran keskiarvo vasemmasta yl??kulmasta oikeaan alakulmaan',
    aika_dijkstra)
    print('Vieraillut solmut:', vieraillut_dijkstra)
    print('Jps:n keskiarvo vasemmasta yl??kulmasta oikeaan alakulmaan',
    aika_jps)
    print('Vieraillut solmut:', vieraillut_jps)
    print('\n')

    aloitus_solmu = (0, 0)
    lopetus_solmu = (0, 255)
    aika_dijkstra, aika_jps = aikavertailun_suoritus(
        aloitus_solmu, lopetus_solmu, kartta)
    vieraillut_dijkstra, vieraillut_jps = aikavaativuuden_vertailu(
        aloitus_solmu, lopetus_solmu, kartta)
    print('Dijkstran keskiarvo vasemmasta yl??kulmasta oikeaan yl??kulmaan',
    aika_dijkstra)
    print('Vieraillut solmut:', vieraillut_dijkstra)
    print('Jps:n keskiarvo vasemmasta yl??kulmasta oikeaan yl??kulmaan',
    aika_jps)
    print('Vieraillut solmut:', vieraillut_jps)
    print('\n')

    aloitus_solmu = (0, 0)
    lopetus_solmu = (140, 255)
    aika_dijkstra, aika_jps = aikavertailun_suoritus(
        aloitus_solmu, lopetus_solmu, kartta)
    vieraillut_dijkstra, vieraillut_jps = aikavaativuuden_vertailu(
        aloitus_solmu, lopetus_solmu, kartta)
    print('Dijkstran keskiarvo vasemmasta yl??kulmasta oikeaan puoliv??liin',
    aika_dijkstra)
    print('Vieraillut solmut:', vieraillut_dijkstra)
    print('Jps:n keskiarvo vasemmasta yl??kulmasta oikeaan puoliv??liin',
    aika_jps)
    print('Vieraillut solmut:', vieraillut_jps)
    print('\n')

    aloitus_solmu = (0, 0)
    lopetus_solmu = (14, 50)
    aika_dijkstra, aika_jps = aikavertailun_suoritus(
        aloitus_solmu, lopetus_solmu, kartta)
    vieraillut_dijkstra, vieraillut_jps = aikavaativuuden_vertailu(
        aloitus_solmu, lopetus_solmu, kartta)
    print('Dijkstran keskiarvo lyhyell?? matkalla', aika_dijkstra)
    print('Vieraillut solmut:', vieraillut_dijkstra)
    print('Jps:n keskiarvo lyhyell?? matkalla', aika_jps)
    print('Vieraillut solmut:', vieraillut_jps)


def aikavertailun_suoritus(aloitus_solmu, lopetus_solmu, kartta):
    """Funktio, jossa mitataan ajan keskiarvo 100 matkalle annettujen solmujen v??lill??
    sek?? palautetaan ajon aikana vierailtujen solmujen keskiarvo"""

    aloitus_aika_dijkstra = time.time()
    for ajo in range(100): # pylint: disable=unused-variable
        verkko = apufunktiot.kaarilista(kartta)
        dijkstra = Dijkstra(aloitus_solmu, lopetus_solmu, verkko, kartta)
        dijkstra.etsi_reitti()
    aika_dijkstra = (time.time() - aloitus_aika_dijkstra)/100

    aloitus_aika_jps = time.time()
    for ajo in range(100):
        verkko = apufunktiot.kaarilista(kartta)
        jps = JumpPointSearch(aloitus_solmu, lopetus_solmu, verkko, kartta)
        jps.hae_reitti()
    aika_jps = (time.time() - aloitus_aika_jps)/100

    return aika_dijkstra, aika_jps

def aikavaativuuden_vertailu(aloitus_solmu, lopetus_solmu, kartta):
    """Verrataan algoritmien vierailtujen solmujen m????r????"""
    vieraillut_solmut_dijkstra = 0
    for ajo in range(10): # pylint: disable=unused-variable
        verkko = apufunktiot.kaarilista(kartta)
        dijkstra = Dijkstra(aloitus_solmu, lopetus_solmu, verkko, kartta)
        dijkstra.etsi_reitti()
        vieraillut_solmut_dijkstra += len(dijkstra.kasitellyt)
    vieraillut_solmut_dijkstra = vieraillut_solmut_dijkstra/10

    vieraillut_solmut_jps = 0
    for ajo in range(10):
        verkko = apufunktiot.kaarilista(kartta)
        jps = JumpPointSearch(aloitus_solmu, lopetus_solmu, verkko, kartta)
        jps.hae_reitti()
        vieraillut_solmut_jps += len(jps.kasitellyt)
    vieraillut_solmut_jps = vieraillut_solmut_jps/10

    return vieraillut_solmut_dijkstra, vieraillut_solmut_jps

if __name__ == '__main__':
    main()
