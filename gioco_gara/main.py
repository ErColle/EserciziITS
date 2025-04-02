import time
import random
import os

lunghezza_percorso = 40

def gara(lunghezza_percorso):
    percorso = ['_'] * lunghezza_percorso
    percorso.append("🥇🌲")

    ambiente = "Soleggiato"
    posizione_tartaruga = 1
    posizione_lepre = 1

    timer = 1
    countdown = 3

    while countdown != 0:
        print(f"                              📢 RACE STARTS IN {countdown} 📢\n\n\n\n\n")
        print(f"🌲🏁 {' '.join(percorso)}")
        countdown -= 1
        time.sleep(1)
        os.system('clear')

    print(f"🔥 BANG !!!!! AND THEY'RE OFF !!!!! 🔥\n\n\n\n\n")
    print(f"🌲🏁 {' '.join(percorso)}")
    time.sleep(1)
    os.system('clear')

    while True:
        os.system('clear')

        if timer % 10 == 0:
            ambiente = "Soleggiato" if ambiente == "Piovoso" else "Piovoso"

        percorso = ['_' if ambiente == "Soleggiato" else '~'] * lunghezza_percorso
        percorso.append("🥇🌲")

        posizione_tartaruga = tartaruga_move(posizione_tartaruga, ambiente)
        posizione_lepre = lepre_move(posizione_lepre, ambiente)

        percorso[min(posizione_lepre, lunghezza_percorso) - 1] = "🐰"
        percorso[min(posizione_tartaruga, lunghezza_percorso) - 1] = "🐢"

        if posizione_lepre == posizione_tartaruga:
            percorso[min(posizione_lepre, lunghezza_percorso) - 1] = "OUCH"

        print(f"🕓 Durata gara: {timer} secondi")
        if ambiente == "Piovoso":
            print(f"🌎 Condizioni ambientali: {ambiente} 🌧️")
        else:
            print(f"🌎 Condizioni ambientali: {ambiente} 🌞")
            
        print(f"🔹 Posizione lepre: {posizione_lepre}")
        print(f"🔸 Posizione tartaruga: {posizione_tartaruga}\n\n\n")
        print(f"🌲🏁 {' '.join(percorso)}")

        if posizione_tartaruga >= lunghezza_percorso or posizione_lepre >= lunghezza_percorso:
            if posizione_tartaruga >= lunghezza_percorso and posizione_lepre < lunghezza_percorso:
                print("\nLA TARTARUGA HA VINTO 🏆!!! YAY!!!")
            elif posizione_lepre >= lunghezza_percorso and posizione_tartaruga < lunghezza_percorso:
                print("\nLA LEPRE HA VINTO 🏆!!! YUCH!!!")
            else:
                print("\nPAREGGIO! 🏆 🐢🐰 🏆")
            break

        time.sleep(1)
        timer += 1  

def tartaruga_move(posizione_tartaruga, ambiente):
    numero = random.randint(1, 10)

    if ambiente == "Piovoso":
        if numero <= 6:
            posizione_tartaruga += 1
        else:
            posizione_tartaruga += 2
    else:
        if numero <= 7:
            posizione_tartaruga += 2
        else:
            posizione_tartaruga += 3

    return min(posizione_tartaruga, lunghezza_percorso)

def lepre_move(posizione_lepre, ambiente):
    numero = random.randint(1, 10)

    if ambiente == "Piovoso":
        if numero <= 3:
            posizione_lepre = max(1, posizione_lepre - 5)
        elif numero <= 5:
            posizione_lepre += 2
        elif numero <= 8:
            posizione_lepre += 5  
    else:
        if numero <= 2:
            posizione_lepre = max(1, posizione_lepre - 4)
        elif numero <= 4:
            posizione_lepre += 3  
        elif numero <= 7:
            posizione_lepre += 6  
        else:
            posizione_lepre += 8  

    return min(posizione_lepre, lunghezza_percorso)

gara(80)
