Algoritmid ja andmestruktuurid  kursuse projekt- Muusikaloend

Muusikaloendi projekti eesmärk on luua muusika esitusloend, mis võimaldab kasutajal kuulata muusikat. Vastavalt kasutaja harjumustele soovitatakse uusi lugusid kuulamiseks ning ei pakuta enam vahelejäetud muusikat.

Koodi kirjutamise põhimõtted:
- muutujad, funktsioonid ja muu selline kirjutatakse eesti keeles
- koodi kirjutamiseks kasutatakse Python süntaksit
- koodi kommenteeritakse eesti keeles ja enne igat lõiku koodis lisatakse lühike kirjeldus mis järgnevas osas toimub
  
Koodi kasutamise juhend:
- enne koodi kasutamist tuleb alla laadida Pythoni library openpyxl, et kasutada xlsx faili lugemise funktsionaalsust
- enne koodi kasutamist tuleb alla laadida Exceli fail käesolevast repositoryst

Koodi töötamise kirjeldus (Content Based Filtering)
1. kasutaja sisestab loo nime 
2. kood käivitub, otsitakse esimesena sama artisti lugusid, seejärel saadud tulemustest samast zanrist lugusid jne
3. igale loole failis lisatakse kaalupunktid
5. kood sorteerib lood vastavalt kaalupunktidele
6. kirjutab uuele lehele excelis
