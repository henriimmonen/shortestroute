from dijkstra import Dijkstra
from apumetodit import Apumetodit

def main():
    a = Apumetodit()
    kartta = a.alusta_kartta('./test.map')
    alku = (0,0)
    loppu = (5,13)
    verkko = a.kaarilista(kartta)

    d = Dijkstra(alku, loppu, verkko, kartta)
    etaisyys = d.etsi_reitti()
    print(d.tulosta_reitti(etaisyys))

if __name__ == '__main__':
    main()