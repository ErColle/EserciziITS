# elementi pubblici
n = 3456  # numero modulo (in realtà dovrebbe essere un primo, ma ok per l’esempio)
p = 123   # base pubblica

# segreti
a = 564  # segreto di Alice
b = 645  # segreto di Bob

# Alice calcola la sua chiave pubblica
def key_pubb_a(p, a, n) -> int:
    return pow(p, a, n)

# Bob calcola la sua chiave pubblica
def key_pubb_b(p, b, n) -> int:
    return pow(p, b, n)

# calcolo delle chiavi pubbliche
A = key_pubb_a(p, a, n)
B = key_pubb_b(p, b, n)

print("Chiave pubblica di Alice:", A)
print("Chiave pubblica di Bob:", B)

# ciascuno calcola la chiave segreta condivisa
K_Alice = pow(B, a, n)
K_Bob = pow(A, b, n)

print("Chiave segreta di Alice:", K_Alice)
print("Chiave segreta di Bob:", K_Bob)
print("Uguali?", K_Alice == K_Bob)
