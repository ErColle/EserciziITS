#COMPREHENSION
#MODO PER COMPATTARE I LOOP

#CON ESSE NON SI POSSONO MODIFICARE E ELIMINARE ELEMENTI E LISTE

[ x + 1 for x in range(20) if x % 2 == 0]
# Do this (x + 1)for this collection (for x in range(20) in this situation (x % 2 == 0)


#Examples
# Traditional loop 
squares = []
for x in range(10):
    if x % 2 == 0:
        squares.append(x**2)

#Comprehension
squares = [x**2 for x in range(10) if x % 2 == 0]











