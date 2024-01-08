Algoritmid ja andmestruktuurid  kursuse projekt - Muusikaloend

Muusikaloendi projekti eesmärk on luua muusika esitusloend, mis võimaldab kasutajal kuulata muusikat. Vastavalt kasutaja harjumustele soovitatakse uusi lugusid kuulamiseks ning ei pakuta enam vahelejäetud muusikat.

Koodi kirjutamise põhimõtted:
- muutujad, funktsioonid ja muu selline kirjutatakse eesti keeles
- koodi kirjutamiseks kasutatakse Python süntaksit
- koodi kommenteeritakse eesti keeles ja enne igat lõiku koodis lisatakse lühike kirjeldus mis järgnevas osas toimub
  
Enne koodi kasutamist lae alla:
- Pythoni library openpyxl ja pandas, et kasutada xlsx faili lugemise funktsionaalsust (pip install openpyxl)
- Pythoni library xlsx writer, et kirjutada uus xlsx fail (pip install XlsxWriter)
- Exceli fail nimega 'andmebaas.xlsx' käesolevast repositoryst

Koodi töötamise kirjeldus (Content Based Filtering)
1. Kasutaja logib sisse oma kontosse esimesest aknast
2. Avaneb uus aken, kus on näha artisti ja laulu nimi ning saab nupule vajutusega laulu märkida meeldivaks (nupuga LIKE) või kuulata järgmist lugu (nupuga SKIP), mis ei salvesta lugu kasutaja meeldivate sekka.
3. Esimese meeldivaks märgitud loo järgi hakkab soovitusalgoritm tööle.
4. Algoritmi tööpõhimõttel soovitatakse esimesena sama artisti järgmisi lugusid, seejärel samast žanrist ja viimasena samal aastal välja antud lugusid. 
5. igale loole failis lisatakse kaalupunktid
6. kood sorteerib lood vastavalt kaalupunktidele
7. kirjutab uude faili nimega andmebaas_sorteeritud
