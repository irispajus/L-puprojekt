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
1. Kasutaja logib sisse oma kontosse esimesest aknast
2. Avaneb uus aken, kus on näha artisti ja laulu nimi ning saab nupule vajutusega laulu "LIKE"-da või "SKIP"-da.
3. Esimese likedud laulu järgi hakkab soovitusalgoritm tööle.
4. kood käivitub, otsitakse esimesena sama artisti lugusid, seejärel saadud tulemustest samast zanrist lugusid jne
5. igale loole failis lisatakse kaalupunktid
6. kood sorteerib lood vastavalt kaalupunktidele
7. kirjutab uuele lehele excelis
