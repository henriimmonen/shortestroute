import time
from dijkstra import Dijkstra
from jps import JumpPointSearch
import apufunktiot

def main():
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
    #kuljettu_reitti = apufunktiot.piirra_kartalle(kartta, reitti_dijkstra)
    #for i in kuljettu_reitti:
    #    print(i)
    print('\n')

    alkuaika_jps = time.time()
    jps = JumpPointSearch(alku, loppu, verkko, kartta)
    print('JPS-algoritmin tulos')
    print('*******************************')
    edeltavat = jps.hae_reitti()
    print(jps.tulosta_reitti(edeltavat, loppu))
    loppuaika_jps = time.time()
    print('Algoritmi suoriutui ajassa: ', loppuaika_jps - alkuaika_jps)
    print('\n')

if __name__ == '__main__':
    main()
