
// ===============================
// FUNZIONI FRECCIA
/*
Sintassi più compatta per scrivere funzioni.
*/

// Classica
function saluta(nome) {
  console.log("Ciao " + nome);
}

// Freccia
const salutaFreccia = (nome) => {
  console.log("Ciao " + nome);
};

salutaFreccia("Luca");

// Esempio veloce (callback)
setTimeout(() => console.log("Eseguito dopo 2 secondi"), 2000);
