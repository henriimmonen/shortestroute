from collections import deque

class Dijkstra():
    def __init__(self, alku, loppu, verkko, kartta):
        self.alku = alku
        self.loppu = loppu
        self.verkko = verkko
        self.jono = deque([])
        self.kartta = kartta
        self.kasitellyt = set({})
        self.etaisyys = [[] for i in range(len(self.kartta[0])*len(self.kartta))]
        self.edeltava = [-1 for i in range(len(self.kartta[0])*len(self.kartta))]

    def etsi_reitti(self):
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
                self.etaisyys[naapuri[0]*len(self.kartta[0])+naapuri[1]] = (self.etaisyys[solmu[0]*len(self.kartta[0])+solmu[1]]+1)
                self.edeltava[naapuri[0]*len(self.kartta[0])+naapuri[1]] = (solmu[0]*len(self.kartta[0])+solmu[1])
        return self.edeltava

