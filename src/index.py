import time
from dijkstra import Dijkstra
from jps import JumpPointSearch
import apufunktiot

def main():
    """" Ohjelman käyttöliittymä """
    kartta = apufunktiot.alusta_kartta('./test.map')
    alku = (0, 0)
    loppu = (5, 13)
    verkko = apufunktiot.kaarilista(kartta)
    print('\n')
    print('Dijkstran algoritmin ja Jump Point Search-algoritmin vertailu\n')

    alkuaika_dijkstra = time.time()
    print('Dijkstran algoritmin tulos')
    print('*******************************')
    dijkstra = Dijkstra(alku, loppu, verkko, kartta)
    etaisyys = dijkstra.etsi_reitti()
    print(dijkstra.tulosta_reitti(etaisyys))
    loppuaika_dijkstra = time.time()
    print('Algoritmi suoriutui ajassa: ', loppuaika_dijkstra-alkuaika_dijkstra)
    print('\n')

    alkuaika_jps = time.time()
    jps = JumpPointSearch(alku, loppu, verkko, kartta)
    print('JPS-algoritmin tulos')
    print('*******************************')
    jps.hae_reitti()
    loppuaika_jps = time.time()
    print('Algoritmi suoriutui ajassa: ', loppuaika_jps - alkuaika_jps)
    print('\n')

if __name__ == '__main__':
    main()
