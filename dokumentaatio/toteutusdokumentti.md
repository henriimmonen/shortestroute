# Toteutusdokumentti
Tämän dokumentin tarkoituksena on selkeyttää toteutetun ohjelman rakennetta ja toimintaa.  

## Ohjelman rakenne
Ohjelman juuressa ovat kansiot src, dokumentaatio ja htmlcov. Näistä src sisältää ohjelmakoodin testeineen ja testiohjelman, dokumentaatio ohjelmaan liittyvän kirjallisen osuuden ja htmlcov coverage-työkalun tuottaman testikattavuusdatan. Lisäksi juuressa ovat kartat test.map ja sydney.map, joita on käytetty ohjelman kehityksessä ja testauksessa.  

Src-kansiossa ovat ohjelman toiminnallisuuden muodostavat tiedostot: index.py, ui.py, dijkstra.py, jps.py ja apufunktiot.py sekä testiohjelma algoritmien_vertailu.py.  

## Saavutetut aika- ja tilavaatimukset
Dijkstran algoritmi on toteutettu käyttäen valmista keko-tietorakennetta. [Tällä sen aikavaativuus on O((|E| + |V|) log |V|)](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm). Jump point search algoritmilla toiminta on huomattavasti nopeampaa, mutta pahimmassa tapauksessa se noudattaa samaa aikavaativuutta, kuin Dijkstran algoritmi.

Tässä toteutuksessa Dijkstran- sekä Jump Point Search-algoritmin tilavaativuus on O(|V|), sillä molemmat käyttävät apufunktiot-moduulin kaarilista-metodia joka käy läpi jokaisen verkon solmun.

## Suorituskyky ja O-analyysivertailu
Algoritmien O-analyysien tulokset ovat samanlaisia, mutta testiohjelmalla tarkasteltuna JPS:n toiminta vaikuttaa huomattavasti tehokkaammalta. Ajallisesti JPS suoriutui pidemmillä matkoilla lähes puolet nopeammin, mutta lyhyellä matkalla aikaa kului 0.3 ms pidempään. Jokaisella reitillä JPS tutki huomattavasti pienemmän osuuden solmuja kuin Dijkstra (kts. testausdokumentti). 

## Puutteet ja kehitysehdotukset
Jps-algoritmin tilavaativuus olisi mahdollista tiivistää, sillä verkon läpikäyminen etukäteen ei ole välttämätöntä tässä toteutuksessa. Naapureiden tarkistamiseen on jo olemassa hyvät metodit, joten käsittelyssä olevan solmun naapurit voisi tarkistaa ajonaikaisesti. Tämä jäi kuitenkin toteuttamatta kurssin laajuuden puitteissa.  

### Lähteet
https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm  
https://harablog.wordpress.com/2011/09/07/jump-point-search/  
