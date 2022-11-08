from dijkstra import Dijkstra
import time

class Main():

    def kartan_alustaminen(self):
            f = open('./test.map', 'r')
            kartta = []
            for x in f:
                if x[0] == '.':
                    kartta.append(x[0:-1])
            f.close()
            self.kartta = kartta

    def kaarilista(self):
        self.verkko = [] # Luodaan verkko
        for i in range(len(self.kartta)):
            for j in range(len(self.kartta[i])):
                self.tarkista_naapurit((i,j))

    def tarkista_naapurit(self, solmu):
        solmun_naapurit = [] # Jokaisella solmulla on lista naapureista
        for naapuri in [(solmu[0]-1,solmu[1]-1), (solmu[0]-1, solmu[1]), (solmu[0]-1,solmu[1]+1),
                            (solmu[0],solmu[1]-1),(solmu[0],solmu[1]+1),(solmu[0]+1,solmu[1]-1),
                            (solmu[0]+1,solmu[1]),(solmu[0]+1,solmu[1]+1)]:
            if self._verkon_sisalla(naapuri):
                #print('Solmu on verkon sisällä', naapuri)
                if self._solmun_naapuriin_voi_kulkea(naapuri):
                    #print('Solmun tarkistus')
                    solmun_naapurit.append(naapuri)
        self.verkko.append(solmun_naapurit)

    def _verkon_sisalla(self, solmu):
        if solmu[0] >= 0 and solmu[0] < len(self.kartta):
            if solmu[1] >= 0 and solmu[1] < len(self.kartta[0]):
                return True
        return False

    def _solmun_naapuriin_voi_kulkea(self, naapuri):
        if self.kartta[naapuri[0]][naapuri[1]] == '.':
            return True
        return False

    def main(self):
        self.kartan_alustaminen()
        alku = (0,0)
        loppu = (-1,-1)
        alku = time.time()
        self.kaarilista()
        print('Aikaa kului: ', time.time()- alku, 'sekuntia')
        print('Kaarilista tehty!')
        print(self.verkko)
        #print(self.verkko[(0,0)])
        #d = Dijkstra(alku, loppu, alustettu_kartta)
        #d.etsi_reitti()


if __name__ == '__main__':
    m = Main()
    m.main()