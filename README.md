# Engeto_PA_3rd_project

Třetí projekt na Python Akademii od Engeta

### Popis projektu

Tento projekt slouží k extrahování výsledků z parlamentních voleb v roce 2017. Odkaz k prohlédnutí najdete [zde](https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ)).

### Instalace knihoven

Knihovny, které jsou použity v kódu jsou uloženy v souboru `requirements.txt`. Pro instalaci doporučuji použít nové virtuální prostředí a s nainstalovaným manažerem použít následovně:

<pre>$ pip3 --version                                       # overim verzi manažeru</pre>

<pre>$ pip3 install -r requirements.txt                     # nainstalujeme knihovny</pre>

### Spuštění projektu

Spuštění souboru election_scraper.py v rámci příkazového řádku požaduje dva povinné argumenty.

<pre>python3 Election_scraper.py 'odkaz-uzemniho-celku' 'vysledny-soubor'</pre>

Následně se vám stáhnou výsledky jako soubor s příponou `.csv` .

### Ukázka projektu

Výsledky hlasování pro okres Prostějov:
1. argument: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103
2. argument: vysledky_prostejov.csv

#### Spuštění programu:

<pre>python3 Election_scraper.py 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103' 'vysledky-prostejov.csv'</pre>

#### Průběh stahování:

STAHUJI DATA Z VYBRANEHO URL: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103

UKLADAM DO SOUBORU: vysledky_prostejov.csv

UKONCUJI Election_scraper

#### Částečný výstup:
code,location,registered,envelopes,valid,Občanská demokratická strana,Řád národa - Vlastenecká unie,CESTA ODPOVĚDNÉ SPOLEČNOSTI,......\
506761,Alojzov,205,145,144,29,0,0,9,0,5,17,4,1,1,0,0,18,0,5,32,0,0,6,0,0,1,1,15,0\
589268,Bedihošť,834,527,524,51,0,0,28,1,13,123,2,2,14,1,0,34,0,6,140,0,0,26,0,0,0,0,82,1\
589276,Bílovice-Lutotín,431,279,275,13,0,0,32,0,8,40,1,0,4,0,0,30,0,3,83,0,0,22,0,0,0,1,38,0\
589284,Biskupice,238,132,131,14,0,0,9,0,5,24,2,1,1,0,0,10,2,0,34,0,0,10,0,0,0,0,19,0\
589292,Bohuslavice,376,236,236,20,0,0,23,0,3,22,3,4,6,0,1,17,0,4,53,1,1,39,0,0,3,0,36,0\
...



Pro správné zobrazení v excelu doporučuji v import průvodci pro „file origin“ zadat „Unicode (UTF-8)“ a pro „delimiter“ označit “comma“.
