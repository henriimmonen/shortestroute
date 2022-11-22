import heapq, math
import apufunktiot

class JumpPointSearch():
    def __init__(self, aloitus_solmu, lopetus_solmu, verkko, kartta):
        self.aloitus_solmu = aloitus_solmu
        self.lopetus_solmu = lopetus_solmu
        self.verkko = verkko
        self.kartta = kartta
        self.keko = []
        self.kasitellyt = set()
        self.hyppypisteet = []
        inf = 10**9
        self.etaisyys = [inf for i in range(len(self.kartta[0])*len(self.kartta))]
        self.edeltava = [-1 for i in range(len(self.kartta[0])*len(self.kartta))]

    def hae_reitti(self):
        heapq.heappush(self.keko, (0, self.aloitus_solmu))
        while len(self.keko) != 0:
            kasiteltava_solmu = heapq.heappop(self.keko)[1]
            self.etsi_hyppypiste(kasiteltava_solmu)

    def etsi_hyppypiste(self, kasiteltava_solmu):
        self.hyppypisteet = []
        if kasiteltava_solmu in self.kasitellyt:
            return
        self.kasitellyt.add(kasiteltava_solmu)

        naapurit = self.verkko[(kasiteltava_solmu[0]*len(self.kartta[0])+kasiteltava_solmu[1])]
        for naapuri in naapurit:
            suuntaX = naapuri[0] - kasiteltava_solmu[0]
            suuntaY = naapuri[1] - kasiteltava_solmu[1]

            self.etsi_horisontaalisesti(kasiteltava_solmu, suuntaX, suuntaY)
            self.etsi_vertikaalisesti(kasiteltava_solmu, suuntaX, suuntaY)
            self.etsi_diagonaalisesti(kasiteltava_solmu, suuntaX, suuntaY)

        # Käsitellään self.hyppypisteet ja päivitetään pituudet

    def etsi_horisontaalisesti(self, kasiteltava_solmu, suuntaX, suuntaY):
        kasiteltava_solmu = (kasiteltava_solmu[0]+suuntaX, kasiteltava_solmu[1]+suuntaY)

        if not apufunktiot.verkon_sisalla(kasiteltava_solmu, self.kartta):
            #tähän tarkistus voidaanko kulkea!
            return

        if kasiteltava_solmu[0] == self.lopetus_solmu[0] and kasiteltava_solmu[1] == self.lopetus_solmu[1]:
            self.hyppypisteet.append(kasiteltava_solmu)
            return

        if not apufunktiot.solmun_naapuriin_voi_kulkea(kasiteltava_solmu, self.kartta):
            if (apufunktiot.solmun_naapuriin_voi_kulkea((kasiteltava_solmu[0]-1, kasiteltava_solmu[1]), self.kartta)
            or apufunktiot.solmun_naapuriin_voi_kulkea((kasiteltava_solmu[0]+1, kasiteltava_solmu[1]), self.kartta)):
                self.hyppypisteet.append(kasiteltava_solmu)
            return

        return self.etsi_vertikaalisesti(kasiteltava_solmu, suuntaX, suuntaY) 

    def etsi_vertikaalisesti(self, kasiteltava_solmu, suuntaX, suuntaY):
        kasiteltava_solmu = (kasiteltava_solmu[0]+suuntaX, kasiteltava_solmu[1]+suuntaY)

        if not apufunktiot.verkon_sisalla(kasiteltava_solmu, self.kartta):
            return

        if kasiteltava_solmu[0] == self.lopetus_solmu[0] and kasiteltava_solmu[1] == self.lopetus_solmu[1]:
            self.hyppypisteet.append(kasiteltava_solmu)
            return

        if not apufunktiot.solmun_naapuriin_voi_kulkea(kasiteltava_solmu, self.kartta):
            if (apufunktiot.solmun_naapuriin_voi_kulkea((kasiteltava_solmu[0], kasiteltava_solmu[1]+1), self.kartta)
            or apufunktiot.solmun_naapuriin_voi_kulkea((kasiteltava_solmu[0], kasiteltava_solmu[1]-1), self.kartta)):
                self.hyppypisteet.append(kasiteltava_solmu)
            return

        return self.etsi_vertikaalisesti(kasiteltava_solmu, suuntaX, suuntaY)

    def etsi_diagonaalisesti(self, kasiteltava_solmu, suuntaX, suuntaY):
        kasiteltava_solmu = (kasiteltava_solmu[0]+suuntaX, kasiteltava_solmu[1]+suuntaY)

        if not apufunktiot.verkon_sisalla(kasiteltava_solmu, self.kartta):
            return

        if kasiteltava_solmu[0] == self.lopetus_solmu[0] and kasiteltava_solmu[1] == self.lopetus_solmu[1]:
            self.hyppypisteet.append(kasiteltava_solmu)
            return
        
        self.etsi_horisontaalisesti(kasiteltava_solmu, 0, suuntaY)
        self.etsi_vertikaalisesti(kasiteltava_solmu, suuntaX, 0)

        if not apufunktiot.solmun_naapuriin_voi_kulkea(kasiteltava_solmu, self.kartta):
            if (apufunktiot.solmun_naapuriin_voi_kulkea((kasiteltava_solmu[0], kasiteltava_solmu[1]+1), self.kartta)
            or apufunktiot.solmun_naapuriin_voi_kulkea((kasiteltava_solmu[0], kasiteltava_solmu[1]-1), self.kartta)):
                self.hyppypisteet.append(kasiteltava_solmu)
            return

        return self.etsi_diagonaalisesti

    def euklidinen_etaisyys(self, alku, loppu):
        etaisyys = math.sqrt((alku[0]-loppu[0])**2 + (alku[1]-loppu[1])**2)
        return etaisyys

