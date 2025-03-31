# TO DO: 

#SISTEMARE L'OUCH
""" SFIDE AGGIUNTIVE:
1. Variabilità Ambientale:
Introdurre fattori ambientali che possono influenzare la corsa, come il meteo.
Ad esempio, la pioggia può ridurre la velocità di avanzamento o aumentare la probabilità di scivolate per entrambi i concorrenti. 
Implementare un sistema dove le condizioni 'soleggiato' e 'pioggia' cambiano dinamicamente ogni 10 tick dell'orologio.
 """
import time 
import random
import os

def gara():
     
    lunghezza_percorso = 70
    percorso = ['_'] * lunghezza_percorso
    percorso.append("██")
    
    ambiente = "Soleggiato"


    posizione_tartaruga = 1
    posizione_lepre = 1
    
    percorso[posizione_lepre - 1] = "H"
    percorso[posizione_tartaruga] = "T"
    
    timer = 1
    countdown = 3

    while countdown != 0:

        print(f"RACE STARTS IN {countdown}\n\n\n\n\n")
        print(" ".join(percorso))
        countdown -= 1
        time.sleep(1)
        os.system('cls')
    
    print(f"BANG !!!!! AND THEY'RE OFF !!!!!")
    print(" ".join(percorso))
    time.sleep(1)
    os.system('cls')

    print(f"Durata gara: {timer} secondi\nCondizioni ambientali: {ambiente}\nPosizione lepre: {posizione_lepre}\nPosizione tartaruga: {posizione_tartaruga}\n\n\n")
    print(" ".join(percorso))
    
    time.sleep(1)
    
    while True:

        #AMBIENTE
        if timer % 10 == 0:
            numero = random.randint(1, 10)
                
            if numero >= 3:
                ambiente = "Soleggiato"
            
            else:
                ambiente = "Piovoso"
        
        os.system('cls')
        
        #STAMPA PERCORSO
        if ambiente == "Soleggiato":
            percorso = ['_'] * lunghezza_percorso
            
        elif ambiente == "Piovoso":
             percorso = ['~'] * lunghezza_percorso
        
        percorso.append("██")
        
        percorso[posizione_lepre - 1] = "H"
        percorso[posizione_tartaruga - 1] = "T"
        
        posizione_tartaruga = tartaruga_move(posizione_tartaruga)
        
        posizione_lepre = lepre_move(posizione_lepre)
         
         
        if posizione_tartaruga == posizione_lepre:
            percorso[posizione_lepre - 1] == "OUCH"
        
        #CONDIZIONE FINE GARA
        if posizione_tartaruga >= lunghezza_percorso:
            print("LA TARTARUGA HA VINTO!!! YAY!!!")
            

            break
        elif posizione_lepre >= lunghezza_percorso:
            print("LA LEPRE HA VINTO!!! YUCH!!!")
            break
        
        timer += 1
        print(f"Durata gara: {timer} secondi")
        print(f"Condizioni ambientali: {ambiente}")
        print(f"Posizione lepre: {posizione_lepre}")
        print(f"Posizione tartaruga: {posizione_tartaruga}\n\n\n")
        
        print(" ".join(percorso))
        
        time.sleep(1)

def tartaruga_move(posizione_tartaruga):
    numero = random.randint(1, 10)
    
    if numero <= 5:  
        posizione_tartaruga += 3
        
    elif numero <= 8:  
        posizione_tartaruga += 1
        
    else: 
        posizione_tartaruga = max(1, posizione_tartaruga - 6)
    
    return posizione_tartaruga
        
def lepre_move(posizione_lepre):
    numero = random.randint(1, 10)

    if numero <= 2: 
        posizione_lepre = max(1, posizione_lepre - 12)
    
    elif numero <= 5:
        posizione_lepre += 9
        
    elif numero <= 6:  
        posizione_lepre += 1
        
    elif numero <= 8: 
        posizione_lepre = max(1, posizione_lepre - 2)
        
    else: 
        pass  

    return posizione_lepre

gara()