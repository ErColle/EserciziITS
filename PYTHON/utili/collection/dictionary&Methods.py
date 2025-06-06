mio_dizionario = {
    "nome": "Mario",
    "età": 30,
    "città": "Roma"
}

# Accesso ai valori tramite la chiave
print(mio_dizionario["nome"])  # Stampa: Mario
print(mio_dizionario.get("età"))  # Stampa: 30


dizionario["chiave"] = valore  # ASSEGNA UN VALORE A UNA CHIAVE (AGGIUNGE O MODIFICA)

dizionario.get("chiave", valore_default)  # RESTITUISCE IL VALORE DI UNA CHIAVE, SE NON ESISTE RESTITUISCE IL VALORE DI DEFAULT

del dizionario["chiave"]  # ELIMINA UNA CHIAVE DAL DIZIONARIO

dizionario.pop("chiave", valore_default)  # RIMUOVE UNA CHIAVE E RESTITUISCE IL SUO VALORE, SE NON ESISTE RESTITUISCE IL VALORE DI DEFAULT

dizionario.clear()  # RIMUOVE TUTTI GLI ELEMENTI DAL DIZIONARIO

dizionario.keys()  # RESTITUISCE UNA VISTA DI TUTTE LE CHIAVI DEL DIZIONARIO

dizionario.values()  # RESTITUISCE UNA VISTA DI TUTTI I VALORI DEL DIZIONARIO

dizionario.items()  # RESTITUISCE UNA VISTA DI TUTTE LE COPPIE (CHIAVE, VALORE) DEL DIZIONARIO

dizionario.update(altro_dizionario)  # AGGIORNA IL DIZIONARIO CON LE CHIAVI E VALORI DI UN ALTRO DIZIONARIO

dizionario | altro_dizionario  # UNISCE DUE DIZIONARI (PYTHON 3.9+), IN CASO DI CHIAVI DUPLICATE PREVALE IL SECONDO DIZIONARIO

len(dizionario)  # RESTITUISCE IL NUMERO DI ELEMENTI NEL DIZIONARIO

"chiave" in dizionario  # CONTROLLA SE UNA CHIAVE È PRESENTE NEL DIZIONARIO (RESTITUISCE True O False)

dizionario.setdefault("chiave", valore_default)  # RESTITUISCE IL VALORE DELLA CHIAVE, SE NON ESISTE LA AGGIUNGE CON IL VALORE DI DEFAULT

dizionario.copy()  # RESTITUISCE UNA COPIA SUPERFICIALE DEL DIZIONARIO

dizionario.popitem()  # RIMUOVE E RESTITUISCE L'ULTIMO ELEMENTO INSERITO
