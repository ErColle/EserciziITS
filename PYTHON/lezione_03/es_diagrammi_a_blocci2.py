# 5 7 8 9 14 15 18 19 
# 5. Calcolo della somma dei quadrati fino a un numero intero positivo n

# Progettare un algoritmo che, dato un numero intero positivo n definito dall'utente, calcoli la somma:

# 1**2 + 2**2 + 3**2 + 4**2 + 5**2 + ... + n2,

# mostrando in output il risultato. Se n è negativo, l'algoritmo mostra un messaggio di errore e termina.


# n = int(input("Inserisci un Numero: " ))
# somma_potenze = 0
# potenza = None

# if n > 0:
    
#     for number in range (0, n):
        
#         potenza = number**2
#         print(potenza)
#         somma_potenze += potenza 
    
#     print(somma_potenze)
# else:
#     print("Errore! Numero negativo!")


# 7. Algoritmo per il calcolo della media dei voti con inserimento iterativo

# Progettare un algoritmo che consenta di inserire all'utente un elenco di voti non negativi relativi ad un esame, calcolandone la media.
# L'algoritmo deve chiedere all'utente se vuole inserire un voto. 

# Se la risposta è "SI", allora l'utente può procedere ad inserire il voto. 
# L'algoritmo deve consentire all'utente di inserire voti fin quando la risposta dell'utente sarà "NO". 

# Infine, mostrare in output il valore medio dei voti inseriti.

# count = 0
# somma = 0 
# risposta = str(input("Vuoi inserire un voto? Si o No: "))


# while risposta == "si": 
    
#     voto = int(input("Inserisci il voto: "))
#     count += +1 
#     somma = somma + voto 
#     risposta = str(input("Vuoi inserire un voto? Si o No: "))
    
# print(f"La media dei voti è {somma / count }! ")    


# 8. Determinare la somma dei numero dentro un intervallo

# Progettare un algoritmo che chieda all’utente di inserire due valori interi positivi 𝐴 e 𝐵 con 𝐴 < 𝐵. 
# Se i valori non rispettano le condizioni, mostrare un messaggio di errore e terminare. 
# Se i valori sono validi, calcolare la somma di tutti i numeri interi compresi tra 𝐴 e 𝐵 (inclusi) e mostrare il risultato.

# a = int(input("Inserisci A: "))
# b = int(input("Inserisci B: "))
# somma = 0

# if ( a > b ):
    
#     for num in range ( b, a+1 ):
#         print(num)
#         somma += num
    
#     print(f"La somma dei numeri nell'intervallo tra {a} e {b} è: {somma}")
        
# else:
    
#     print("Errore! A deve essere maggiore di B!")
    

# 9 . Conteggio dei numeri divisibili

# Progettare un algoritmo che richieda all’utente di inserire un valore intero positivo n. 
# Se nè negativo, il programma termina mostrando un messaggio di errore. Se n è positivo:

# l’utente può inserire 10 numeri interi;
# contare quanti di questi numeri sono divisibili per n.
# Mostrare in output il risultato del conteggio.

# num = int(input("Inserisci il divisore: "))
# i = 1
# somma = 0

# if num > 0:
    
#     while i != 10 + 1:
    
#         n = int(input(f"{i}. Inserisci un numero: ")) 
        
#         if n%num == 0: 
#             somma += 1
            
#         i += 1
#     print(f"Hai inserito {somma} divisibili per {num}! ")
    
# else: 
#     print ("Errore! il numero deve essere positivo!")


# 14. Simulazione di un gioco di dadi

# Progettare un algoritmo che simuli un gioco basato sul lancio di due dadi virtuali a sei facce, D1 e D2. L'algoritmo deve eseguire le seguenti operazioni:

# Simulare il lancio dei due dadi.
# Calcolare la somma dei valori ottenuti dai due dadi.
# Applicare le seguenti regole di gioco per determinare il punteggio:
# Se entrambi i dadi mostrano numeri pari e la somma è maggiore di 8, il giocatore vince e il punteggio è impostato direttamente a 100.
# Se uno dei dadi mostra 6 oppure la somma è uguale a 7, il punteggio del giocatore viene incrementato di 10.
# In tutti gli altri casi, il giocatore perde e il punteggio è impostato a 0.
# Mostrare il risultato del gioco e il punteggio ottenuto.
# Il gioco continua finché il punteggio totale del giocatore non raggiunge 100 (vittoria) oppure scende a zero (sconfitta).

# punteggio = 0

# while punteggio != 100:
#     n1 = int(input("Tira il primo dado e dimmi quanto esce!: "))
#     n2 = int(input("Tira il secondo dado e dimmi quanto esce!: "))

#     somma = n1 + n2

#     if n1 % 2 == 0 and n2 % 2 == 0 and somma > 8:
#         punteggio = 100
#         print("Hai vinto! Punteggio uguale a 100!")
#         break

#     elif n1 == 6 or n2 == 6 or somma == 7:
#         punteggio += 10
#         print(f"Punteggio attuale: {punteggio}")

#     else:
#         punteggio = 0
#         break

# if punteggio == 0:
#     print("Punteggio uguale a 0, hai perso!")

# 18. Classifica e somma condizionale

# Scrivere un algoritmo che consenta all’utente di inserire una numero variabile di numeri interi (la quantità è scelta dall’utente). L'algoritmo deve:

# sommare i numeri pari e maggiori della media dei numeri inseriti fino a quel momento;
# sommare i numeri dispari o minori della media dei numeri inseriti fino a quel momento;
# Mostrare in output entrambe le somme e indicare quale somma è maggiore.

# i = int(input("Quanti numeri vuoi inserire?: "))

# somma_pari = 0
# somma_dispari = 0

# somma = 0
# count = 0

# while i != 0:
    
#     print(i,".")
#     num = int(input("Inserisci un numero: "))
#     count += 1
#     somma += num
#     media = somma / count
    
#     if num%2 == 0 and num > media: 
#         somma_pari += num
        
#     if num%2 == 1 and num < media:
#         somma_dispari += num
    
#     i-= 1 

# print(f"Somma pari: {somma_pari}\nSomma dispari: {somma_dispari}")

# 19. Calcolo di sequenze condizionali

# Scrivere un algoritmo che calcoli il valore di una sequenza numerica basata su un valore n inserito dall’utente. La sequenza segue queste regole:

# se n è pari, calcolare la somma dei numeri da 1 a n che sono divisibili per 4;
# se n è dispari, calcolare il prodotto dei numeri dispari da 1 a n;
# se n è negativo, mostrare un messaggio di errore e terminare.
# Infine, mostrare il risultato calcolato.

# num = int(input("Inserisci un numero: "))
# somma = 0 
# prodotto = 1
# if num > 0:

#     for elem in range ( 0, num+1 ):
#         if num%2 == 0:
            
#             if elem%4 == 0:
#                 somma += elem
#                 risultato = somma
                
#     for elem in range ( 1, num+1 ):
#         if num%2 == 1: 
            
#             if elem%2 == 1:
                
#                 prodotto *= elem
#                 risultato = prodotto 

#     print(f"Il risultato è: {risultato}")

# else:
#     print("Errore! Il numero deve essere positvo!")
