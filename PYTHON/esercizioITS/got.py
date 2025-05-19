""" Test classe Room:
ID: Room1, Atteso: Room1
Piano: 1, Atteso: 1
Posti: 15, Atteso: 15
Area: 30, Atteso: 30

Test di inizializzazione Building:
Nome: Test Building, Atteso: Test Building
Indirizzo: 123 Test St, Atteso: 123 Test St
Piani: (1, 10), Atteso: (1, 10)
Stanze iniziali: [], Atteso: []

Dopo aggiunta Room1:
Stanze: ['Room1'], Atteso: [Room1]

Dopo tentativo di aggiunta Room3 (piano non valido):
Stanze: ['Room1'], Atteso: [Room1]

Dopo tentativo di aggiunta duplicato Room1:
Stanze: ['Room1', 'Room1'], Atteso: [Room1]

Dopo aggiunta Room2:
Area totale: 100, Atteso: 70

Rappresentazione in stringa dell'edificio:
Nome Edificio: Test Building
Indirizzo Edificio: 123 Test St
Piani Edificio: (1, 10)
Stanze nell'edificio:
ID Stanza: Room1, Piano: 1, Posti: 15, Area: 30
ID Stanza: Room1, Piano: 1, Posti: 15, Area: 30
ID Stanza: Room2, Piano: 5, Posti: 20, Area: 40
Area totale dell'edificio: 100m2

Verifica finale: Stanze: ['Room1', 'Room1', 'Room2'], Atteso: ['Room1', 'Room2']
Verifica finale: Area totale: 100, Atteso: 70 """