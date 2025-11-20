
// ===============================
// SPREAD OPERATOR
/*
Permette di "espandere" array e oggetti.
*/

const arr1 = [1, 2];
const arr2 = [3, 4];
const unito = [...arr1, ...arr2];
console.log(unito);

const base = { nome: "Anna" };
const esteso = { ...base, eta: 22 };
console.log(esteso);
