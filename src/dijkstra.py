import heapq

class Dijkstra():
    def __init__(self, alku, loppu, kartta):
        self.alku = alku
        self.loppu = loppu
        self.kartta = kartta
        self.keko = []
        self.kasitellyt = []

    def etsi_reitti(self):
        return 
        heapq.heappush(self.keko, self.alku)
        while not self.keko.empty():
            solmu = heapq.heappop(self.keko)
            if self.kasitellyt[solmu]:
                continue
            self.kasitellyt[solmu] = True
            kaaret = self.solmun_kaaret(solmu)
