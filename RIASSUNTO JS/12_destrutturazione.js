
// ===============================
// DESTRUTTURAZIONE
/*
Permette di estrarre valori da array o oggetti in modo compatto.
*/

const dati = ["Mario", 30];
const [nome, eta] = dati;
console.log(nome, eta);

const user = { nome: "Luca", eta: 25 };
const { nome: n, eta: e } = user;
console.log(n, e);
