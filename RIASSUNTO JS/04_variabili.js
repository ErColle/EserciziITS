
// Variabili in JavaScript
// Possiamo usare let, const e var.

// Esempio con let
let nome = "Mario";
let eta = 30;
nome = "Luigi"; // riassegnazione possibile

// Esempio con const
const piGreco = 3.14159;
// piGreco = 3.15; // Errore! Non si può riassegnare

// Tipi diversi
let stringa = "Ciao";
let numero = 42;
let booleano = true;
let nullo = null;
let indefinito;

// Differenza con var (function scope + hoisting)
console.log(a); // undefined (hoisting)
var a = 5;
console.log(a); // 5
