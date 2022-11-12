class Apufunktiot():
    def alusta_kartta(self, osoite):
        """Alustetaan matriisikartta tiedostosta

        Args:
            osoite: suhteellinen osoite, josta karttatiedosto luetaan

        Returns:
            matriisi: kartta
        """
        lukija = open(osoite, 'r')
        kartta = []
        for rivi in lukija:
            if rivi[0] == '.' or rivi[0] == '@':
                kartta.append(rivi[0:-1])
        lukija.close()
        return kartta

    def kaarilista(self, kartta):
        """ Luodaan kaarilista """
        self.verkko = [] # Luodaan verkko
        for i in range(len(kartta)):
            for j in range(len(kartta[i])):
                self._tarkista_naapurit((i, j), kartta)
        return self.verkko

    def _tarkista_naapurit(self, solmu, kartta):
        solmun_naapurit = [] # Jokaisella solmulla on lista naapureista
        for naapuri in [(solmu[0]-1, solmu[1]-1), (solmu[0]-1, solmu[1]), (solmu[0]-1, solmu[1]+1),
                        (solmu[0], solmu[1]-1), (solmu[0], solmu[1]+1), (solmu[0]+1, solmu[1]-1),
                        (solmu[0]+1, solmu[1]), (solmu[0]+1, solmu[1]+1)]:
            if self._verkon_sisalla(naapuri, kartta): # Tarkistetaan onko naapuri verkon sisällä
                if self._solmun_naapuriin_voi_kulkea(naapuri, kartta):
                    solmun_naapurit.append(naapuri)
        self.verkko.append(solmun_naapurit)

    def _verkon_sisalla(self, solmu, kartta): # Tarkistetaan solmu matriisin sisällä
        if solmu[0] >= 0 and solmu[0] < len(kartta):
            if solmu[1] >= 0 and solmu[1] < len(kartta[0]):
                return True
        return False

    def _solmun_naapuriin_voi_kulkea(self, naapuri, kartta):
        if kartta[naapuri[0]][naapuri[1]] == '.':
            return True
        return False
