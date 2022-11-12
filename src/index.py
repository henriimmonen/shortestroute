from dijkstra import Dijkstra
import apufunktiot

def main():
    """" Ohjelman käyttöliittymä """
    kartta = apufunktiot.alusta_kartta('./test.map')
    alku = (0, 0)
    loppu = (5, 13)
    verkko = apufunktiot.kaarilista(kartta)

    dijkstra = Dijkstra(alku, loppu, verkko, kartta)
    etaisyys = dijkstra.etsi_reitti()
    print(dijkstra.tulosta_reitti(etaisyys))

if __name__ == '__main__':
    main()
