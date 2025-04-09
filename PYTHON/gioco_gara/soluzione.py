import random

# Costanti
LUNGHEZZA_CORSIA = 70
CAMBIO_CONDIZIONI = 10  # Ogni quanti tick cambiano le condizioni
ENERGIA_INIZIALE = 100  # Energia iniziale per tartaruga e lepre
OSTACOLI = {15: -3, 30: -5, 45: -7}  # Posizioni degli ostacoli e l'effetto negativo
BONUS = {10: 5, 25: 3, 50: 10}  # Posizioni dei bonus e l'effetto positivo

# Stato iniziale
tartaruga = 1
lepre = 1
tick = 0
condizioni = "soleggiato"  # Condizioni meteorologiche iniziali
energia_tartaruga = ENERGIA_INIZIALE
energia_lepre = ENERGIA_INIZIALE


# Funzione per mostrare la posizione corrente nella pista
def mostra_posizioni(tartaruga, lepre):
    traccia = ['_'] * LUNGHEZZA_CORSIA
    pos_tartaruga = min(tartaruga, LUNGHEZZA_CORSIA)
    pos_lepre = min(lepre, LUNGHEZZA_CORSIA)
    if pos_tartaruga == pos_lepre:
        traccia[pos_tartaruga-1] = 'OUCH!!!'
    else:
        traccia[pos_tartaruga-1] = 'T'
        traccia[pos_lepre-1] = 'H'
    print(''+str(traccia))

# Funzione per la mossa della tartaruga
def muovi_tartaruga(tartaruga, condizioni, energia_tartaruga):
    mossa = random.randint(1, 10)

    if condizioni == "pioggia":
        mod_tartaruga = -1 
    else:
        mod_tartaruga = 0

    if 1 <= mossa <= 5 and energia_tartaruga >= 5:
        tartaruga += 3 + mod_tartaruga # Passo veloce
        energia_tartaruga -= 5
    else:
        energia_tartaruga += 10
        energia_tartaruga = min(energia_tartaruga, ENERGIA_INIZIALE)  # Ricarica se non ha energia per muoversi
    
    if 6 <= mossa <= 7 and energia_tartaruga >= 10:
        tartaruga -= 6 + mod_tartaruga # Scivolata
        tartaruga = max(1, tartaruga)  # Non andare sotto il quadrato 1
        energia_tartaruga -= 10
    else:
        energia_tartaruga += 10
        energia_tartaruga = min(energia_tartaruga, ENERGIA_INIZIALE)  # Ricarica se non ha energia per muoversi
    
    if 8 <= mossa <= 10 and energia_tartaruga >= 3:
        tartaruga += 1 + mod_tartaruga # Passo lento
        energia_tartaruga -= 3
    else:
        energia_tartaruga += 10
        energia_tartaruga = min(energia_tartaruga, ENERGIA_INIZIALE)  # Ricarica se non ha energia per muoversi


    # Controlla la presenza di ostacoli
    if tartaruga in OSTACOLI:
        tartaruga += OSTACOLI[tartaruga]
        tartaruga = max(1, tartaruga)  # Non andare sotto il quadrato 1

    # Controlla la presenza di bonus
    if tartaruga in BONUS:
        tartaruga += BONUS[tartaruga]


    return tartaruga

# Funzione per la mossa della lepre
def muovi_lepre(lepre, condizioni, energia_lepre):
    mossa = random.randint(1, 10)

    if condizioni == "pioggia":
        mod_lepre = -2
    else:
        mod_lepre = 0

    if 1 <= mossa <= 2:
        lepre += 0  # Riposo
        energia_lepre += 10 # Ricarica energia
        energia_lepre = min(energia_lepre, ENERGIA_INIZIALE) # Verifico che l'energia guadagnata non superi l'energia iniziale
    elif 3 <= mossa <= 4 and energia_lepre >= 15:
        lepre += 9 + mod_lepre  # Grande balzo
        energia_lepre -= 15
    elif mossa == 5 and energia_lepre >= 20:
        lepre -= 12 + mod_lepre # Grande scivolata
        lepre = max(1, lepre)  # Non andare sotto il quadrato 1
        energia_lepre -= 20
    elif 6 <= mossa <= 8 and energia_lepre >= 5:
        lepre += 1 + mod_lepre # Piccolo balzo
        energia_lepre -= 5
    elif 9 <= mossa <= 10 and energia_lepre >= 8:
        lepre -= 2 + mod_lepre # Piccola scivolata
        lepre = max(1, lepre)  # Non andare sotto il quadrato 1
        energia_lepre -= 8


    # Controlla la presenza di ostacoli
    if lepre in OSTACOLI:
        lepre += OSTACOLI[lepre]
        lepre = max(1, lepre)  # Non andare sotto il quadrato 1

    # Controlla la presenza di bonus
    if lepre in BONUS:
        lepre += BONUS[lepre]

    return lepre

def cambia_condizioni():
    return random.choice(["soleggiato", "pioggia", "ventoso"])

print("BANG !!!!!")
print("AND THEY'RE OFF !!!!!")

while tartaruga < LUNGHEZZA_CORSIA and lepre < LUNGHEZZA_CORSIA:
    if tick % CAMBIO_CONDIZIONI == 0:
        condizioni = cambia_condizioni()  # Cambia le condizioni ogni 10 tick
        print(f"Le condizioni meteorologiche sono ora: {condizioni}")
    
    tartaruga = muovi_tartaruga(tartaruga, condizioni, energia_tartaruga)  # Aggiorno posizione tartaruga
    lepre = muovi_lepre(lepre, condizioni, energia_lepre)  # Aggiorno posizione lepre
    
    mostra_posizioni(tartaruga, lepre)
    tick += 1

    if tartaruga >= LUNGHEZZA_CORSIA or lepre >= LUNGHEZZA_CORSIA:
        if tartaruga >= LUNGHEZZA_CORSIA and lepre >= LUNGHEZZA_CORSIA:
            print("It's a tie.")
        elif tartaruga >= LUNGHEZZA_CORSIA:
            print("TORTOISE WINS! || YAY!!!")
        elif lepre >= LUNGHEZZA_CORSIA:
            print("Hare wins. Yuch.")
        break