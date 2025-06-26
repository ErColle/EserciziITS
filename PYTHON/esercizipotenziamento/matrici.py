import random

def genera( dim: int ): 

    matrice = []
    for i in range(dim):
        riga_matrice = []
        for j in range(dim):
            riga_matrice.append(random.randint(0, 12))
        matrice.append(riga_matrice)

    for riga in matrice:
        print(f"{riga}\n")
        
    return matrice

def printMAT(matrice):
    for riga in matrice:
        for elemento in riga:
            print(f"{elemento:>5}", end="")  
        print(f"\n")
        
def calcolaCarico( matrice, riga: int , colonna: int ):
    
    sum_riga = sum(matrice[riga])
    sum_col = 0
    
    for row in range(len(matrice)):     #
        sum_col += matrice[row][colonna]   
        
    carico = sum_riga - sum_col
    
    print(carico)
    return carico

def caricoNullo(matrice): 

    tuple_list: list[tuple[int,int]] = [] 
    
    for row in range(len(matrice)):
        for col in range(len(matrice[row])):
            
            carico = calcolaCarico(matrice, row, col)
            if carico == 0:
                tuple_list.append(carico)
                
    print(tuple_list)

matrice = genera(4)

printMAT(matrice)

calcolaCarico(matrice, 1, 3)

print(matrice)

# caricoNullo(matrice)

