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

def gara(len_percorso):
    
    percorso = ["_" * len_percorso]
    
stringa = ["_" * 70]  

print("  ".join(stringa))
    

# def tartaruga_move():
    
    

# def lepre_move():