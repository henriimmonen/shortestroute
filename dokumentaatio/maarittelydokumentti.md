# Projektin määritelmä
Projektin aiheena on kahden pisteen välisen lyhimmän reitin löytäminen käyttäen JPS (Jump Point Search) algoritmia. Tämän algoritmin toimintaa verrataan sitten Dijkstran algoritmin toimintaan.  

Projekti toteutetaan Python-ohjelmointikielellä.  

## Ongelman määrittely
Tarkoituksena on toteuttaa reitinhaku kahdella eri algoritmilla. Karttapohjana käytän [Moving AI Lab:n](https://www.movingai.com/benchmarks/grids.html) karttaa, sillä ne ovat helposti saatavissa ASCII muodossa.  

Ohjelma tulee ottamaan syötteenä kaksi pistettä, joiden välisen lyhimmän reitin se laskee ja antaa ajallisen vertailun näiden kahden algoritmin toiminnasta. Ohjelma tulee lisäksi näyttämään kyseisen reitin visuaalisesti.

Kyseisen aiheen valintaan motivoi ohjelmistotekniikan kurssilla toteuttamani Pacman-pelin klooni, jossa käytin haamujen liikkumisen ohjelmointiin A* algoritmia. JPS on A*:ä optimoidumpi algoritmi, joten sen toiminta alkoi kiinnostamaan.    

## Lisätiedot
Projektin dokumentaatio tulee olemaan suomenkielinen.  
Työn tekijä on tietojenkäsittelytieteen kandidaatin tutkintoa suorittava opiskelija. 

### Lähteet
[Jump Point Search](http://users.cecs.anu.edu.au/~dharabor/data/papers/harabor-grastien-aaai11.pdf)

