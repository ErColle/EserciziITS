try: # ----> Esegui il codice 
    pass

except: # ----> Se c'è un errore, esegui il codice
    pass

else: # ----> Se non c'è errore, esegui il codice
    pass

finally: # ----> Esegui il codice, sia che ci sia un errore o meno
    pass

#CUSTOM EXCEPTION

class CustomError(Exception): # ----> Crea una classe di errore personalizzata
    pass

#keyword raise  --> richiama un'eccezione
number = 10
if number > 5: # ----> Se il numero è maggiore di 5, solleva un'eccezione
    raise Exception("Il numero è maggiore di 5") # ----> Solleva un'eccezione
print ("Il numero è minore di 5")

