import math
import heapq

class Dijkstra(): # pylint: disable=too-many-instance-attributes
    def __init__(self, alku, loppu, verkko, kartta):
        self.alku = alku
        self.loppu = loppu
        self.verkko = verkko
        self.kartta = kartta
        self.kasitellyt = set({})
        self.keko = []
        inf = 10**9
        self.etaisyys = [inf for i in range(len(self.kartta[0])*len(self.kartta))]
        self.edeltava = [-1 for i in range(len(self.kartta[0])*len(self.kartta))]

    def etsi_reitti(self):
        """Etsitään lyhyin reitti leveyshaulla

        Returns:
            self.edeltava: lista jokaista solmua edeltäneestä solmusta
        """
        heapq.heappush(self.keko, self.alku)
        self.kasitellyt.add(self.alku)
        self.etaisyys[self.alku[0]*len(self.kartta[0])+self.alku[1]] = 0
        while len(self.keko) > 0:
            solmu = heapq.heappop(self.keko)
            self.kasitellyt.add(solmu)
            if solmu[0] == self.loppu[0] and solmu[1] == self.loppu[1]:
                break
            for naapuri in self.verkko[(solmu[0]*len(self.kartta[0])+solmu[1])]:
                if naapuri in self.kasitellyt:
                    continue
                heapq.heappush(self.keko, naapuri)
                etaisyys_naapuriin = self.laske_etaisyys(solmu, naapuri)
                if self.etaisyys[naapuri[0]*len(self.kartta[0])+naapuri[1]] > self.etaisyys[
                    solmu[0]*len(self.kartta[0])+solmu[1]] + etaisyys_naapuriin:
                    self.etaisyys[naapuri[0]*len(self.kartta[0])+naapuri[1]] = self.etaisyys[
                        solmu[0]*len(self.kartta[0])+solmu[1]] + etaisyys_naapuriin
                    self.edeltava[naapuri[0]*len(self.kartta[0])+naapuri[1]] = (
                    solmu[0]*len(self.kartta[0])+solmu[1])
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
            edeltavat_solmut: lista jokaista solmua edeltäneestä solmusta

        Returns:
            reitti_oikein_pain: lista kuljetusta reitistä alusta loppuun
        """
        reitti = []
        solmu = self.loppu[0]*len(self.kartta[0])+self.loppu[1]
        reitti.append(solmu)

        while edeltavat_solmut[solmu] != -1:
            reitti.append(edeltavat_solmut[solmu])
            solmu = edeltavat_solmut[solmu]
        reitti_oikein_pain = []
        for i in range(len(reitti)-1, -1, -1):
            reitti_oikein_pain.append((reitti[i]//len(self.kartta[0]),
                                       reitti[i]%len(self.kartta[0])))
        return reitti_oikein_pain
