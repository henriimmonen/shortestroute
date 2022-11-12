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

    path = []
    edeltava = loppu[0]*len(kartta[0])+loppu[1]
    path.append(edeltava)

    while etaisyys[edeltava] != -1:
        path.append(etaisyys[edeltava])
        edeltava = etaisyys[edeltava]

    print("Polku ruudusta:", alku, 'ruutuun', loppu, ': ')
    for i in range(len(path)-1, -1, -1):
        print((path[i]//len(kartta[0]), path[i]%len(kartta[0])))

if __name__ == '__main__':
    main()