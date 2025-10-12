
# RSA 

# Kpub, Kpriv -> numeri di interi di grandi dimensioni
# kpub(e, n)
# Kpriv(d, n)                A -----> B       --> operazione di cifratura pow(M, e) % n --> mess cifrato
                                                                                            # (num int)              
#                     A cifra con la chiave Kpub di B     (M MESSAGGIO)                 

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

# decodifico il messaggio con la chiave privato

with open('chiave_priv.txt') as cv:
    chiave_priv = cv.read()
    
chiave_priv = chiave_priv.replace(':', '')
chiave_priv = chiave_priv.replace('\n', '')
chiave_priv = chiave_priv.replace(' ', '')

print("\n\nChiave privata:", chiave_priv)

# Converto la chiave privata in intero
chiave_priv = int(chiave_priv, 16)

# Decodifico il messaggio
messaggio_decrittografato = pow(messaggio_crittografato, chiave_priv, modulo)

print("\n\n",messaggio_crittografato)

for chars in range(0, messaggio_crittografato + 1, ):
    
    

# Converto indietro in testo
# messaggio_decrittografato_bytes = bytes.fromhex(hex(messaggio_decrittografato)[2:])
# messaggio_decrittografato_testo = messaggio_decrittografato_bytes.decode('utf-8')

print("\n\nMessaggio decifrato:", messaggio_decrittografato_testo)






