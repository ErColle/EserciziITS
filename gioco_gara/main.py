import time
import random
import os
import sys

def gara(lunghezza_percorso):
    
    #variabili
    
    ostacoli = {
        59: -1,  
        41: -2,  #Posizione: Penalita',
        21: -3
    }
    
    bonus = {
        51: 1,  
        36: 3,  #Posizione: Bonus,
        14: 2
    }
    

    ambiente = "Soleggiato"
    posizione_tartaruga = 1
    posizione_lepre = 1

    timer = 1
    countdown = 3
    
    percorso = ['_'] * lunghezza_percorso
    percorso.append("🏇🌲")
    
    #STAMPA BONUS E MALUS NEL PERCORSO
    for posizioni in ostacoli.keys():
            percorso[posizioni-1] = "x"
    
    for posizioni in bonus.keys():
            percorso[posizioni-1] = "^"
    
    while countdown != 0:
        print(f"                              📢 RACE STARTS IN {countdown} 📢\n\n\n\n\n")
        print(f"🌲🏁 {' '.join(percorso)}")
        countdown -= 1
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')

    print(f"🔥 BANG !!!!! AND THEY'RE OFF !!!!! 🔥\n\n\n\n\n")
    print(f"🌲🏁 {' '.join(percorso)}")
    time.sleep(1)
    os.system('cls')

    while True:
        os.system('cls')

        # CAMBIO AMBIENTE OGNI 10 SEC/TICK
        if timer % 10 == 0:
            ambiente = "Soleggiato" if ambiente == "Piovoso" else "Piovoso"

        # CREAZIONE PERCORSO 
        percorso = ['_' if ambiente == "Soleggiato" else '~'] * lunghezza_percorso
        percorso.append("🏇🌲")
        
        #STAMPA BONUS E MALUS NEL PERCORSO --. DA VEDERE 
        for posizioni in ostacoli.keys():
            percorso[posizioni-1] = "x"
    
        for posizioni in bonus.keys():
            percorso[posizioni-1] = "^"

        posizione_tartaruga = tartaruga_move(posizione_tartaruga, ambiente, lunghezza_percorso)
        posizione_lepre = lepre_move(posizione_lepre, ambiente, lunghezza_percorso)

        percorso[min(posizione_lepre, lunghezza_percorso) - 1] = "🐰"
        percorso[min(posizione_tartaruga, lunghezza_percorso) - 1] = "🐢"
        
        
        #VARIAZIONI POSIZIONI OSTACOLI --. DA VEDERE 
        for chiave, valore in ostacoli.items():
            if posizione_lepre == chiave:
                posizione_lepre += valore 
                print("⬇⬇ MALUS 🐰 ⬇⬇")
                percorso[posizione_lepre - valore] = str(valore)
            else: 
                pass
                
        for chiave, valore in ostacoli.items():
            if posizione_tartaruga == chiave:
                posizione_tartaruga += valore 
                print("⬇⬇ MALUS 🐢 ⬇⬇")
                percorso[posizione_tartaruga - valore] = str(valore)
            else:
                pass
        
        #VARIAZIONI POSIZIONI BONUS
        for chiave, valore in bonus.items():
            if posizione_lepre == chiave:
                posizione_lepre += valore 
                print("⬆⬆ BONUSSS 🐰 ⬆⬆")
                percorso[posizione_lepre - valore] = str(f"+{valore}")
            else: 
                pass
                
        for chiave, valore in bonus.items():
            if posizione_tartaruga == chiave:
                posizione_tartaruga += valore 
                print("⬆⬆ BONUSSS 🐢 ⬆⬆")
                percorso[posizione_tartaruga - valore] = str(f"+{valore}")
            else:
                pass

        # SE STESSA POSIZIONE "OUCH"
        if posizione_lepre == posizione_tartaruga:
            percorso[min(posizione_lepre, lunghezza_percorso) - 1] = "OUCH"

        # PRINT INFOS 
        print(f"🕓 Durata gara: {timer} secondi")
        print(f"🌎 Condizioni ambientali: {ambiente} {'🌧️' if ambiente == 'Piovoso' else '🌞'}")
        print(f"🔹 Posizione lepre: {posizione_lepre}")
        print(f"🔸 Posizione tartaruga: {posizione_tartaruga}\n\n")
        print(f"🌲🏁 {' '.join(percorso)}")
        
        # CRITERI DI VINCITA E PAREGGIO
        if posizione_tartaruga >= lunghezza_percorso or posizione_lepre >= lunghezza_percorso:
            if posizione_tartaruga >= lunghezza_percorso and posizione_lepre < lunghezza_percorso:
                print("\nLA TARTARUGA HA VINTO 🏆!!! YAY!!!\n")
            elif posizione_lepre >= lunghezza_percorso and posizione_tartaruga < lunghezza_percorso:
                print("\nLA LEPRE HA VINTO 🏆!!! YUCH!!!\n")
            else:
                print("\nPAREGGIO! 🏆 🐢🐰 🏆")
            sys.exit()

        time.sleep(1)
        timer += 1  

def tartaruga_move(posizione_tartaruga, ambiente, lunghezza_percorso):
    numero = random.randint(1, 10)

    if ambiente == "Piovoso":
        if numero <= 3:  # 30% 
            posizione_tartaruga = max(1, posizione_tartaruga - 6)
        elif numero <= 8:  # 50% 
            posizione_tartaruga += 3
        else:  # 20% 
            posizione_tartaruga += 1
    else:
        if numero <= 5:  # 50% 
            posizione_tartaruga += 3
        elif numero <= 7:  # 20% 
            posizione_tartaruga = max(1, posizione_tartaruga - 6)
        else:  # 30% 
            posizione_tartaruga += 1

    return min(posizione_tartaruga, lunghezza_percorso)

def lepre_move(posizione_lepre, ambiente, lunghezza_percorso):
    numero = random.randint(1, 10)

    if ambiente == "Piovoso":
        if numero <= 3:  # 30% 
            pass
        elif numero <= 5:  # 20% 
            posizione_lepre += 9
        elif numero <= 6:  # 10% 
            posizione_lepre = max(1, posizione_lepre - 12)
        elif numero <= 8:  # 20% 
            posizione_lepre += 1
        else:  # 20% 
            posizione_lepre = max(1, posizione_lepre - 2)
    else:
        if numero <= 2:  # 20%
            pass
        elif numero <= 4:  # 20% 
            posizione_lepre += 9
        elif numero <= 5:  # 10%
            posizione_lepre = max(1, posizione_lepre - 12)
        elif numero <= 7:  # 30% 
            posizione_lepre += 1
        else:  # 20% 
            posizione_lepre = max(1, posizione_lepre - 2)

    return min(posizione_lepre, lunghezza_percorso)

os.system('cls')
# Input lunghezza percorso con controllo dei valori
percorso_len = int(input("Inserisci lunghezza percorso | Minimo 30 Massimo 70: "))
if not (30 <= percorso_len <= 70):
    print("\n\n\n❗Errore! Valore inserito non valido! ❗\n\n")
    sys.exit()

gara(percorso_len)
