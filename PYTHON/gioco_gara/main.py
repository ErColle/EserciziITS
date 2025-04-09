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
    
    stamina_tartaruga = 100
    stamina_lepre = 100
    
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
        clear_screen()


    print(f"🔥 BANG !!!!! AND THEY'RE OFF !!!!! 🔥\n\n\n\n\n")
    print(f"🌲🏁 {' '.join(percorso)}")
    time.sleep(1)
    clear_screen()


    while True:
        clear_screen()

        
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
            
        #RICHIAMO FUNZIONI DI MOVIMENTO  
        posizione_tartaruga, stamina_tartaruga = tartaruga_move(posizione_tartaruga, ambiente, stamina_tartaruga)
        posizione_lepre, stamina_lepre = lepre_move(posizione_lepre, ambiente, stamina_lepre)

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
 
        print(f"\n🔋 Stamina: {stamina_tartaruga}% 🐢")
        print(f"\n🔋 Stamina: {stamina_lepre}% 🐰")
        
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

def tartaruga_move(posizione_tartaruga, ambiente, stamina_tartaruga):
    numero = random.randint(1, 10)
    if stamina_tartaruga > 0:
        if ambiente == "Piovoso":
            if numero <= 3:  # 30% 
                posizione_tartaruga = max(1, posizione_tartaruga - 6)
                stamina_tartaruga -= 10
            elif numero <= 8:  # 50% 
                posizione_tartaruga += 3
                stamina_tartaruga -= 5
            else:  # 20% 
                posizione_tartaruga += 1
                stamina_tartaruga -= 3
        else:
            if numero <= 5:  # 50% 
                posizione_tartaruga += 3
                stamina_tartaruga -= 5
            elif numero <= 7:  # 20% 
                posizione_tartaruga = max(1, posizione_tartaruga - 6)
                stamina_tartaruga -= 10
            else:  # 30% 
                posizione_tartaruga += 1
                stamina_tartaruga -= 3
    else: 
        stamina_tartaruga += 10 
        

    return posizione_tartaruga, max(stamina_tartaruga, 0)


def lepre_move(posizione_lepre, ambiente, stamina_lepre):
    numero = random.randint(1, 10)

    if stamina_lepre <= 0:
        if (ambiente == "Piovoso" and numero <= 3) or (ambiente != "Piovoso" and numero <= 2):
            stamina_lepre += 10
        return posizione_lepre, stamina_lepre

    if ambiente == "Piovoso":
        if numero <= 5:          # 50%
            posizione_lepre += 9
            stamina_lepre -= 15
        elif numero <= 6:        # 10%
            posizione_lepre = max(1, posizione_lepre - 12)
            stamina_lepre -= 20
        elif numero <= 8:        # 20%
            posizione_lepre += 1
            stamina_lepre -= 3
        else:                    # 20%
            posizione_lepre = max(1, posizione_lepre - 2)
            stamina_lepre -= 8
    else:  # Tempo sereno
        if numero <= 2:          # 20%
            stamina_lepre += 10
        elif numero <= 4:        # 20%
            posizione_lepre += 9
            stamina_lepre -= 15
        elif numero <= 5:        # 10%
            posizione_lepre = max(1, posizione_lepre - 12)
            stamina_lepre -= 20
        elif numero <= 7:        # 20%
            posizione_lepre += 1
            stamina_lepre -= 3
        else:                    # 30%
            posizione_lepre = max(1, posizione_lepre - 2)
            stamina_lepre -= 8
            
    
    return posizione_lepre, min(max(stamina_lepre, 0), 100)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()

gara()
