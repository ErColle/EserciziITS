
// ===============================
// ASYNC / AWAIT
/*
Sintassi moderna per lavorare con codice asincrono in modo leggibile.
*/

async function caricaDati() {
  try {
    const utente = await new Promise(res =>
      setTimeout(() => res({ nome: "Sara" }), 1000)
    );
    console.log("Utente caricato:", utente.nome);
  } catch (err) {
    console.log("Errore:", err);
  }
}

caricaDati();
