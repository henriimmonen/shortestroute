# Käyttöohje
Kloonaa projekti Githubista itsellesi.  

Tämä jälkeen siirry komentorivillä kyseisen projektin juureen ja aja seuraavat komennot:  
`poetry shell`  
`poetry install`  

Jonka jälkeen ohjelma käynnistetään komennolla:  
`poetry src/index.py`  

Juuressa toimivia komentoja ovat:  
`pytest src` (Testien ajaminen)  
`pylint src` (Pylint-tarkistusten ajaminen)  
`coverage run --branch -m pytest; coverage html`  
(Ajaa testit ja kerää haaraumakattavuuden juuren kansioon 'htmlcov')

