
// ===============================
// VARIABILI IN JAVASCRIPT
/*
Tipi principali: let, const, var
- let: variabile modificabile
- const: costante (non modificabile)
- var: vecchia sintassi, da evitare
*/

let nome = "Mario";
nome = "Luigi"; // posso riassegnare

const PI = 3.14;
// PI = 3.15 -> Errore!

// Differenza con var (hoisting)
console.log(a); // undefined
var a = 5;
console.log(a); // 5

// Vari tipi di valori
let numero = 42;
let stringa = "Ciao!";
let booleano = true;
let nullo = null;
let indefinito;
