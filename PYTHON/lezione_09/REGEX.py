""" ===========================================
GUIDA COMPLETA E DETTAGLIATA ALLE REGEX
===========================================

1. METACARATTERI BASE
---------------------
.     → Punto: matcha **qualsiasi carattere** (tranne newline)
        Esempio: `a.b` → matcha "acb", "a1b"
^     → Inizio stringa: matcha solo all’inizio
        Esempio: `^ciao` → matcha "ciao mondo"
$     → Fine stringa: matcha solo alla fine
        Esempio: `mondo$` → matcha "ciao mondo"
*     → 0 o più ripetizioni del pattern precedente
        Esempio: `a*` → "", "a", "aa"
+     → 1 o più ripetizioni
        Esempio: `a+` → "a", "aa"
?     → 0 o 1 occorrenza (opzionale)
        Esempio: `a?` → "", "a"
|     → OR logico (oppure)
        Esempio: `gatto|cane` → matcha uno dei due
()    → Raggruppamento
        Esempio: `(ab)+` → "ab", "abab"
[]    → Classe di caratteri (uno qualsiasi)
        Esempio: `[abc]` → "a", "b", "c"
[^]   → Classe negata
        Esempio: `[^0-9]` → tutto tranne numeri
{}    → Quantificatore
        Esempi:
        `a{3}` → "aaa"
        `a{2,}` → almeno due a
        `a{2,4}` → da due a quattro a

------------------------------------------------------------

2. CLASSI PREDEFINITE (SHORTHAND)
---------------------------------
\d    → Cifra (digit) [0-9]
\D    → Non cifra
\w    → Carattere alfanumerico + underscore [a-zA-Z0-9_]
\W    → Tutto tranne \w
\s    → Spazio bianco (spazio, tab, newline, ecc.)
\S    → Non spazio bianco
\b    → Confine di parola (utile per parole intere)
\B    → Non confine di parola (interno a una parola)

------------------------------------------------------------

3. QUANTIFICATORI
-----------------
*       → 0 o più volte
+       → 1 o più volte
?       → 0 o 1 volta
{n}     → esattamente n volte
{n,}    → almeno n volte
{n,m}   → tra n e m volte

Esempi:
`a{3}`     → matcha "aaa"
`a{2,}`    → matcha "aa", "aaa", ...
`a{2,4}`   → matcha "aa", "aaa", "aaaa"

------------------------------------------------------------

4. LOOKAHEAD E LOOKBEHIND
--------------------------
(?=...)    → Lookahead positivo (matcha se dopo c'è ...)
(?!...)    → Lookahead negativo (matcha se dopo NON c'è ...)
(?<=...)   → Lookbehind positivo (matcha se prima c'è ...)
(?<!...)   → Lookbehind negativo (matcha se prima NON c'è ...)

Esempi:
`\d(?=€)`      → cifra seguita da € (es. "5€")
`\d(?!€)`      → cifra non seguita da €
`(?<=€)\d`     → cifra preceduta da €
`(?<!€)\d`     → cifra non preceduta da €

------------------------------------------------------------

5. FLAG (MODIFICATORI)
----------------------
Usati in Python con re.compile() o in altri linguaggi con sintassi /.../flags

re.I     → Ignore case (non fa distinzione tra maiuscole/minuscole)
re.M     → Multiline: ^ e $ funzionano su ogni riga
re.S     → Dotall: "." include anche i newline
re.X     → Verbose: permette spazi e commenti nella regex

Esempio:
```python
re.compile(r'^ciao', re.I | re.M)
 """