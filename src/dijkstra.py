import math
import heapq

class Dijkstra: # pylint: disable=too-many-instance-attributes
    def __init__(self, alku, loppu, verkko, kartta):
        self.aloitus_solmu = alku
        self.lopetus_solmu = loppu
        self.verkko = verkko
        self.kartta = kartta
        self.kasitellyt = set()
        self.keko = []
        inf = 10**9
        self.etaisyys = [inf for i in range(len(self.kartta[0])*len(self.kartta))]
        self.edeltava = [-1 for i in range(len(self.kartta[0])*len(self.kartta))]

    def etsi_reitti(self):
        """Etsitään lyhyin reitti

        Returns:
            self.edeltava: Lista jokaista solmua edeltäneestä solmusta
        """
        heapq.heappush(self.keko, self.aloitus_solmu)
        self.etaisyys[self.aloitus_solmu[0]*len(self.kartta[0])+self.aloitus_solmu[1]] = 0

        while len(self.keko) > 0:
            kasiteltava_solmu = heapq.heappop(self.keko)

            if kasiteltava_solmu in self.kasitellyt:
                continue

            self.kasitellyt.add(kasiteltava_solmu)

            if self.maalissa(kasiteltava_solmu):
                break

            for naapuri in self.verkko[
                    (kasiteltava_solmu[0]*len(self.kartta[0])+kasiteltava_solmu[1])
                    ]:
                etaisyys_naapuriin = self.laske_etaisyys(kasiteltava_solmu, naapuri)

                if self.etaisyys[naapuri[0]*len(self.kartta[0])+naapuri[1]] > self.etaisyys[
                    kasiteltava_solmu[0]*len(self.kartta[0])+kasiteltava_solmu[1]
                    ] + etaisyys_naapuriin:

                    self.etaisyys[naapuri[0]*len(self.kartta[0])+naapuri[1]] = self.etaisyys[
                        kasiteltava_solmu[0]*len(self.kartta[0])+kasiteltava_solmu[1]
                        ] + etaisyys_naapuriin

                    self.edeltava[naapuri[0]*len(self.kartta[0])+naapuri[1]] = (
                    kasiteltava_solmu[0]*len(self.kartta[0])+kasiteltava_solmu[1])

                heapq.heappush(self.keko, naapuri)
        return self.edeltava

    def laske_etaisyys(self, solmu, naapuri):
        """Diagonaalisesti liikuttaessa etäisyys on sqrt(2), muuten 1
        """
        if solmu[0] - naapuri[0] != 0 and solmu[1] - naapuri[1] != 0:
            return math.sqrt(2)
        return 1

    def tulosta_reitti(self, edeltavat_solmut):
        """Muodostetaan reitti oikeassa järjestyksessä

        Args:
            edeltavat_solmut: Lista jokaista solmua edeltäneestä solmusta

        Returns:
            reitti_oikein_pain: Lista kuljetusta reitistä alusta loppuun
        """
        reitti = []
        solmu = self.lopetus_solmu[0]*len(self.kartta[0])+self.lopetus_solmu[1]
        reitti.append(solmu)

        while edeltavat_solmut[solmu] != -1:
            reitti.append(edeltavat_solmut[solmu])
            solmu = edeltavat_solmut[solmu]

        reitti_oikein_pain = []
        for i in range(len(reitti)-1, -1, -1):
            reitti_oikein_pain.append((reitti[i]//len(self.kartta[0]),
                                       reitti[i]%len(self.kartta[0])))
        return reitti_oikein_pain

    def maalissa(self, kasiteltava_solmu):
        """Tarkistetaan ollaanko päädytty maaliin

        Args:
            kasiteltava_solmu: Käsittelyssä oleva solmu

        Returns:
           Boolean-arvo: True jos maalissa, muuten False
        """
        if kasiteltava_solmu[0] == self.lopetus_solmu[0]:
            if kasiteltava_solmu[1] == self.lopetus_solmu[1]:
                return True
        return False
