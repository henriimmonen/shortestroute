import heapq, math
import apufunktiot

class JumpPointSearch():
    def __init__(self, aloitus_solmu, lopetus_solmu, verkko, kartta): # pylint: disable=too-many-instance-attributes
        self.aloitus_solmu = aloitus_solmu
        self.lopetus_solmu = lopetus_solmu
        self.verkko = verkko
        self.kartta = kartta
        self.keko = []
        self.kasitellyt = set()
        self.hyppypisteet = []
        self.g = {self.aloitus_solmu: 0}
        self.f = {self.aloitus_solmu: self.euklidinen_etaisyys(self.aloitus_solmu, self.lopetus_solmu)}
        self.edeltava = {}

    def hae_reitti(self):
        heapq.heappush(self.keko, (0, self.aloitus_solmu))
        while len(self.keko) != 0:
            kasiteltava_solmu = heapq.heappop(self.keko)[1]

            if self.maalissa(kasiteltava_solmu):
                return self.edeltava

            self.etsi_hyppypiste(kasiteltava_solmu)
            self.kasittele_hyppypisteet(kasiteltava_solmu)

    def etsi_hyppypiste(self, kasiteltava_solmu):
        self.hyppypisteet = []

        if kasiteltava_solmu in self.kasitellyt:
            return

        self.kasitellyt.add(kasiteltava_solmu)

        naapurit = self.verkko[(kasiteltava_solmu[0]*len(self.kartta[0])+kasiteltava_solmu[1])]
        for naapuri in naapurit:
            if naapuri in self.kasitellyt:
                continue

            if self.maalissa(naapuri):
                self.hyppypisteet.append(naapuri)
                return

            suuntaX = naapuri[0] - kasiteltava_solmu[0]
            suuntaY = naapuri[1] - kasiteltava_solmu[1]


            if suuntaX == 0 and suuntaY != 0:
                self.etsi_horisontaalisesti(kasiteltava_solmu, suuntaX, suuntaY)
            if suuntaX != 0 and suuntaY == 0:
                self.etsi_vertikaalisesti(kasiteltava_solmu, suuntaX, suuntaY)
            if suuntaX != 0 and suuntaY != 0:
                self.etsi_diagonaalisesti(kasiteltava_solmu, suuntaX, suuntaY)
        return

    def kasittele_hyppypisteet(self, kasiteltava_solmu):
        for hyppypiste in self.hyppypisteet:

            if hyppypiste in self.kasitellyt:
                continue

            alustava_pituus = self.g[kasiteltava_solmu] + self.euklidinen_etaisyys(kasiteltava_solmu, hyppypiste)

            if alustava_pituus < self.g.get(hyppypiste, 0) or hyppypiste not in [solmu[1] for solmu in self.keko]:
                self.g[hyppypiste] = alustava_pituus
                self.f[hyppypiste] = alustava_pituus + self.euklidinen_etaisyys(hyppypiste, self.lopetus_solmu)
                self.edeltava[hyppypiste] = kasiteltava_solmu
                heapq.heappush(self.keko, (self.f[hyppypiste], hyppypiste))

    def etsi_horisontaalisesti(self, kasiteltava_solmu, suuntaX, suuntaY):
        kasiteltava_solmu = (kasiteltava_solmu[0]+suuntaX, kasiteltava_solmu[1]+suuntaY)

        if not apufunktiot.verkon_sisalla(kasiteltava_solmu, self.kartta) or not apufunktiot.solmun_naapuriin_voi_kulkea(
                kasiteltava_solmu, self.kartta):
            return False

        if self.maalissa(kasiteltava_solmu):
            self.hyppypisteet.append(kasiteltava_solmu)
            return True

        if apufunktiot.verkon_sisalla((kasiteltava_solmu[0]-1, kasiteltava_solmu[1]), self.kartta):
            if not apufunktiot.solmun_naapuriin_voi_kulkea((kasiteltava_solmu[0]-1, kasiteltava_solmu[1]), self.kartta):
                if apufunktiot.solmun_naapuriin_voi_kulkea((kasiteltava_solmu[0]-1, kasiteltava_solmu[1]+suuntaY), self.kartta):
                    self.hyppypisteet.append(kasiteltava_solmu)
                    return True

        if apufunktiot.verkon_sisalla((kasiteltava_solmu[0]+1, kasiteltava_solmu[1]), self.kartta):
            if not apufunktiot.solmun_naapuriin_voi_kulkea((kasiteltava_solmu[0]+1, kasiteltava_solmu[1]), self.kartta):
                if apufunktiot.solmun_naapuriin_voi_kulkea((kasiteltava_solmu[0]+1, kasiteltava_solmu[1]+suuntaY), self.kartta):
                    self.hyppypisteet.append(kasiteltava_solmu)
                    return True

        return self.etsi_horisontaalisesti(kasiteltava_solmu, suuntaX, suuntaY) 

    def etsi_vertikaalisesti(self, kasiteltava_solmu, suuntaX, suuntaY):
        kasiteltava_solmu = (kasiteltava_solmu[0]+suuntaX, kasiteltava_solmu[1]+suuntaY)

        if not apufunktiot.verkon_sisalla(kasiteltava_solmu, self.kartta) or not apufunktiot.solmun_naapuriin_voi_kulkea(
                kasiteltava_solmu, self.kartta):
            return False

        if self.maalissa(kasiteltava_solmu):
            self.hyppypisteet.append(kasiteltava_solmu)
            return True

        if apufunktiot.verkon_sisalla((kasiteltava_solmu[0], kasiteltava_solmu[1]+1), self.kartta):
            if not apufunktiot.solmun_naapuriin_voi_kulkea((kasiteltava_solmu[0], kasiteltava_solmu[1]+1), self.kartta):
                if apufunktiot.solmun_naapuriin_voi_kulkea((kasiteltava_solmu[0]+suuntaX, kasiteltava_solmu[1]+1), self.kartta):
                    self.hyppypisteet.append(kasiteltava_solmu)
                    return True

        if apufunktiot.verkon_sisalla((kasiteltava_solmu[0], kasiteltava_solmu[1]-1), self.kartta):
            if not apufunktiot.solmun_naapuriin_voi_kulkea((kasiteltava_solmu[0], kasiteltava_solmu[1]-1), self.kartta):
                if apufunktiot.solmun_naapuriin_voi_kulkea((kasiteltava_solmu[0]+suuntaX, kasiteltava_solmu[1]-1), self.kartta):
                    self.hyppypisteet.append(kasiteltava_solmu)
                    return True

        return self.etsi_vertikaalisesti(kasiteltava_solmu, suuntaX, suuntaY)

    def etsi_diagonaalisesti(self, kasiteltava_solmu, suuntaX, suuntaY):
        kasiteltava_solmu = (kasiteltava_solmu[0]+suuntaX, kasiteltava_solmu[1]+suuntaY)

        if not apufunktiot.verkon_sisalla(kasiteltava_solmu, self.kartta) or not apufunktiot.solmun_naapuriin_voi_kulkea(
                kasiteltava_solmu, self.kartta):
            return False

        if self.maalissa(kasiteltava_solmu):
            self.hyppypisteet.append(kasiteltava_solmu)
            return True

        if len(self.verkko[(kasiteltava_solmu[0]*len(self.kartta[0])+kasiteltava_solmu[1])]) < 8:
            if kasiteltava_solmu[0] != 0 and kasiteltava_solmu[0] != len(self.kartta):
                if kasiteltava_solmu[1] != 0 and kasiteltava_solmu[1] != len(self.kartta[0]):
                    self.hyppypisteet.append(kasiteltava_solmu)
                    return True

        if self.etsi_horisontaalisesti(kasiteltava_solmu, 0, suuntaY):
            self.hyppypisteet.append(kasiteltava_solmu)
            return True
        
        if self.etsi_vertikaalisesti(kasiteltava_solmu, suuntaX, 0):
            self.hyppypisteet.append(kasiteltava_solmu)
            return True

        return self.etsi_diagonaalisesti(kasiteltava_solmu, suuntaX, suuntaY)

    def euklidinen_etaisyys(self, alku, loppu):
        etaisyys = math.sqrt((alku[0]-loppu[0])**2 + (alku[1]-loppu[1])**2)
        return etaisyys

    def maalissa(self, kasiteltava_solmu):
        if kasiteltava_solmu[0] == self.lopetus_solmu[0] and kasiteltava_solmu[1] == self.lopetus_solmu[1]:
            return True
        return False

    def tulosta_reitti(self, edeltavat, kasiteltava_solmu):
        reitti = []
        while kasiteltava_solmu in edeltavat:
            reitti.append(kasiteltava_solmu)
            kasiteltava_solmu = self.edeltava[kasiteltava_solmu]
        reitti.append(self.aloitus_solmu)
        reitti = reitti[::-1]
        print(reitti)
