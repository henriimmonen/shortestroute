import heapq
import math
import apufunktiot

class JumpPointSearch: # pylint: disable=too-many-instance-attributes
    def __init__(self, aloitus_solmu, lopetus_solmu, verkko, kartta):
        self.aloitus_solmu = aloitus_solmu
        self.lopetus_solmu = lopetus_solmu
        self.verkko = verkko
        self.kartta = kartta
        self.keko = []
        self.kasitellyt = set()
        self.hyppypisteet = []
        self.etaisyys_solmuun = {self.aloitus_solmu: 0}
        self.etaisyys_maaliin = {self.aloitus_solmu: self.euklidinen_etaisyys(
                self.aloitus_solmu, self.lopetus_solmu)}
        self.edeltava = {}

    def hae_reitti(self):
        """Runko algoritmin toiminnalle

        Returns:
            self.edeltava: Palautetaan sanakirja kuljetuista solmuista
        """
        heapq.heappush(self.keko, (0, self.aloitus_solmu))
        while len(self.keko) != 0:
            kasiteltava_solmu = heapq.heappop(self.keko)[1]

            if self.maalissa(kasiteltava_solmu):
                return self.edeltava

            self.etsi_hyppypiste(kasiteltava_solmu)
            self.kasittele_hyppypisteet(kasiteltava_solmu)

    def etsi_hyppypiste(self, kasiteltava_solmu):
        """Annetun solmun naapureista lähdetään etsimään hyppypisteitä
        """
        self.hyppypisteet = []

        if kasiteltava_solmu in self.kasitellyt:
            return

        self.kasitellyt.add(kasiteltava_solmu)

        if kasiteltava_solmu == self.aloitus_solmu:
            naapurit = self.verkko[(
                kasiteltava_solmu[0]*len(
                    self.kartta[0]
                    )+kasiteltava_solmu[1]
                    )]
        else:
            naapurit, suunta = self.karsi_naapurit(kasiteltava_solmu)
            naapurit = self.tarkista_pakotetut_naapurit(kasiteltava_solmu, suunta, naapurit)

        for naapuri in naapurit:

            if naapuri in self.kasitellyt:
                continue

            suunta_x = naapuri[0] - kasiteltava_solmu[0]
            suunta_y = naapuri[1] - kasiteltava_solmu[1]

            if suunta_x == 0 and suunta_y != 0:
                hyppypiste = self.etsi_horisontaalisesti(naapuri, suunta_x, suunta_y)
            if suunta_x != 0 and suunta_y == 0:
                hyppypiste = self.etsi_vertikaalisesti(naapuri, suunta_x, suunta_y)
            if suunta_x != 0 and suunta_y != 0:
                hyppypiste = self.etsi_diagonaalisesti(naapuri, suunta_x, suunta_y)

            if hyppypiste is not None:
                self.hyppypisteet.append(hyppypiste)

                if self.maalissa(hyppypiste):
                    return
        return

    def kasittele_hyppypisteet(self, kasiteltava_solmu):
        """Kun hyppypisteet on saatu kerättyä, päivitetään kuljettu etäisyys sekä etäisyys maaliin
        """
        for hyppypiste in self.hyppypisteet:

            if hyppypiste in self.kasitellyt:
                continue

            alustava_pituus = self.etaisyys_solmuun[
                    kasiteltava_solmu
                    ] + self.euklidinen_etaisyys(
                        kasiteltava_solmu, hyppypiste)

            if alustava_pituus < self.etaisyys_solmuun.get(hyppypiste, 0) or hyppypiste not in [
                    solmu[1] for solmu in self.keko]:
                self.etaisyys_solmuun[hyppypiste] = alustava_pituus
                self.etaisyys_maaliin[hyppypiste] = alustava_pituus + self.euklidinen_etaisyys(
                        hyppypiste, self.lopetus_solmu)
                self.edeltava[hyppypiste] = kasiteltava_solmu
                heapq.heappush(self.keko, (self.etaisyys_maaliin[hyppypiste], hyppypiste))

    def etsi_horisontaalisesti(self, kasiteltava_solmu, suunta_x, suunta_y):
        """Etsitään hyppysolmua horisontaalisesti
        """
        if not apufunktiot.verkon_sisalla(
                kasiteltava_solmu, self.kartta
                ) or not apufunktiot.solmun_naapuriin_voi_kulkea(
                kasiteltava_solmu, self.kartta):
            return None

        if self.maalissa(kasiteltava_solmu):
            return kasiteltava_solmu

        if not apufunktiot.solmun_naapuriin_voi_kulkea((
                kasiteltava_solmu[0]-1, kasiteltava_solmu[1]
                ), self.kartta):
            if apufunktiot.solmun_naapuriin_voi_kulkea((
                    kasiteltava_solmu[0]-1, kasiteltava_solmu[1]+suunta_y
                    ), self.kartta):
                return kasiteltava_solmu

        if not apufunktiot.solmun_naapuriin_voi_kulkea((
                kasiteltava_solmu[0]+1, kasiteltava_solmu[1]
                ), self.kartta):
            if apufunktiot.solmun_naapuriin_voi_kulkea((
                    kasiteltava_solmu[0]+1, kasiteltava_solmu[1]+suunta_y
                    ), self.kartta):
                return kasiteltava_solmu

        return self.etsi_horisontaalisesti((
            kasiteltava_solmu[0]+suunta_x, kasiteltava_solmu[1]+suunta_y
            ), suunta_x, suunta_y)

    def etsi_vertikaalisesti(self, kasiteltava_solmu, suunta_x, suunta_y):
        """Etsitään hyppysolmua vertikaalisesti
        """
        if not apufunktiot.verkon_sisalla(
                kasiteltava_solmu, self.kartta
                ) or not apufunktiot.solmun_naapuriin_voi_kulkea(
                kasiteltava_solmu, self.kartta):
            return None

        if self.maalissa(kasiteltava_solmu):
            return kasiteltava_solmu

        if not apufunktiot.solmun_naapuriin_voi_kulkea((
                kasiteltava_solmu[0], kasiteltava_solmu[1]+1
                ), self.kartta):
            if apufunktiot.solmun_naapuriin_voi_kulkea((
                    kasiteltava_solmu[0]+suunta_x, kasiteltava_solmu[1]+1
                    ), self.kartta):
                return kasiteltava_solmu

        if not apufunktiot.solmun_naapuriin_voi_kulkea((
                kasiteltava_solmu[0], kasiteltava_solmu[1]-1
                ), self.kartta):
            if apufunktiot.solmun_naapuriin_voi_kulkea((
                    kasiteltava_solmu[0]+suunta_x, kasiteltava_solmu[1]-1
                    ), self.kartta):
                return kasiteltava_solmu

        return self.etsi_vertikaalisesti((
            kasiteltava_solmu[0]+suunta_x, kasiteltava_solmu[1]+suunta_y
            ), suunta_x, suunta_y)

    def etsi_diagonaalisesti(self, kasiteltava_solmu, suunta_x, suunta_y):
        """Etsitään hyppysolmua diagonaalisesti
        """
        if not apufunktiot.verkon_sisalla(
                kasiteltava_solmu, self.kartta
                ) or not apufunktiot.solmun_naapuriin_voi_kulkea(
                kasiteltava_solmu, self.kartta
                ):
            return None

        if self.maalissa(kasiteltava_solmu):
            return kasiteltava_solmu

        if self.etsi_horisontaalisesti(kasiteltava_solmu, 0, suunta_y) is not None:
            return kasiteltava_solmu

        if self.etsi_vertikaalisesti(kasiteltava_solmu, suunta_x, 0) is not None:
            return kasiteltava_solmu

        return self.etsi_diagonaalisesti((
            kasiteltava_solmu[0]+suunta_x, kasiteltava_solmu[1]+suunta_y
            ), suunta_x, suunta_y)

    def euklidinen_etaisyys(self, alku, loppu):
        """Lasketaan kahden koordinaatin välinen euklidinen etäisyys
        """
        etaisyys = math.sqrt((alku[0]-loppu[0])**2 + (alku[1]-loppu[1])**2)
        return etaisyys

    def maalissa(self, kasiteltava_solmu):
        """Tarkistetaan ollaanko päästy määritettyyn maalisolmuun

        Args:
            kasiteltava_solmu: Käsittelyssä oleva solmu tuple-muodossa

        Returns:
            Boolean-arvo: True jos ollaan maalissa, muuten False
        """
        if kasiteltava_solmu[0] == self.lopetus_solmu[0]:
            if kasiteltava_solmu[1] == self.lopetus_solmu[1]:
                return True
        return False

    def karsi_naapurit(self, kasiteltava_solmu):
        """Karsitaan solmun naapureista jps-algoritmin sääntöjen mukaisesti
        jatkosolmut

        Args:
            kasiteltava_solmu: Käsittelyssä oleva solmu tuple-muodossa

        Returns:
            list: Lista naapurisolmuista
        """
        edeltava_solmu = self.edeltava[kasiteltava_solmu]

        suunta_x = kasiteltava_solmu[0] - edeltava_solmu[0]
        suunta_y = kasiteltava_solmu[1] - edeltava_solmu[1]

        if suunta_x == 0 or suunta_y == 0:
            if suunta_x == 0:
                if suunta_y > 0:
                    suunta_y = 1
                else:
                    suunta_y = -1
            if suunta_y == 0:
                if suunta_x > 0:
                    suunta_x = 1
                else:
                    suunta_x = -1
            return [(
                kasiteltava_solmu[0]+suunta_x, kasiteltava_solmu[1]+suunta_y
                )], (suunta_x, suunta_y)

        if suunta_x != 0 and suunta_y != 0:
            if suunta_x > 0:
                suunta_x = 1
            if suunta_x < 0:
                suunta_x = -1
            if suunta_y > 0:
                suunta_y = 1
            if suunta_y < 0:
                suunta_y = -1
            return [(kasiteltava_solmu[0]+suunta_x, kasiteltava_solmu[1]+suunta_y),
                    (kasiteltava_solmu[0]+suunta_x, kasiteltava_solmu[1]),
                    (kasiteltava_solmu[0], kasiteltava_solmu[1]+suunta_y)], (suunta_x, suunta_y)
        return []

    def tulosta_reitti(self, edeltavat, kasiteltava_solmu):
        """Tulostetaan kuljettu reitti

        Args:
            edeltavat: Sanakirja kuljetuista solmuista
            kasiteltava_solmu: Käsittelyssä oleva solmu
        """
        reitti = []
        while kasiteltava_solmu in edeltavat:
            reitti.append(kasiteltava_solmu)
            kasiteltava_solmu = self.edeltava[kasiteltava_solmu]
        reitti.append(self.aloitus_solmu)
        reitti = reitti[::-1]
        return reitti

    def tarkista_pakotetut_naapurit(self, kasiteltava_solmu, suunta, naapurit): # pylint: disable=too-many-branches
        """Tarkistetaan onko solmulla pakotettuja naapureita

        Args:
            kasiteltava_solmu: Käsittelyssä oleva solmu
            suunta: Kulkusuunta tuple-muodossa
            naapurit: Lista solmun naapureista

        Returns:
            naapurit: Lista solmun naapureista, johon on lisätty mahdolliset pakotetut
            naapurit
        """
        if suunta[0] == 0 and suunta[1] != 0:
            if not apufunktiot.solmun_naapuriin_voi_kulkea((
                    kasiteltava_solmu[0]+1, kasiteltava_solmu[1]
                    ), self.kartta):
                if apufunktiot.solmun_naapuriin_voi_kulkea((
                        kasiteltava_solmu[0]+1, kasiteltava_solmu[1]+suunta[1]
                        ), self.kartta):
                    naapurit.append((kasiteltava_solmu[0]+1, kasiteltava_solmu[1]+suunta[1]))

            if not apufunktiot.solmun_naapuriin_voi_kulkea((
                    kasiteltava_solmu[0]-1, kasiteltava_solmu[1]
                    ), self.kartta):
                if apufunktiot.solmun_naapuriin_voi_kulkea((
                        kasiteltava_solmu[0]-1, kasiteltava_solmu[1]+suunta[1]
                        ), self.kartta):
                    naapurit.append((kasiteltava_solmu[0]-1, kasiteltava_solmu[1]+suunta[1]))

        if suunta[0] != 0 and suunta[1] == 0:
            if not apufunktiot.solmun_naapuriin_voi_kulkea((
                kasiteltava_solmu[0], kasiteltava_solmu[1]+1
                ), self.kartta):
                if apufunktiot.solmun_naapuriin_voi_kulkea((
                        kasiteltava_solmu[0]+suunta[0], kasiteltava_solmu[1]+1
                        ), self.kartta):
                    naapurit.append((kasiteltava_solmu[0]+suunta[0], kasiteltava_solmu[1]+1))

            if not apufunktiot.solmun_naapuriin_voi_kulkea((
                kasiteltava_solmu[0], kasiteltava_solmu[1]-1
                ), self.kartta):
                if apufunktiot.solmun_naapuriin_voi_kulkea((
                        kasiteltava_solmu[0]+suunta[0], kasiteltava_solmu[1]-1
                        ), self.kartta):
                    naapurit.append((kasiteltava_solmu[0]+suunta[0], kasiteltava_solmu[1]-1))

        if suunta[0] != 0 and suunta[1] != 0:
            if suunta[0] == -1 and suunta[1] == -1:
                if not apufunktiot.solmun_naapuriin_voi_kulkea((
                    kasiteltava_solmu[0], kasiteltava_solmu[1]+1
                    ), self.kartta):
                    if apufunktiot.solmun_naapuriin_voi_kulkea((
                            kasiteltava_solmu[0]+suunta[0], kasiteltava_solmu[1]+1
                            ), self.kartta):
                        naapurit.append((kasiteltava_solmu[0]+suunta[0], kasiteltava_solmu[1]+1))

                if not apufunktiot.solmun_naapuriin_voi_kulkea((
                    kasiteltava_solmu[0]+1, kasiteltava_solmu[1]
                    ), self.kartta):
                    if apufunktiot.solmun_naapuriin_voi_kulkea((
                            kasiteltava_solmu[0]+1, kasiteltava_solmu[1]+suunta[1]
                            ), self.kartta):
                        naapurit.append((kasiteltava_solmu[0]+1, kasiteltava_solmu[1]+suunta[1]))

            if suunta[0] == 1 and suunta[1] == -1:
                if not apufunktiot.solmun_naapuriin_voi_kulkea((
                    kasiteltava_solmu[0]-1, kasiteltava_solmu[1]
                    ), self.kartta):
                    if apufunktiot.solmun_naapuriin_voi_kulkea((
                            kasiteltava_solmu[0]-1, kasiteltava_solmu[1]+suunta[1]
                            ), self.kartta):
                        naapurit.append((kasiteltava_solmu[0]-1, kasiteltava_solmu[1]+suunta[1]))

                if not apufunktiot.solmun_naapuriin_voi_kulkea((
                    kasiteltava_solmu[0], kasiteltava_solmu[1]+1
                    ), self.kartta):
                    if apufunktiot.solmun_naapuriin_voi_kulkea((
                            kasiteltava_solmu[0]+suunta[0], kasiteltava_solmu[1]+1
                            ), self.kartta):
                        naapurit.append((kasiteltava_solmu[0]+suunta[0], kasiteltava_solmu[1]+1))

            if suunta[0] == -1 and suunta[1] == 1:
                if not apufunktiot.solmun_naapuriin_voi_kulkea((
                    kasiteltava_solmu[0]+1, kasiteltava_solmu[1]
                    ), self.kartta):
                    if apufunktiot.solmun_naapuriin_voi_kulkea((
                            kasiteltava_solmu[0]+1, kasiteltava_solmu[1]+suunta[1]
                            ), self.kartta):
                        naapurit.append((kasiteltava_solmu[0]+1, kasiteltava_solmu[1]+suunta[1]))

                if not apufunktiot.solmun_naapuriin_voi_kulkea((
                    kasiteltava_solmu[0], kasiteltava_solmu[1]-1
                    ), self.kartta):
                    if apufunktiot.solmun_naapuriin_voi_kulkea((
                            kasiteltava_solmu[0]+suunta[0], kasiteltava_solmu[1]-1
                            ), self.kartta):
                        naapurit.append((kasiteltava_solmu[0]+suunta[0], kasiteltava_solmu[1]-1))

            if suunta[0] == 1 and suunta[1] == 1:
                if not apufunktiot.solmun_naapuriin_voi_kulkea((
                    kasiteltava_solmu[0], kasiteltava_solmu[1]-1
                    ), self.kartta):
                    if apufunktiot.solmun_naapuriin_voi_kulkea((
                            kasiteltava_solmu[0]+suunta[0], kasiteltava_solmu[1]-1
                            ), self.kartta):
                        naapurit.append((kasiteltava_solmu[0]+suunta[0], kasiteltava_solmu[1]-1))

                if not apufunktiot.solmun_naapuriin_voi_kulkea((
                    kasiteltava_solmu[0]-1, kasiteltava_solmu[1]
                    ), self.kartta):
                    if apufunktiot.solmun_naapuriin_voi_kulkea((
                            kasiteltava_solmu[0]-1, kasiteltava_solmu[1]+suunta[1]
                            ), self.kartta):
                        naapurit.append((kasiteltava_solmu[0]-1, kasiteltava_solmu[1]+suunta[1]))
        return naapurit
