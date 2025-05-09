import json  # Importa il modulo json per leggere e scrivere file JSON

# Definisce il percorso del file JSON, la modalità di apertura e l'encoding
PATH: str = "PYTHON/lezione_14/config.json"
mode: str = "r"                                             # Modalità di apertura: 'r' = read (lettura)
encoding: str = "utf-8"                                     # Tipo di codifica dei caratteri

# Inizializza la variabile che conterrà i dati letti dal file
config = None

# Apre il file JSON in modalità lettura
with open(PATH, mode=mode, encoding=encoding) as file:
    config: dict = json.load(file)                          # Carica il contenuto del file come dizionario Python

# Aggiunge (o aggiorna) una nuova chiave nel dizionario
config["AGGIUNTA"] = "NUOVO"                                # Inserisce la chiave "AGGIUNTA" con valore "NUOVO"

# Apre di nuovo il file, questa volta in modalità scrittura ('w' sovrascrive il file)
with open(PATH, mode="w", encoding=encoding) as file:
    # Salva il dizionario aggiornato nel file, con indentazione per leggibilità
    json.dump(config, file, indent=4)

""" #Creazione file json

config: dict = { 
    "Persona": { 
        "name": "Mario", 
        "surname": "Rossi", 
        "age": 30, 
        "city": "Roma" 
    }
}

with open(PATH, mode="w", encoding=encoding) as file:
    # Salva il dizionario nel file JSON, con indentazione per leggibilità
    json.dump(config, file, indent=4)
"""


aa = """ z """