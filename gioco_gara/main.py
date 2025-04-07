import time
import random
import os
import sys

def gara():
    
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
    
    lunghezza_percorso = 70
    ambiente = "Soleggiato"
    posizione_tartaruga = 1
    posizione_lepre = 1

    timer = 1
    countdown = 3
    
    percorso = ['_'] * lunghezza_percorso
    percorso.append("🏅🌲")
    percorso[posizione_lepre-1] = "🐰"
    percorso[posizione_tartaruga] = "🐢"
    
    #STAMPA BONUS E MALUS NEL PERCORSO
    
    for posizioni in ostacoli.keys():
            percorso[posizioni-1] = "▫"

    for posizioni in bonus.keys():
            percorso[posizioni-1] = "☆"
    
    while countdown != 0:
        print(f"                                                          📢 RACE STARTS IN {countdown} 📢\n\n\n\n\n")
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
        
        # CAMBIO AMBIENTE OGNI 10 SEC/TICK
        if timer % 10 == 0:
            ambiente = "Soleggiato" if ambiente == "Piovoso" else "Piovoso"

        # CREAZIONE PERCORSO 
        percorso = ['_' if ambiente == "Soleggiato" else '~'] * lunghezza_percorso
        percorso.append("🏅🌲")
        
        #STAMPA BONUS E MALUS NEL PERCORSO
        for posizioni in ostacoli.keys():
            percorso[posizioni-1] = "▫"
    
        for posizioni in bonus.keys():
            percorso[posizioni-1] = "☆"

        posizione_tartaruga = tartaruga_move(posizione_tartaruga, ambiente)
        posizione_lepre = lepre_move(posizione_lepre, ambiente)
        
        # Assicura che le posizioni non superino la lunghezza del percorso
        posizione_tartaruga = min(posizione_tartaruga, lunghezza_percorso)
        posizione_lepre = min(posizione_lepre, lunghezza_percorso)

        
        #MALUSS 
        
        for chiave, valore in ostacoli.items():
            if posizione_lepre == chiave:
                posizione_lepre = posizione_lepre + valore 
                print("⬇⬇⬇MALUSSS🐰⬇⬇⬇")
                percorso[chiave-1] = str(valore) 
            else:
                pass
                
        for chiave, valore in ostacoli.items():
            if posizione_tartaruga == chiave:
                posizione_tartaruga = posizione_tartaruga + valore
                print("⬇⬇⬇MALUSSS🐢⬇⬇⬇")
                percorso[chiave-1] = str(valore) 
            else: 
                pass
        #BONUSSS
                
        for chiave, valore in bonus.items():
            if posizione_lepre == chiave:
                posizione_lepre = posizione_lepre + valore
                print("⬆⬆⬆BONUSSS🐰⬆⬆⬆")
                percorso[chiave-1] = str(f"+ {valore}") 
            else: 
                pass
                
        for chiave, valore in bonus.items():
            if posizione_tartaruga == chiave:
                posizione_tartaruga = posizione_tartaruga + valore
                print("⬆⬆⬆BONUSSS🐢⬆⬆⬆")
                percorso[chiave-1] = str(f"+ {valore}") 
            else: 
                pass

        # SE STESSA POSIZIONE "OUCH"
        if posizione_lepre == posizione_tartaruga:
            percorso[min(posizione_lepre, lunghezza_percorso) - 1] = "OUCH"
            
        #LITITE POSIZIONE A MASSIMO PERCORSO 
        percorso[min(posizione_lepre, lunghezza_percorso) - 1] = "🐰"
        percorso[min(posizione_tartaruga, lunghezza_percorso) - 1] = "🐢"


        # PRINT INFOS 
        print(f"🕓 Durata gara: {timer} secondi")
        print(f"🌎 Condizioni ambientali: {ambiente} {'🌧️' if ambiente == 'Piovoso' else '🌞'}")
        print(f"🔹 Posizione lepre: {posizione_lepre}")
        print(f"🔸 Posizione tartaruga: {posizione_tartaruga}\n\n")
        print(f"🌲🏁 {' '.join(percorso)}")
        
        # CRITERI DI VINCITA E PAREGGIO
        if posizione_tartaruga >= lunghezza_percorso or posizione_lepre >= lunghezza_percorso:
            if posizione_tartaruga >= lunghezza_percorso and posizione_lepre < lunghezza_percorso:
                print("\n                                                        LA TARTARUGA HA VINTO 🏆!!! YAY!!!\n")
            elif posizione_lepre >= lunghezza_percorso and posizione_tartaruga < lunghezza_percorso:
                print("\n                                                        LA LEPRE HA VINTO 🏆!!! YUCH!!!\n")
            else:
                print("\nPAREGGIO! 🏆 🐢🐰 🏆")
            sys.exit()


        time.sleep(1)
        timer += 1  

def tartaruga_move(posizione_tartaruga, ambiente):
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

    return posizione_tartaruga

def lepre_move(posizione_lepre, ambiente):
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

    return posizione_lepre

os.system('clear')

gara()
