# Testausdokumentti
## Kattavuusraportti yksikkötesteistä
![testikattavuus](https://github.com/henriimmonen/shortestroute/blob/main/dokumentaatio/kuvat/testikattavuus_lopullinen.png)

### Dijkstran algoritmi
Algoritmin toimintaa on testattu kurssin aikana niin automatisoiduin yksikkötestein, kuin manuaalisesti. Yksikkötestit keskittyvät funktioiden toiminnan varmistamiseen, sekä oikeiden solmujen ja reitin löytämiseen kolmella erilaisella kartalla. Lisäksi olen laskenut että reitti on todella lyhin mahdollinen pienillä kartoilla, sekä suuremmilla kartoilla tarkastellut reitin järkevyyttä ja lyhyyttä visuaalisesti.

### Jump Point Search
Kuten Dijkstran algoritmin kanssa, testausta on suoritettu runsaasti manuaalisesti sekä automatisoiduin yksikkötestein. Vertailua Dijkstran algoritmiin on tehty suuremmilla kartoilla visuaalisesti. Yksikkötestien kattavuus on pienempää kuin Dijkstran-algoritmissä, mutta tämä johtuu pääasiassa monista ehtolauseista, joita tarvitaan naapurien karsimiseen, sekä pakotettujen naapurien tunnistamiseen. Testeihin sisältyy muutama testi, jotka tarkistavat vertikaalisen ja horisontaalisen haun tunnistavan pakotetut naapurit, mutta aivan jokaista ehtolausetta en lähtenyt testaamaan vain testikattavuutta lisätäkseni.  

## Perustoiminnallisuuden testaaminen
Ohjelma tulostaa kartan ja kuljetun reitin molempien algoritmien kohdalla pienemmillä kartoilla. Suuremmilla kartoilla avataan kartta tekstieditoriin tarkasteltavaksi ennen lähtö- ja maalipisteiden valintaa, sekä tuloksena piirretyn reitin jälkeen.  

Testiohjelma vertailee molempien algoritmien reittien pituutta ja varmistaa kymmennellä eri reitillä, että reitti on todella yhtä pitkä molempien algoritmien tuottamana. Näitä ajoja suoritetaan kymmenen kappaletta per reitti, jotta varmistutaan ettei reitti muutu suorituskertojen välillä.  

## Suorituskyky
Testiohjelman toimintaan kuuluu myös ajallinen vertailu algoritmien välillä. Vertailu suoritetaan neljällä erilaisella reitillä sydney.map-kartassa. Jokainen reitti etsitään 100 kertaa ja lopuksi kulunut aika jaetaan sadalla, jotta saadaan keskiarvo. *** KUVA AIKAVERTAILUSTA ***
