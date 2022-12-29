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
![algoritmien vertailu](https://github.com/henriimmonen/shortestroute/blob/main/dokumentaatio/kuvat/tilasto.png)  
Testiohjelman toimintaan kuuluu myös ajallinen- ja käytyjen solmujen määrällinen vertailu. Vertailu suoritetaan neljällä erilaisella reitillä sydney.map-kartassa. Jokainen reitti etsitään 100 kertaa ja lopuksi kulunut aika jaetaan sadalla, jotta saadaan keskiarvo. Vierailtujen solmujen määrää vertaillessa ajetaan reitti 10 kertaa ja jaetaan tulos kymmenellä. Kun testiohjelma oli valmis, ajoin sen läpi ja poimin tiedot taulukkoon. Tein myös testiajoja varsinaisella ohjelmalla ja vertasin saatuja tuloksia testiohjelman keskiarvoihin nähdäkseni pitävätkö ne hyvin paikkaansa. Vaihtelua oli jonkin verran, joten keskiarvo ainakin suoritusajasta oli perusteltu. Tulosten perusteella JPS-algoritmi suoriutui huomattavasti nopeammin ja vieraili huomattavasti pienemmässä määrässä solmuja suorituksen aikana. Ajallinen ero algoritmien välillä kuitenkin pienenee lyhyemmillä matkoilla ja voi jopa kääntyä Dijkstran eduksi. Tämä tapahtuu luultavasti siksi, että Dijkstan on nopeampi käydä läpi kaarilistaa, kun taas JPS:llä aikaa kuluu pakotettujen naapureiden ja hyppysolmujen evaluointiin. JPS:n toteutus ilman jokaisen solmun läpikäyntiä ennakkoon nopeuttaisi toimintaa luultavasti riittävästi myös lyhyemmillä matkoilla.
