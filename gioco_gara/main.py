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
        os.system('clear')

    print(f"BANG !!!!! AND THEY'RE OFF !!!!!\n\n\n\n\n")
    print(" ".join(percorso))
    time.sleep(1)
    os.system('clear')

    print(f"Durata gara: {timer} secondi\nCondizioni ambientali: {ambiente}\nPosizione lepre: {posizione_lepre}\nPosizione tartaruga: {posizione_tartaruga}\n\n\n")
    print(" ".join(percorso))
    
    time.sleep(1)
    
    while True:
        os.system('clear')

        if timer % 10 == 0:
            ambiente = "Soleggiato" if ambiente == "Piovoso" else "Piovoso"  # Cambia ambiente ogni 10 secondi

        if ambiente == "Soleggiato":
            percorso = ['_'] * lunghezza_percorso
        else:
            percorso = ['~'] * lunghezza_percorso

        percorso.append("██")

        posizione_tartaruga = tartaruga_move(posizione_tartaruga, ambiente)
        posizione_lepre = lepre_move(posizione_lepre, ambiente)

        percorso[posizione_lepre - 1] = "H"
        percorso[posizione_tartaruga - 1] = "T"

        if posizione_lepre == posizione_tartaruga:
            percorso[posizione_lepre - 1] = "OUCH"

        print(f"Durata gara: {timer} secondi")
        print(f"Condizioni ambientali: {ambiente}")
        print(f"Posizione lepre: {posizione_lepre}")
        print(f"Posizione tartaruga: {posizione_tartaruga}\n\n\n")
        print(" ".join(percorso))

        if posizione_tartaruga >= lunghezza_percorso or posizione_lepre >= lunghezza_percorso:
            if posizione_tartaruga >= lunghezza_percorso:
                print("LA TARTARUGA HA VINTO!!! YAY!!!")
            else:
                print("LA LEPRE HA VINTO!!! YUCH!!!")
            break

        # time.sleep(0.1)
        timer += 1  

def tartaruga_move(posizione_tartaruga, ambiente):
    numero = random.randint(1, 10)
    
    if ambiente == "Piovoso":
        if numero <= 4:
            posizione_tartaruga = max(1, posizione_tartaruga - 6)
        elif numero <= 7:
            posizione_tartaruga += 1
        else:
            posizione_tartaruga += 2
    else:
        if numero <= 5:
            posizione_tartaruga += 3
        elif numero <= 8:
            posizione_tartaruga += 1
        else:
            posizione_tartaruga = max(1, posizione_tartaruga - 6)

    return posizione_tartaruga

def lepre_move(posizione_lepre, ambiente):
    numero = random.randint(1, 10)
    
    if ambiente == "Piovoso":
        if numero <= 3:
            posizione_lepre = max(1, posizione_lepre - 12)
        elif numero <= 6:
            posizione_lepre += 1
        elif numero <= 8:
            posizione_lepre += 2
        else:
            pass
    else:
        if numero <= 2:
            posizione_lepre = max(1, posizione_lepre - 12)
        elif numero <= 5:
            posizione_lepre += 9
        elif numero <= 6:
            posizione_lepre += 1
        elif numero <= 8:
            posizione_lepre = max(1, posizione_lepre - 2)
    
    return posizione_lepre

gara()
