import heapq, math
import apufunktiot

class JumpPointSearch():
    def __init__(self, aloitus_solmu, lopetus_solmu, verkko, kartta):
        self.aloitus_solmu = aloitus_solmu
        self.lopetus_solmu = lopetus_solmu
        self.verkko = verkko
        self.kartta = kartta
        self.keko = []
        self.kasitellyt = ({})
        inf = 10**9
        self.etaisyys = [inf for i in range(len(self.kartta[0])*len(self.kartta))]
        self.edeltava = [-1 for i in range(len(self.kartta[0])*len(self.kartta))]

    def hae_reitti(self):
        heapq.heappush((0, self.aloitus_solmu))
        #self.etaisyys[self.alku[0]*len(self.kartta[0])+self.alku[1]] = 0
        while len(self.keko) != 0:
            kasiteltava_solmu = heapq.heappop(self.keko)
            self.etsi_hyppypiste(kasiteltava_solmu)

    def etsi_hyppypiste(self, kasiteltava_solmu):
        if kasiteltava_solmu in self.kasitellyt:
            return
        self.kasitellyt.add(kasiteltava_solmu)

        self.etsi_vertikaalisesti(kasiteltava_solmu)
        self.etsi_horisontaalisesti(kasiteltava_solmu)
        self.etsi_diagonaalisesti(kasiteltava_solmu)

    def etsi_vertikaalisesti(self, kasiteltava_solmu):
        for suunta in (0, 1), (0, -1):
            kasiteltava_solmu = (kasiteltava_solmu[0], (kasiteltava_solmu[1][0], kasiteltava_solmu[1][1] + suunta[1]))

            if not apufunktiot.verkon_sisalla(kasiteltava_solmu, self.kartta):
                if not apufunktiot.solmun_naapuriin_voi_kulkea(kasiteltava_solmu[1], self.kartta):
                    return

            if kasiteltava_solmu[1][0] == self.lopetus_solmu[0] and kasiteltava_solmu[1][1] == self.lopetus_solmu[1]:
                heapq.heappush(self.keko, (kasiteltava_solmu[0] + 1, kasiteltava_solmu[1]))
            #tarkista pakotetut_naapurit
            return self.etsi_vertikaalisesti(kasiteltava_solmu) 

    def etsi_horisontaalisesti(self):
        for suunta in (-1, 0), (1, 0):

    def etsi_diagonaalisesti(self):
        for suunta in (-1, -1), (-1, 1), (1, -1), (1, 1):
            
    def euklidinen_etaisyys(self, alku, loppu):
        etaisyys = math.sqrt((alku[0]-loppu[0])**2 + (alku[1]-loppu[1])**2)
        return etaisyys

