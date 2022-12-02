# Viikon tapahtumat
Olen käyttänyt runsaahkosti aikaa jps-algoritmin refaktorointiin, mutta en saanut työtä aivan loppuun saakka. En ollut aivan varma algoritmin toiminnasta, joten kävin sitä läpi vielä suurennuslasin kanssa. Esimerkiksi naapurien karsimista (pruning) ei ollut aiemmin toteutettu, mutta nyt se on. Metodi jäi kuitenkin keskeneräiseksi sillä tavalla, että se on karkeasti toteutettu ja liian pitkä. Tässä löytyy siis vielä työnsarkaa. Tämän metodin kohdalla on tarkoituksena poistaa suurin osa if-lauseista ja käyttää yhtä koodiblokkia tarkastamaan esteen ja mahdollisen pakotetun naapurin olemassaolo.  

Algoritmin hiomisen lisäksi loin Dijkstran ja Jump point searchin tuottamien kulkureittien visualisoinnin. Tällä hetkellä ohjelma piirtää kuljetun reitin komentoriville, mutta tämä ei tietenkään ole kestävä ratkaisu isompien karttojen kohdalla. Tämän vuoksi ohjelmaan on tarkoitus lisätä mahdollisuus piirtää kartta tiedostoon.  

Käyttöliittymä on edelleen kesken, mutta luulen että sen kehitykseen jää paremmin aikaa projektin loppupuolella, kun jps:n hiomiseen ei enää kulu aikaa.  

Vertaisarvioinnin tekeminen oli mukavaa, sillä toisten kirjoittamaa koodia tulee luettua harmittavan vähän.  
## Seuraavan viikon tehtävät
Otan käyttöliittymän kehittämisen työn alle ja aloitan algoritmien vertailun mahdollistamisen muullakin kuin aikapohjaisella vertailulla.  

### Tuntimäärä
Työtunteja kertyi 15h.
