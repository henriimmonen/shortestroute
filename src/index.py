import time
from dijkstra import Dijkstra
from jps import JumpPointSearch
import apufunktiot

def main(): # pylint: disable=too-many-locals
    """" Ohjelman käyttöliittymä """
    kartta = apufunktiot.alusta_kartta('./test.map')
    alku = (0, 0)
    loppu = (5, 6)
    verkko = apufunktiot.kaarilista(kartta)
    print('\n')
    print('Dijkstran algoritmin ja Jump Point Search-algoritmin vertailu\n')
    alkuaika_dijkstra = time.time()
    print('Dijkstran algoritmin tulos')
    print('*******************************')
    dijkstra = Dijkstra(alku, loppu, verkko, kartta)
    etaisyys = dijkstra.etsi_reitti()
    reitti_dijkstra = dijkstra.tulosta_reitti(etaisyys)
    print(reitti_dijkstra)
    loppuaika_dijkstra = time.time()
    print('Algoritmi suoriutui ajassa: ', loppuaika_dijkstra-alkuaika_dijkstra)
    print('\n')
    print('Dijkstran reitti:')
    kuljettu_reitti = apufunktiot.piirra_kartalle(kartta, reitti_dijkstra)
    for i in kuljettu_reitti:
        print(i)
    print('\n')

    kartta = apufunktiot.alusta_kartta('./test.map')
    verkko = apufunktiot.kaarilista(kartta)
    alkuaika_jps = time.time()
    jps = JumpPointSearch(alku, loppu, verkko, kartta)
    print('JPS-algoritmin tulos')
    print('*******************************')
    edeltavat = jps.hae_reitti()
    reitti_jps = jps.tulosta_reitti(edeltavat, loppu)
    print(reitti_jps)
    loppuaika_jps = time.time()
    print('Algoritmi suoriutui ajassa: ', loppuaika_jps - alkuaika_jps)
    print('\n')
    print('JPS:n reitti:')
    for i in range(len(reitti_jps)-1):
        if apufunktiot.puuttuu_solmuja(reitti_jps[i], reitti_jps[i+1]):
            reitti_jps.insert(i, apufunktiot.laske_puuttuvat_solmut(reitti_jps[i], reitti_jps[i+1]))
    kuljettu_reitti = apufunktiot.piirra_kartalle(kartta, reitti_jps)
    for i in kuljettu_reitti:
        print(i)
    print('\n')

if __name__ == '__main__':
    main()
