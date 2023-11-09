Algoritmid ja andmestruktuurid  kursuse projekt- Muusikaloend

Muusikaloendi projekti eesmärk on luua muusika esitusloend, mis võimaldab kasutajal kuulata muusikat. Vastavalt kasutaja harjumustele soovitatakse uusi lugusid kuulamiseks ning ei pakuta enam vahelejäetud muusikat.

Koodi kirjutamise põhimõtted:
- muutujad, funktsioonid ja muu selline kirjutatakse eesti keeles
- koodi kirjutamiseks kasutatakse Python süntaksit
  
Koodi kasutamise juhend:
- enne koodi kasutamist tuleb alla laadida Pythoni library openpyxl, et kasutada xlsx faili lugemise funktsionaalsust
- enne koodi kasutamist tuleb alla laadida Exceli fail käesolevast repositoryst

Koodi töötamise kirjeldus
1. kasutaja sisestab loo nime (kas siin on oluline kas lugu on listis olemas või ei?, sisestam peaks ka artisti ja zanri)
2. kood käivitub, otsitakse esimesena sama artisti lugusid, seejärel saadud tulemustest samast zanrist lugusid (kuidas käituda kui excelis on mitu samade omadustega lugu?)
3. kood sorteerib lood
4. kirjutab uuele lehele excelis
