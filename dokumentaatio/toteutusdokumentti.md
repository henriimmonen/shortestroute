# Toteutusdokumentti
Tämän dokumentin tarkoituksena on selkeyttää toteutetun ohjelman rakennetta ja toimintaa.  

## Ohjelman rakenne
Ohjelman juuressa ovat kansiot src, dokumentaatio ja htmlcov. Näistä src sisältää ohjelmakoodin testeineen ja testiohjelman, dokumentaatio ohjelmaan liittyvän kirjallisen osuuden ja htmlcov coverage-työkalun tuottaman testikattavuusdatan. Lisäksi juuressa ovat kartat test.map ja sydney.map, joita on käytetty ohjelman kehityksessä ja testauksessa.  

Src-kansiossa ovat ohjelman toiminnallisuuden muodostavat tiedostot: index.py, ui.py, dijkstra.py, jps.py ja apufunktiot.py.  

## Saavutetut aika- ja tilavaatimukset
Tässä toteutuksessa Dijkstran- sekä Jump Point Search-algoritmin tilavaativuus on O(v), sillä molemmat käyttävät apufunktiot-moduulin ```kaarilista```-metodia joka käy läpi jokaisen verkon solmun ja tarkistaa sen naapurit.  

## Suorituskyky ja O-analyysivertailu

## Puutteet ja kehitysehdotukset
Jps-algoritmin tilavaativuus olisi mahdollista tiivistää samaan kuin sen aikavaativuus, sillä verkon läpikäyminen etukäteen ei ole välttämätöntä tässä toteutuksessa. Naapureiden tarkistamiseen on jo olemassa hyvät metodit, joten käsittelyssä olevan solmun naapurit voisi tarkistaa ajonaikaisesti. Tämä jäi kuitenkin toteuttamatta kurssin laajuuden puitteissa.  
### Lähteet
