from collections import deque

class Dijkstra(): # pylint: disable=too-many-instance-attributes
    def __init__(self, alku, loppu, verkko, kartta):
        self.alku = alku
        self.loppu = loppu
        self.verkko = verkko
        self.kartta = kartta
        self.kasitellyt = set({})
        self.jono = deque([])
        self.etaisyys = [[] for i in range(len(self.kartta[0])*len(self.kartta))]
        self.edeltava = [-1 for i in range(len(self.kartta[0])*len(self.kartta))]

    def etsi_reitti(self):
        """Etsitään lyhyin reitti leveyshaulla

        Returns:
            self.edeltava: lista jokaista solmua edeltäneestä solmusta
        """
        self.jono.append(self.alku)
        self.kasitellyt.add(self.alku)
        self.etaisyys[self.alku[0]*len(self.kartta[0])+self.alku[1]] = 0
        while self.jono:
            solmu = self.jono.popleft()
            for naapuri in self.verkko[(solmu[0]*len(self.kartta[0])+solmu[1])]:

                if naapuri in self.kasitellyt:
                    continue

                self.jono.append(naapuri)
                self.kasitellyt.add(naapuri)
                self.etaisyys[naapuri[0]*len(self.kartta[0])+naapuri[1]] = (
                    self.etaisyys[solmu[0]*len(self.kartta[0])+solmu[1]]+1)
                self.edeltava[naapuri[0]*len(self.kartta[0])+naapuri[1]] = (
                    solmu[0]*len(self.kartta[0])+solmu[1])
        return self.edeltava

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
