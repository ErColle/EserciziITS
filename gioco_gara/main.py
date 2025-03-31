'''
PERCORSO 70 QUADRATI 
    OGNI QUADRATO RAPPRESENTA UNA POSIZIONE
        LEPRE E TARTARUGA START QUADRATO #1 
        
OROLOGIO CHE CONTA I SECONDI 
    OGNI TICK IL PERCORSO E LE POSIZIONI SI AGGIORNANO
    

T = POSIZIONE TARTARUGA 

H = POSIZONE LEPRE 

"_" = POSIZIONI LIBERE

SE T E H SONO IN POSIZ UGUALI == "OUCH"

    
SE T ARRIVA POSIZIONE 70 == "TORTOISE  WINS! || VAY!!"

SE H ARRIVA POSIZIONE 70 == "HARE WINS || YUCH!!"


'''

import time 
import random
import os

def gara():
    
    timer = 0
    
    lunghezza_percorso = 70
    percorso = ['_'] * lunghezza_percorso


    posizione_tartaruga = 1
    posizione_lepre = 1
    
    percorso[posizione_lepre - 1] = "H"
    percorso[posizione_tartaruga] = "T"
    
    print("BANG !!!!! AND THEY'RE OFF !!!!!")
    
    print(" ".join(percorso))
    
    time.sleep(1)
    
    while True:
        
        os.system('cls')
        
        percorso = ['_'] * lunghezza_percorso
        
        percorso[posizione_lepre - 1] = "H"
        percorso[posizione_tartaruga - 1] = "T"
        
        posizione_tartaruga = tartaruga_move(posizione_tartaruga)
        
        posizione_lepre = lepre_move(posizione_lepre)
         
         
        if posizione_tartaruga == posizione_lepre:
            percorso[posizione_lepre - 1] == "OUCH" 
        
        if posizione_tartaruga >= lunghezza_percorso:
            print("LA TARTARUGA HA VINTO!!! YAY!!!")
            break
        elif posizione_lepre >= lunghezza_percorso:
            print("LA LEPRE HA VINTO!!! YUCH!!!")
            break
        
        print(f"Durata gara: {timer} secondi")
        timer += 1
        
        print(f"Posizione lepre: {posizione_lepre}")
        print(f"Posizione tartaruga: {posizione_tartaruga}")
        
        print(" ".join(percorso))
        
        time.sleep(1)


'''

- Passo veloce (50% di probabilità): avanza di 3 quadrati.
    - Scivolata (20% di probabilità): arretra di 6 quadrati. Non può andare sotto il quadrato 1.
    - Passo lento (30% di probabilità): avanza di 1 quadrato.


'''

def tartaruga_move(posizione_tartaruga):
    numero = random.randint(1, 10)
    
    if numero <= 5:  
        posizione_tartaruga += 3
        
    elif numero <= 8:  
        posizione_tartaruga += 1
        
    else: 
        posizione_tartaruga = max(1, posizione_tartaruga - 6)
    
    return posizione_tartaruga
        
'''

  - Riposo (20% di probabilità): non si muove.
    - Grande balzo (20% di probabilità): avanza di 9 quadrati.
    - Grande scivolata (10% di probabilità): arretra di 12 quadrati. Non può andare sotto il quadrato 1.
    -  Piccolo balzo (30% di probabilità): avanza di 1 quadrato.
    - Piccola scivolata (20% di probabilità): arretra di 2 quadrati. Non può andare sotto il quadrato 1.


'''


def lepre_move(posizione_lepre):
    numero = random.randint(1, 10)

    if numero <= 2: 
        posizione_lepre = max(1, posizione_lepre - 12)
    
    elif numero <= 4:
        posizione_lepre += 9
        
    elif numero <= 6:  
        posizione_lepre += 1
        
    elif numero <= 8: 
        posizione_lepre = max(1, posizione_lepre - 2)
        
    else: 
        pass  

    return posizione_lepre


gara()