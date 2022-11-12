# Viikon tapahtumat
Tällä viikolla aloitin projektin ydintoiminnallisuuden kirjoittamisen. Ohjelma ottaa tällä hetkellä kovakoodattuna syötteen (kartta) ja muodostaa tästä ensin matriisin ja sen jälkeen kaarilistan.  

Tätä kaarilistaa käyttäen leveyshaku hakee lyhyimmän reitin haluttuun ruutuun. Myös alku- ja loppuruutu ovat kovakoodattuja, mutta ne tulevat olemaan määriteltävissä komentoriviltä.   

Ohjelmaan on lisätty automatisoitu yksikkötestaus, codecov-konfiguroitu testikattavuus ja pylint-tarkistukset. Docstring-kommentointi on tehty tällä hetkellä valmiina olevaan osuuteen.

Jouduin refaktoroimaan koodia jonkin verran yksikkötestejä kirjoittaessani ja pylint-virheitä korjaillessani. Nyt koodi on mielestäni järkevästi jaettu eri luokkiin ja apufunktioihin.

## Seuraavan viikon tehtävät
Alkavalla viikolla aloitan JPS-haun kirjoittamisen, sekä lisään karttaan piirtämisen kuljetun reitin havainnollistamiseksi. 

### Tuntimäärä
Tällä viikolla käytin n. 17h projektin tekemiseen.
