
#MASSIMO TRA 4 NUMERI

# i: int = 0
# max = 0
# while i != 4:
# 	num = int(input("nserisci un numero: "))
# 	if num > max:
# 		max = num
# 	i += 1
# print(max)

#SOMMA DEI NUMERI POSTITIVI 
#Progettare un algoritmo che calcoli la somma dei soli numeri positivi tra 5 valori inseriti dall'utente.
#  Quindi, se un numero è negativo o zero, ignora quel valore nella somma.

# i: int = 0
# somma: int = 0
# while i != 5:
# 	num = int(input("inserisci un numero: "))
# 	if num > 0:
# 		if num%2 == 0:
# 			somma += num
# 	i += 1

# print(somma)

#CONTROLLO PARITA DI UN NUMERO 
#Progetta un algoritmo utile a determinare se un numero inserito dall'utente è pari o dispari.

# num = int(input("inserisci un numero: "))
# if num%2 == 0:
# 	print("il numero è pari")
# else:
# 	 print("il numero è dispari")

#CONTA I NUMERI PARI E DISPARI 
# Progetta un algoritmo che dati 10 numeri forniti dall'utente, conta quanti sono pari e quanti dispari.

# i: int = 0
# pari: int = 0 
# dispari: int = 0 
# while i != 10:
# 	num = int(input("inserisci un numero: "))
# 	if num%2 == 0:
# 		pari += 1
# 	else:
# 		dispari += 1
# 	i += 1
# print("i numeri pari sono: ", pari)
# print("i numeri dispari sono: ", dispari)

#Trovare i numeri maggiori di un valore soglia
#Progetta un algoritmo che dati 7 numeri, trova e comunica i numeri maggiori di un valore soglia fornito dall'utente.

# i: int = 0 
# soglia = int(input("inserisci la soglia : "))

# while i != 7:
# 	num = int(input("inserisci un numero:"))
# 	if num > soglia:
# 		print("il numero ", num, "è maggiore della soglia")
# 	i += 1

# CLASSIFICA DELLE VENDITE
# Progetta un algoritmo che forniti dall'utente 20 totali di vendita e i nomi dei venditori, 
# trova i due nomi dei venditori con il totale più alto e il totale più basso delle vendite.

# i: int = 0
# max = 0
# registro_min = {}
# registro_max = {}
# vendita = 0
# azienda = ""
# registro = {}

# vendita = int(input("inserisci il totale delle vendite: "))
# azienda = str(input("inserisci il nome del venditore: "))
# registro_min = {azienda: vendita}
# min = vendita 
# while i != 3:
# 	vendita = int(input("inserisci il totale delle vendite: "))
# 	azienda = str(input("inserisci il nome del venditore: "))
# 	registro[azienda] = vendita

# 	if vendita > max:
# 		max = vendita
# 		registro_max = {azienda: vendita}

# 	if vendita < min: 
# 		min = vendita 
# 		registro_min = {azienda: vendita}

# 	i += 1

# print("Venditore con il totale più alto: ", registro_max)
# print("Venditore con il totale più basso: ", registro_min)


#DISTRUBUZIONE DI UNA BORSA DI STUDIO 

# Progettare un algoritmo che, richiesto allo studente il reddito familiare e la media dei voti, 
# se il reddito è inferiore a 20.000 € e la media è superiore a 27 approva la borsa di studio, 
# altrimenti rifiuta la richiesta visualizzando il messaggio "Borsa di studio rifiutata. 
# (Motivo: reddito o media insufficiente)".

# reddito = int(input("inserisci il reddito familiare: "))
# media = int(input("inserisci la media dei voti: "))
# if reddito < 20000 and media > 27:
# 	print("Borsa di studio approvata")
# else:
# 	print("Borsa di studio rifiutata. (Motivo: reddito o media insufficiente)")

#SISTEMA DI PRENOTAZIONE POSTI

# Progetta un algoritmo per gestire la prenotazione dei posti in una sala che contiene 20 sedie libere. 
# L'utente può inserire una delle seguenti opzioni "prenota", "libera", "visualizza", "esci". 
# Per ogni opzione:

# se l'utente inserisce "prenota", se ci sono ancora sedie libere, decrementa di uno il numero di posti liberi;
# se l'utente inserisce "libera", incrementa di uno il numero di sedie libere;
# se l'utente inserisce "visualizza", mostra il numero dei posti liberi e il numero dei posti occupati;
# se l'utente inserisce "esci", termina l'algoritmo.
# Torna all'inserimento di una opzione finché l'utente non seleziona "esci".

# opzione: str = ""
# posti_liberi: int = 20
# posti_occupati: int = 0

# while opzione != "esci":
#     opzione = str(input("Inserisci un'opzione: "))
#     if opzione == "prenota":
#         if posti_liberi > 0:
#             posti_liberi -= 1
#             posti_occupati += 1
#         else:
#             print("posti esauriti")
#     elif opzione == "libera":
#         posti_liberi += 1
#         posti_occupati -= 1
#     elif opzione == "visualizza":
#         print("posti liberi: ", posti_liberi)
#         print("posti occupati: ", posti_occupati)


# SISTEMA DI GESTIONE DI UN PARCHEGGIO 

# Progetta un algoritmo per la gestione dell'ingresso e dell'uscita di veicoli da un parcheggio 
# con un numero massimo di posti dato in input. 
# L'utente può inserire una delle seguenti opzioni "ingresso", "uscita", "stato", "esci". Per ogni opzione:

# se l'utente inserisce "ingresso", verifica se ci sono posti disponibili, quindi incrementa il numero di posti occupati;
# se l'utente inserisce "uscita", verifica che ci siano veicoli nel parcheggio, quindi decrementa il numero di posti occupati;
# se l'utente inserisce "stato", mostra il numero dei posti liberi e il numero dei posti occupati;
# se l'utente inserisce "esci", termina l'algoritmo.
# Torna all'inserimento di una opzione finché l'utente non seleziona "esci".

# opzione: str = ""
# posti_disponibili = 100
# posti_occupati = 0

# while opzione != "esci":
#     opzione = str(input("Inserisci un'opzione: "))
#     if opzione == "ingresso":
#         if posti_disponibili > 0:
#             posti_disponibili -= 1
#             posti_occupati += 1
#         else:
#             print("posti esauriti")
#     elif opzione == "uscita":
#         if posti_occupati > 0:
#             posti_disponibili += 1
#             posti_occupati -= 1
#     elif opzione == "stato":
#         print("posti liberi: ", posti_disponibili)
#         print("posti occupati: ", posti_occupati)

# SISTEMA DI REGISTRAZIONE DI CORSI

# Progetta un algoritmo che gestisca l'iscrizione degli studenti a corsi disponibili in una università. 
# Per ogni corso ci sono un massimo di 100 posti liberi. 
# Richiesto il nome del corso, mostra un menu con le seguenti opzioni "iscrivi", "annulla", "visualizza", "elimina", ed "Esci".

# se l'utente inserisce "iscrivi", verifica se ci sono posti disponibili per il corso, quindi incrementa il numero di posti occupati;
# se l'utente inserisce "annulla", decrementa il numero di posti occupati;
# se l'utente inserisce "visualizza", mostra il numero dei posti liberi e il numero dei posti occupati nel corso;
# se l'utente inserisce "elimina", elimina il corso e richiedi un nuovo corso;
# se l'utente inserisce "esci", termina l'algoritmo.

# nome = str(input("inserisci il nome dello studente: "))
# corso = str(input("inserisci il nome del corso: "))
# opzione: str = ""
# posti_disponibili = 100
# posti_occupati = 0
# studente = {nome, corso}
# print(studente)

# while opzione != "esci":
#     opzione = str(input("Inserisci un'opzione: "))
#     if opzione == "iscrivi":
#         if posti_disponibili > 0:
#             posti_disponibili -= 1
#             posti_occupati += 1
#         else:
#             print("posti esauriti")
#     elif opzione == "annulla":
#         posti_disponibili += 1
#         posti_occupati -= 1
#     elif opzione == "visualizza":
#         print("posti liberi: ", posti_disponibili)
#         print("posti occupati: ", posti_occupati)
#     elif opzione == "elimina":
#         corso = str(input("inserisci il nome del corso: "))
#         posti_disponibili = 100
#         posti_occupati = 0
#         print(studente)

# Calcolo della somma dei quadrati fino a un numero intero positivo 

# Progettare un algoritmo che, dato un numero intero positivo n definito dall'utente, calcoli la somma:

# 1^2 + 2^2 + 3^2 + 4^2 + 5^2 + ... + n^2,

# mostrando in output il risultato. Se n è negativo, l'algoritmo mostra un messaggio di errore e termina.

# somma = 0 
# i = 1
# num = int(input("Inserisci un numero: "))

# if num > 0:
#     while i != num:
#         somma += i**2
#         i += 1
#         print(somma)
#     print("La somma dei quadrati fino a", num, "è:", somma)
# else:
#     print("Numero non valido")


# Somma condizionata di numeri in base a un valore x
# Progettare un algoritmo che chieda all'utente di inserire un valore x positivo. Se x è negativo, 
# l'algoritmo mostra un messaggio di errore e termina. Se x  è positivo, 
# il programma deve consentire all'utente di inserire 10 numeri sia positivi che negativi. 

# Se x è pari, allora dei numeri inseriti devono essere sommati solamente i numeri che sono maggiori della metà di x. 
# Se, invece, x è dispari, dei numeri inseriti devono essere sommati solo i numeri che sono minori di x.

# x = int(input("Inserisci x: "))
# i = 0
# somma = 0
# if x > 0:
# 	while i != 10:
# 		num = int(input("Inserisci un numero: "))
# 		if x % 2 == 0:
# 			if num > x / 2:
# 				somma += num
# 		else:
# 			if num < x:
# 				somma += num
# 		i += 1
# 	print(somma)
# else:
# 	print("Errore")

# Algoritmo per il calcolo della media dei voti con inserimento iterativo

# Progettare un algoritmo che consenta di inserire all'utente un elenco di voti non negativi relativi ad un esame, 
# calcolandone la media. L'algoritmo deve chiedere all'utente se vuole inserire un voto. 
# Se la risposta è "SI", allora l'utente può procedere ad inserire il voto.
#  L'algoritmo deve consentire all'utente di inserire voti fin quando la risposta dell'utente sarà "NO". 
# Infine, mostrare in output il valore medio dei voti inseriti.

# voto: int = 0
# somma: int = 0
# media: float = 0
# risposta: str = ""
# i: int = 0
# nvoti = 5
# while i != nvoti:
# 	voto = int(input("Inserisci un voto: "))
# 	if voto >= 0:
# 		somma += voto
# 		media = somma / nvoti
# 	else: 
# 		i -= 1
# 	i += 1

# print(media)

# while risposta != "no":
# 	risposta = str(input("Vuoi inserire un altro voto? "))
# 	if risposta == "si":
# 		voto = int(input("Inserisci un voto: "))
# 		if voto >= 0:
# 			somma += voto
# 			nvoti += 1 
# 			media = somma / nvoti
# 			print(media)

#  Determinare la somma dei numero dentro un intervallo

# Progettare un algoritmo che chieda all’utente di inserire due valori interi positivi 𝐴 e 𝐵 con 𝐴 < 𝐵. 
# Se i valori non rispettano le condizioni, mostrare un messaggio di errore e terminare. Se i valori sono validi, 
# calcolare la somma di tutti i numeri interi compresi tra 𝐴 e 𝐵 (inclusi) e mostrare il risultato.

# print("Inserisci due numeri interi positivi con A < B")
# a = int(input("Inserisci A: "))
# b = int(input("Inserisci B: "))

# if b > 0 and a > 0 and a < b:
# 	somma = a
# 	while a != b-1:
# 		somma += a
# 		a += 1 
# 		print(a)

# 	print("La somma è:", somma)

# else:
# 	print("Errore!!!!!")

# Validazione dell'età per l'attività

# Progettare un algoritmo che richieda all’utente di inserire la sua età.
# L'algoritmo deve:

# controllare se l’età è compresa tra 18 e 65 anni. 
# Se sì, mostrare un messaggio che indica che l’utente può partecipare all’attività;
# se l’età non rientra nell’intervallo, verificare se è inferiore a 18 oppure maggiore di 65. 
# Se sì,mostrare un messaggio che indica che l’utente non può partecipare perché ha superato l'età massima consentita 
# o non ha raggiunto l'età minima consentita.

# eta = int(input("Inserisci la tua età: "))
# if eta >= 18 and eta <= 65:
# 	print("Puoi partecipare all'attività!")
# elif eta < 18:
# 	print("Non hai raggiunto l'età minima consentita!")
# else:
# 	print("Hai superato l'età massima consentita!")


# Classifica basata su più condizioni

# Progettare un algoritmo che richieda all’utente di inserire un valore intero.
# Il programma deve verificare:

# se il numero è pari e maggiore di 10. Se sì, mostrare “Numero valido”;
# se il numero è dispari o minore o uguale a 10. Se sì, mostrare “Numero non valido”.

# num = int(input("Inserisci un numero intero: "))
# if num%2 == 0 and num > 10: 
# 	print("Numero valido")
# elif num%2 == 1 or num <= 10:
# 	print("Numero non valido")

# Scelta condizionale basata su input multipli

# Progettare un algoritmo che richieda all’utente di inserire un numero variabile n di valori x e y. L'algoritmo deve:

# calcolare il prodotto di x e y solo se entrambi i valori sono positivi;
# calcolare la somma di x e y solo se uno dei due valori è negativo;
# mostrare il risultato dell’operazione effettuata o un messaggio di errore altrimenti.

# i = 0 
# n = int(input("Inserisci n: "))
# prodotto = 0 
# sum = 0 

# while i != n:
# 	i += 1
# 	print("inserisci X  e Y")
# 	x = int(input("X: "))
# 	y = int(input("Y: "))
# 	if x > 0 and y > 0:
# 		prodotto = x*y
# 		print(prodotto)
# 	elif (x > 0 and y < 0) or (x < 0 and y > 0): 
# 		somma = y + x
# 		print(somma)
# 	else:
# 		print("Errore!")


# Esercizio di controllo numerico con condizioni arbitrarie

# Progettare un algoritmo che verifichi se tre numeri interi positivi x, y, z rispettano le seguenti regole:

# la somma di x+y+z deve essere pari;
# x deve essere divisibile per 3, y divisibile per 5 e z divisibile per 7;
# se entrambe le condizioni sono vere, mostrare: “Regole rispettate”. Altrimenti, mostrare: “Regole non rispettate”.

# x = 1
# y = 1
# z = 1

# while x > 0 and y > 0 and z > 0:  
#     print("Inserisci x, y, z")
#     x = int(input("X: "))
#     y = int(input("Y: "))
#     z = int(input("Z: "))
    
#     if x % 3 == 0 and y % 5 == 0 and z % 7 == 0:
#         print("Regole rispettate")
#     else:
#         print("Regole non rispettate")


# Sistema di gestione delle temperature
# Sviluppare un algoritmo che chieda all'utente di inserire 7 temperature
# (una per ogni giorno della settimana), L'algoritmo deve: 
# calcolarela temperatura media
# controllare se tutte le temperature sono comprese tra 10 e 30:
#     Se si, mostrare "Temperatura nella norma".
# verificare se almeno una temperatura è maggiore di 35 e minore di 5:
#     Se si, mostrare "Allerta temperatura norma"


# temp_max: float = 0
# temp_min: float = 0 
# media: float = 0
# somma: int = 0 
# i: int = 0
# giorno_max:  int= ""
# giorno_min: int = ""
# check1: bool = False
# check2: bool = False

# day = str(input("Inserisci il giorno: "))
# temp = float(input("Inserisci la temperatura del giorno: "))

# giorno_max = i
# giorno_min = i

# temp_max = temp_min = temp

# somma += temp 

# while i != (7-1): 

#     i += 1
#     print(i)
#     day = str(input("Inserisci il giorno: "))
#     temp = float(input("Inserisci la temperatura del giorno: "))

#     if temp > 35 or temp < 5:
#         check1 = True

#     if temp > 10 or temp < 30:
#         check2 = True

#     if temp > temp_max:        
#         giorno_max = i
#         temp_max = temp

#     if temp < temp_min:
#         temp_min = i
#         giorno_min = day

#     somma += temp
    

# if check1 == True:
#     print("Allerta temperatura!")
# if check2 == True:
#     print("Temperatura nella norma!")

# media = somma / 7

# print(f
# p"Temperatura minima settimanale\nGiorno: {giorno_min+1} Temperatura: {temp_min}\n")

# print(f"Temperatura massima settimanale\nGiorno: {giorno_max+1} Temperatura: {temp_max}\n")

# print("Media temperatura: ", media)


# 2-3. Personal Message: Use a variable to represent a person’s name, and print a message to that person. 
# Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”

# name: str = "Eiric"
# print (f"Hello {name}, would you like to learn some Python today?")


# 2-4. Name Cases: Use a variable to represent a person’s name, 
# and then print that person’s name in lowercase, uppercase, and title case.

# name: str = "Eric"
# print(name.lower())
# print(name.upper())
# print(name.title())


# 2-5. Famous Quote: Find a quote from a famous person you admire. 
# Print the quote and the name of its author. 
# Your output should look something like the following, 
# including the quotation marks: Albert Einstein once said, “A person who never made a mistake never tried anything new.”

# quote: str = "\"Adottiamo sti cazzo di bambini.\""
# author: str = "Cicciogamer89"

# print(f"{author} once said, {quote}")


# 3-1. Names: Store the names of a few of your friends in a list called names. 
# Print each person’s name by accessing each element in the list, one at a time.

# names: list = ["Mario", "Gabriele", "Alessio"]
# for names in names:
#     print(names)


# 3-2. Greetings: Start with the list you used in Exercise 3-1,
#  but instead of just printing each person’s name, print a message to them. 
# The text of each message should be the same, but each message should be personalized with the person’s name.

# names: list = ["Mario", "Gabriele", "Alessio"]

# for names in names:
#     print(f"Ciao {names} che dici di bello?????")


# 43-3. Your Own List: Think of your favorite mode of transportation, 
# such as a motorcycle or a car, and make a list that stores several examples. 
# Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”

# transportation: list = ["Tesla", "Ducati Panigale", "Lamborghini"]

# for vehicle in transportation:
#     print(f"I would like to own a {vehicle}.")


# If you could invite anyone, living or deceased, to dinner, who would you invite? 
# Make a list that includes at least three people you’d like to invite to dinner. 
# Then use your list to print a message to each person, inviting them to dinner.

# guests: list = ["Elon Musk", "Steve Jobs", "Bill Gates"]

# for guests in guests:
#     print(f"Hi {guests}, I would like to invite you to dinner.")


# 3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, 
# so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
# • Start with your program from Exercise 3-4. Add a print() call at the end of your program, 
# stating the name of the guest who can’t make it.
# • Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
# • Print a second set of invitation messages, one for each person who is still in your list.

# guests: list = ["Elon Musk", "Steve Jobs", "Bill Gates"]

# for guest in guests:
#     print(f"Hi {guest}, I would like to invite you to dinner.")

# print("Steve Jobs can't make it to dinner.")

# guests[1] = "Mark Zuckerberg"

# for guests in guests:
#     print(f"Hi {guests}, I would like to invite you to dinner.")


# 3-6. More Guests: You just found a bigger dinner table, so now more space is available. 
# Think of three more guests to invite to dinner.
# • Start with your program from Exercise 3-4 or 3-5. 
# Add a print() call to the end of your program, informing people that you found a bigger table.
# • Use insert() to add one new guest to the beginning of your list.
# • Use insert() to add one new guest to the middle of your list.
# • Use append() to add one new guest to the end of your list.
# • Print a new set of invitation messages, one for each person in your list.

# guests: list = ["Elon Musk", "Steve Jobs", "Bill Gates"]

# for guest in guests:
#     print(f"Hi {guest}, I would like to invite you to dinner.")

# print("I've just found a bigger table!")

# guests.insert(0, "Mark Zuckerberg")
# guests.insert(2, "Jeff Bezos")
# guests.append("Larry Page")

# for guest in guests:
#     print(f"Hi {guest}, I would like to invite you to dinner.")


# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, 
# and now you have space for only two guests.
# • Start with your program from Exercise 3-6. 
# Add a new line that prints a message saying that you can invite only two people for dinner.
# • Use pop() to remove guests from your list one at a time until only two names remain in your list. 
# Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t 
# invite them to dinner.
# • Print a message to each of the two people still on your list, letting them know they’re still invited.
# • Use del to remove the last two names from your list, so you have an empty list. 
# Print your list to make sure you actually have an empty list at the end of your program.

guests: list = ["Elon Musk", "Steve Jobs", "Bill Gates"]

print("I've just found a bigger table!")

guests.insert(0, "Mark Zuckerberg")
guests.insert(2, "Jeff Bezos")
guests.append("Larry Page")

for guest in guests:
    print(f"Hi {guest}, I would like to invite you to dinner.")

print("I can invite only two people for dinner.")

while len(guests) > 2:
    guest = guests.pop()
    print(f"Sorry {guest}, I can't invite you to dinner.")

for guest in guests:
    print(f"Hi {guest}, vieni alla mia cena.")

guests.clear()
print(guests)


# 3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
# • Store the locations in a list. Make sure the list is not in alphabetical order.
# • Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
# • Use sorted() to print your list in alphabetical order without modifying the actual list.
# • Show that your list is still in its original order by printing it.
# • Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
# • Show that your list is still in its original order by printing it again.
# • Use reverse()  to change the order of your list. Print the list to show that its order has changed.
# • Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
# • Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
# • Use sort() to change your list so it’s stored in reverse-alphabetical order.
# Print the list to show that its order has changed.

locations: list = ["New York", "Tokyo", "Paris", "London", "Rome"]
print(locations)
print(sorted(locations))
print(locations)
print(sorted(locations, reverse=True))
print(locations)
locations.reverse()
print(locations)
locations.reverse()
print(locations)
locations.reverse()
print(locations)
locations.sort()
print(locations)
locations.sort(reverse=True)
print(locations)
