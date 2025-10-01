mess = "ciao messaggio"

# traduzione messaggio in numeri

mess = int(mess.encode('utf-8').hex(), 16)

print("MESSAGGIO CONVERTITO IN ESADECIMALE:", mess)

# publicExponent: 3 (0x3) chiave pubblica
# prendo il modulo dal file modulo.txt

with open('modulo.txt') as m:
    modulo = m.read()
    
# tolgo al modulo : e accapo
modulo = modulo.replace(':', '')
modulo = modulo.replace('\n', '')
modulo = modulo.replace(' ', '')

modulo = int(modulo, 16)

print("\n\nMODULO:", modulo)

# crittografo il messaggio con la il messaggio convertito in intero
# per la potenza della chiave pubblica, per il modulo del modulo
messaggio_crittografato = pow(mess, 3) % modulo

print("\n\n\nmessaggio crittografato:", messaggio_crittografato)

# decodifico il messaggio con la chiave privata
