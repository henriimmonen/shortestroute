# Testausdokumentti
## Kattavuusraportti yksikkötesteistä
![testikattavuus](https://github.com/henriimmonen/shortestroute/blob/main/dokumentaatio/kuvat/coverage.png)

### Dijkstran algoritmi
Tällä hetkellä Dijkstran toiminta tapahtuu muutamassa eri funktiossa. Näitä voisi kuitenkin refaktoroida kattavampaa testausta ajatellen. Algoritmia kirjoittaessa testausta on suoritettu pääasiallisesti manuaalisesti, mutta ohjelman laajentamista ajatellen testausta (erityisesti reitin pituuteen ja sen vastaavuuteen jps:n tuottaman reitin kanssa) tulisi automatisoida.  

### Jump Point Search
Kuten Dijkstran algoritmin kanssa, testausta on suoritettu runsaasti manuaalisesti. Suorituskykyä olisi kuitenkin hyvä testata vielä kattavammin kuin
 pelkän ajan perusteella.

## Perustoiminnallisuuden testaaminen
Ohjelma tulostaa terminaaliin kuljetun reitin, jonka perusteella on mahdollista tarkastella algoritmien toimintaa silmämääräisesti. Tämä tulee kuitenkin toteuttamaan myöhemmin niin, että kuljettu reitti myös piirretään tiedostoon ja näytetään käyttäjälle.

## Suorituskyky
Tällä hetkellä algoritmien toimintaa verrataan ajallisesti. Myöhemmässä vaiheessa toteutetaan vertailua muilla parametreillä.
