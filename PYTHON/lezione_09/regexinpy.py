import re

# 1. Verifica se una stringa è un numero intero
# Scrivi una funzione is_integer(s) che restituisce True se la stringa è un numero intero (positivo o negativo), False altrimenti.

# Esempio:

# is_integer("123")      # True
# is_integer("-456")     # True
# is_integer("12.3")     # False

# """ def is_integer(stringa:str):
#     if re.match(r"^-?\d+$", stringa):
#         print("True")
#     else: 
#         print("False")
        
# is_integer("123.1") """

# 2. Trova tutte le email in un testo
# Scrivi una funzione extract_emails(text) che prende un testo e restituisce tutte le email trovate.

# Esempio:

# text = "Contattaci a info@azienda.com oppure support@help.org"
# extract_emails(text)  # ['info@azienda.com', 'support@help.org']

# """ def extrct_emails(text:str):
#     emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
#     print(emails)
    
# text = "Contattaci a info@azienda.com oppure support@help.org"
# extrct_emails(text) """


# 3. Sostituisci tutti i numeri con ‘###’
# Scrivi una funzione mask_numbers(text) che sostituisce tutte le sequenze di cifre con ###.

# Esempio:

# text = "Il codice è 12345 e la data è 2025."
# mask_numbers(text)  # "Il codice è ### e la data è ###."

# def mask_numbers(text):
#     print(re.sub(r"\d", "#", text))
    
# text = "Il codice è 12345 e la data è 2025."
# mask_numbers(text)


# 4. Verifica un CAP
# Scrivi una funzione is_valid_cap(cap) che restituisce True se il CAP è valido (5 cifre), False altrimenti.

# Esempio:

# is_valid_cap("70124")   # True
# is_valid_cap("A0123")   # False

# def is_valid_cap(cap):
#     if re.match(r"\d{5}$", cap):
#         print("True")
#     else:
#         print("False")

# is_valid_cap("70121") 


# 5. Estrai tutte le date nel formato gg/mm/aaaa
# Scrivi una funzione find_dates(text) che trova tutte le date in formato italiano (dd/mm/yyyy) in un testo.

# Esempio:

# text = "Le date importanti sono 09/04/2025 e 15/08/2023."
# find_dates(text)  # ['09/04/2025', '15/08/2023']

# def find_dates(text):
#     dates = re.findall(r"\d{2}+/\d{2}/+\d{4}", text)
#     print(dates)

# text = "Le date importanti sono 09/04/2025 e 15/08/2023."
# find_dates(text)



# 6. Verifica un codice prodotto
# Scrivi una funzione check_product_code(code) che verifica se il codice è nel formato PROD-1234-AB.

# Esempio:

# check_product_code("PROD-9876-ZX")  # True
# check_product_code("PROD-99-ZX")    # False

# def check_product_code(code):
#     if re.findall(r"^[A-Z]{4}-\d{4}-[A-Z]{2}", code):
#         print(True)
#     else:
#         print(False)

# check_product_code("PROD-9876-ZX")  # True
# check_product_code("PROD-99-ZX")    # False

# 7. Verifica un nome proprio
# Scrivi una funzione is_valid_name(name) che controlla se la stringa inizia con una lettera maiuscola seguita da almeno due lettere minuscole.

# Esempio:

# is_valid_name("Marco")    # True
# is_valid_name("marco")    # False
# is_valid_name("Ma")       # False

def is_valid_name(name):
    dates = re.match(r"\d{2}+/\d{2}/+\d{4}", text)
    print(dates)

text = "Le date importanti sono 09/04/2025 e 15/08/2023."
find_dates(text)


# 8. Trova parole con lettere maiuscole e numeri
# Scrivi una funzione find_codes(text) che trova tutte le parole lunghe 8 caratteri, con lettere maiuscole e/o numeri.

# Esempio:

# text = "I codici sono AB12CD34 e 12345678 e XYZZYZZZ"
# find_codes(text)  # ['AB12CD34', '12345678', 'XYZZYZZZ']

# def find_codes(text):
#     codes = re.findall(r"\b[A-Z0-9]{8}\b", text)
#     print(codes)

# text = "I codici sono AB12CD34 e 12345678 e XYZZYZZZ"
# find_codes(text)

# 9. Trova tutti i codici fiscali in un testo
# Scrivi una funzione find_fc(text) che trova tutti i codici fiscali all'interno di un testo.

# Esempio:

# testo = "Mario Rossi CF: RSSMRA85M01H501Z, mentre Maria Bianchi ha il CF BNCMRA85T41H501Y."
# codici = find_fc(testo) # ['RSSMRA85M01H501Z', 'BNCMRA85T41H501Y']

# def find_fc(testo):
#     codici = re.findall(r"[A-Z]{6}\d{2}[A-Z]\d{2}", testo)
#     print(codici)

# testo = "Mario Rossi CF: RSSMRA85M01H501Z, mentre Maria Bianchi ha il CF BNCMRA85T41H501Y."
# codici = find_fc(testo) # ['RSSMRA85M01H501Z', 'BNCMRA85T41H501Y']