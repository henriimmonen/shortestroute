def alusta_kartta(osoite):
    """Alustetaan matriisikartta tiedostosta

    Args:
        osoite: suhteellinen osoite, josta karttatiedosto luetaan

    Returns:
        matriisi: kartta
    """
    kartta = []
    with open(osoite, 'r', encoding="utf-8") as lukija:
        for rivi in lukija:
            if rivi[0] == '.' or rivi[0] == '@':
                kartta.append(rivi[0:-1])
    lukija.close()
    return kartta

def kaarilista(kartta):
    """Luodaan kaarilista annetusta karttapohjasta

    Args:
        kartta: matriisikartta

    Returns:
        verkko: kaarilista
    """
    verkko = []
    for rivi in enumerate(kartta):
        for sarake in enumerate(kartta[rivi[0]]):
            solmun_naapurit = tarkista_naapurit((rivi[0], sarake[0]), kartta)
            verkko.append(solmun_naapurit)
    return verkko

def tarkista_naapurit(solmu, kartta):
    """Tarkistetaan annetun solmun kaaret

    Args:
        solmu: tuple-muotoinen koordinaatti
        kartta : matriisikartta

    Returns:
        solmun_naapurit: lista solmun kaarista
    """
    solmun_naapurit = []
    for naapuri in [(solmu[0]-1, solmu[1]-1), (solmu[0]-1, solmu[1]), (solmu[0]-1, solmu[1]+1),
                    (solmu[0], solmu[1]-1), (solmu[0], solmu[1]+1), (solmu[0]+1, solmu[1]-1),
                    (solmu[0]+1, solmu[1]), (solmu[0]+1, solmu[1]+1)]:

        if verkon_sisalla(naapuri, kartta):
            if solmun_naapuriin_voi_kulkea(naapuri, kartta):
                solmun_naapurit.append(naapuri)
    return solmun_naapurit

def verkon_sisalla(solmu, kartta):
    """Tarkistetaan onko annettu solmu matriisin sisällä

    Args:
        solmu: tuple-muotoinen koordinaatti
        kartta: matriisikartta

    Returns:
        Boolean-arvo: True, jos solmu on matriisin sisällä, muuten False
    """
    if solmu[0] >= 0 and solmu[0] < len(kartta):
        if solmu[1] >= 0 and solmu[1] < len(kartta[0]):
            return True
    return False

def solmun_naapuriin_voi_kulkea(naapuri, kartta):
    """Tarkistetaan onko annettuun solmuun kaarta

    Args:
        naapuri: tuple-muotoinen koordinaatti
        kartta: matriisikartta

    Returns:
        Boolean-arvo: True, jos annettuun solmuun on kaari, muuten False
    """
    if verkon_sisalla(naapuri, kartta) and kartta[naapuri[0]][naapuri[1]] == '.':
        return True
    return False

def piirra_kartalle(alkuperainen_kartta, kuljettu_reitti):
    for rivi in range(len(alkuperainen_kartta)):
        for sarake in range(len(alkuperainen_kartta[0])):
            if (rivi, sarake) in kuljettu_reitti:
                alkuperainen_kartta[rivi] = vaihda_merkki(sarake, alkuperainen_kartta[rivi])
    return alkuperainen_kartta

def vaihda_merkki(sarake, kartan_rivi):
    sarakkeen_loppu = sarake+1
    if sarake+1 >= len(kartan_rivi):
        sarakkeen_loppu = sarake

    uusi_rivi = kartan_rivi[:sarake] + '*' + kartan_rivi[sarakkeen_loppu:]
    return uusi_rivi