
// Async / Await

async function caricaDati() {
  try {
    const utente = await new Promise(res =>
      setTimeout(() => res({ nome: "Mario" }), 1000)
    );
    console.log("Utente:", utente.nome);
  } catch (err) {
    console.log("Errore:", err);
  }
}
caricaDati();
