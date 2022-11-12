from dijkstra import Dijkstra
from apufunktiot import Apufunktiot

def main():
    """" Ohjelman käyttöliittymä """
    apufunktiot = Apufunktiot()
    kartta = apufunktiot.alusta_kartta('./test.map')
    alku = (0, 0)
    loppu = (5, 13)
    verkko = apufunktiot.kaarilista(kartta)

    dijkstra = Dijkstra(alku, loppu, verkko, kartta)
    etaisyys = dijkstra.etsi_reitti()
    print(dijkstra.tulosta_reitti(etaisyys))

if __name__ == '__main__':
    main()
