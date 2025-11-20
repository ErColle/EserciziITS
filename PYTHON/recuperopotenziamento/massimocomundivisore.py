# 8.B Il Massimo Comun Divisore di due o più numeri è il più grande divisore comune dei numeri considerati.
# Ad esempio, se consideriamo i numeri 12 e 18, il loro Massimo Comun Divisore è mcd(12,18) = 6.
# Infatti,
# i divisori di 12 sono:
#         12 = 1, 2, 3, 4, 6, 12
# i divisori di 18 sono:
#         18 = 1, 2, 3, 6, 9, 18

# il divisore più grande che 12 e 18 hanno in comune è 6.

# Scrivere nel file frazione.py una funzione  mcd(int x, int y) per il calcolo del Massimo Comune Divisore.
 
# Nel caso in cui esista un Massimo Comun Divisore tra i numeri x e y, allora la funzione deve ritornarlo come numero intero.
# Altrimenti, nel caso in cui non esista un massimo Comun Divisore tra i numeri x e y, la funzione deve ritornare 1.
   

# Suggerimento: per semplicità, per implementare la funzione richiesta, 
# trovare una soluzione che generalizzi l'esempio proposto e che tenga conto dei casi x > y e x < y per evitare di replicare righe di codice.

def mcd(x: int, y: int):
    
    divisorix = []
    divisoriy = []
    comuni = []
    
    for num in range(x, 0, -1):
        if x % num == 0:
            divisorix.append(num)
        
    for num in range(y, 0, -1):
        if y % num == 0:
            divisoriy.append(num)    
        
    for num in divisorix:
        if num in divisoriy:
            comuni.append(num)
    if comuni == []:
        return 1
    else:
        return max(comuni)
        

print(mcd(7, 20))
        
    