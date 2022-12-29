# Käyttöohje
Kloonaa projekti Githubista itsellesi.  

Tämä jälkeen siirry komentorivillä kyseisen projektin juureen ja aja seuraavat komennot:  
`poetry shell`  
`poetry install`  

Jonka jälkeen ohjelma käynnistetään komennolla:  
`python3 src/index.py`  

Juuressa toimivia komentoja ovat:  
- `pytest src` (Testien ajaminen)  
- `pylint src` (Pylint-tarkistusten ajaminen)  
- `coverage run --branch -m pytest; coverage html`  
(Ajaa testit ja kerää haaraumakattavuuden juuren kansioon 'htmlcov')  
- `python3 src/algoritmien_vertilu.py` (Ajaa testiohjelman)

