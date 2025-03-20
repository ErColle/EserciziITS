
stringa.append(6)  # AGGIUNGE UN ELEMENTO ALLA FINE DELLA STRINGA

len(stringa)  # RESTITUISCE IL NUMERO DI CARATTERI NELLA STRINGA

stringa.pop()  # RIMUOVE E RESTITUISCE L'ULTIMO ELEMENTO DELLA STRING


#FORMATTAZIONE STRINGA

stringa.upper()  # CONVERTE LA STRINGA IN MAIUSCOLO

stringa.lower()  # CONVERTE LA STRINGA IN MINUSCOLO

stringa.capitalize()  # CONVERTE IL PRIMO CARATTERE IN MAIUSCOLO E GLI ALTRI IN MINUSCOLO

stringa.title()  # CONVERTE IN MAIUSCOLO IL PRIMO CARATTERE DI OGNI PAROLA

stringa.strip()  # RIMUOVE SPAZI INIZIALI E FINALI DALLA STRINGA

stringa.lstrip()  # RIMUOVE GLI SPAZI SOLO A SINISTRA

stringa.rstrip()  # RIMUOVE GLI SPAZI SOLO A DESTRA



stringa.replace("vecchio", "nuovo")  # SOSTITUISCE TUTTE LE OCCORRENZE DI "vecchio" CON "nuovo"

stringa.split("separatore")  # DIVIDE LA STRINGA IN UNA LISTA USANDO "separatore"

stringa.rsplit("separatore", n)  # DIVIDE LA STRINGA DA DESTRA AL MASSIMO n VOLTE

stringa.join(lista)  # UNISCE GLI ELEMENTI DELLA LISTA IN UNA STRINGA USANDO "stringa" COME SEPARATORE

stringa.find("A")  # RESTITUISCE POSIZIONE DELLA DELLA PRIMA "A" NELLA STRINGA (-1 SE NON TROVATA)

stringa.rfind("sottostringa")  # RESTITUISCE L'INDICE DELL'ULTIMA OCCORRENZA DI "sottostringa" (-1 SE NON TROVATA)

stringa.index("sottostringa")  # COME find(), MA GENERA UN ERRORE SE NON TROVATA

stringa.rindex("sottostringa")  # COME rfind(), MA GENERA UN ERRORE SE NON TROVATA

stringa.startswith("prefisso")  # RESTITUISCE True SE LA STRINGA INIZIA CON "prefisso", ALTRIMENTI False

stringa.endswith("suffisso")  # RESTITUISCE True SE LA STRINGA FINISCE CON "suffisso", ALTRIMENTI False

stringa.count("sottostringa")  # CONTA QUANTE VOLTE "sottostringa" APPARE NELLA STRINGA

stringa.center(lunghezza, "carattere")  # CENTRA LA STRINGA IN UNA NUOVA STRINGA DI LUNGHEZZA "lunghezza", RIEMPITA CON "carattere"

stringa.ljust(lunghezza, "carattere")  # GIUSTIFICA A SINISTRA RIEMPIENDO FINO A "lunghezza" CON "carattere"

stringa.rjust(lunghezza, "carattere")  # GIUSTIFICA A DESTRA RIEMPIENDO FINO A "lunghezza" CON "carattere"

stringa.zfill(lunghezza)  # RIEMPIE A SINISTRA CON ZERI FINO A RAGGIUNGERE "lunghezza"

stringa.isdigit()  # RESTITUISCE True SE TUTTI I CARATTERI SONO CIFRE, ALTRIMENTI False

stringa.isalpha()  # RESTITUISCE True SE TUTTI I CARATTERI SONO LETTERE, ALTRIMENTI False

stringa.isalnum()  # RESTITUISCE True SE TUTTI I CARATTERI SONO LETTERE O NUMERI, ALTRIMENTI False

stringa.isspace()  # RESTITUISCE True SE LA STRINGA CONTIENE SOLO SPAZI, ALTRIMENTI False

stringa.islower()  # RESTITUISCE True SE TUTTI I CARATTERI SONO MINUSCOLI, ALTRIMENTI False

stringa.isupper()  # RESTITUISCE True SE TUTTI I CARATTERI SONO MAIUSCOLI, ALTRIMENTI False

stringa.istitle()  # RESTITUISCE True SE OGNI PAROLA HA IL PRIMO CARATTERE MAIUSCOLO, ALTRIMENTI False

stringa.swapcase()  # INVERTE MAIUSCOLE E MINUSCOLE NELLA STRINGA







