#ASSERIZIONI assert

# Le asserzioni sono delle affermazioni che devono essere vere in un determinato punto del programma
# Puo essere utilizzato per debugging e testare il codice
 
assert condizione, "Messaggio di errore" # ----> Se la condizione è falsa, solleva un'eccezione con il messaggio di errore

x = 5

assert x > 0, "x deve essere maggiore di 0"
