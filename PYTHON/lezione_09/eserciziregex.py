import re

# 1. Riconoscere numeri
# Obiettivo: Definire una RegEx che riconosca solo stringhe composte da cifre.

text = "AB12CD34"

""" if re.match(r"^\d+$", text):
    print("parola composta da cifre") """

# Esercizio 1.1: Scrivi una RegEx che riconosca un numero intero positivo (es. 123, 98765).

""" if re.match(r"^\d+$", text):
    print("Numero intero positivo") """

# Esercizio 1.2: Modifica la RegEx per accettare anche numeri negativi (es. -45, -1000, 0).

""" if re.match(r"^-?\d+$", text):
    print("numero accettato") """

# 2. Riconoscere parole
# Obiettivo: Lavorare con lettere e lunghezze di stringhe.

# Esercizio 2.1: Scrivi una RegEx che riconosca una parola composta solo da lettere minuscole.

""" if re.match(r"^[a-z]+$", text):
    print("solo lettere minuscole")
 """
# Esercizio 2.2: Adatta la RegEx per accettare parole con lettere maiuscole e minuscole.

""" if re.match(r"^[a-zA-z]+$", text):
    print("lettere maiuscole e minuscole") """
    
# Esercizio 2.3: Modifica la RegEx per accettare parole lunghe da 5 a 10 caratteri.

""" if re.match(r"^[a-zA-Z]{5,10}$", text):
    print("da 5 a 10 caratteri")
 """
# 3. Email semplici
# Obiettivo: Definire pattern per email.

# Esercizio 3.1: Scrivi una RegEx che riconosca email del tipo nome@dominio.com.

""" if re.match(r"^\S+@+\S+.+\S", text):
    print("email") """

# Esercizio 3.2: Estendi la RegEx per accettare anche domini con più estensioni, es. nome@dominio.co.uk.

""" if re.match(r"^\S+@\S+.\S+?\S", text):
    print("email") ?????
 """
# 4. CAP e codici
# Obiettivo: Lavorare con lunghezze fisse e caratteri misti.

# Esercizio 4.1: Definisci una RegEx per un CAP italiano (esattamente 5 cifre).

""" if re.match(r"^\d{5}", text):
    print("CAP") """

# Esercizio 4.2: Scrivi una RegEx che riconosca un codice fiscale italiano semplificato: 6 lettere, 2 numeri, 1 lettera, 2 numeri.


""" if re.match(r"[A-Z]{6}\d{2}[A-Z]\d{2}", text):
    print("CF") """

# 5. Riconoscere date
# Obiettivo: Lavorare con formati numerici separati da caratteri speciali.

# Esercizio 5.1: Scrivi una RegEx che riconosca una data nel formato gg/mm/aaaa (es. 09/04/2025).

""" if re.match(r"\d{2}+/\d{2}/+\d{4}", text):
    print("data") """

# Esercizio 5.2: Adatta la RegEx per accettare anche il formato gg-mm-aaaa.

""" if re.match(r"\d{2}+[/-]\d{2}[/-]\d{4}", text):
    print("data") """

# 6. Codici personalizzati
# Obiettivo: Unire lettere, numeri e caratteri speciali.

# Esercizio 6.1: Scrivi una RegEx per identificare un codice prodotto nel formato PROD-1234-XY.

""" if re.match(r"^[A-Z]{4}-\d{4}-[A-Z]{2}", text):
    print("true") """

# Esercizio 6.2: Crea una RegEx per un ID alfanumerico di esattamente 8 caratteri, che può contenere lettere maiuscole e numeri (es. AB12CD34).

""" if re.match(r"^[a-zA-Z0-9]{8}", text):
    print("true") """

# Esercizi – Comprensione di RegEx
# Data la RegEx, occorre interpretarla.

# Esercizio 7.1: Cosa fa questa RegEx? ^[A-Z][a-z]{2,}$
# Esercizio 7.2: Quali stringhe sono accettate da \d{3}-\d{2}-\d{4}?

""" nnn-nn-nnnn
 """
# Esercizio 7.3: Qual è l’effetto del simbolo ? in questa RegEx: colou?r
# Bonus – Errori comuni
# Obiettivo: Trovare errori in RegEx sbagliate.

# Esercizio 8.1: Qual è l’errore nella RegEx ^\d{2,5}?$ se voglio matchare da 2 a 5 cifre?
# Esercizio 8.2: La RegEx [A-z] funziona per lettere? Perché può essere rischiosa?