
// Spread operator

const hobby1 = ["Nuoto", "Ciclismo"];
const hobby2 = ["Lettura"];
const unione = [...hobby1, ...hobby2];
console.log(unione);

const utente = { nome: "Mario", eta: 30 };
const utenteEsteso = { ...utente, isAdmin: true };
console.log(utenteEsteso);
