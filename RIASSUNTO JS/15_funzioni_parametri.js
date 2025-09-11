
// ===============================
// FUNZIONI COME PARAMETRI
/*
Le funzioni possono essere passate come argomenti.
*/

function esegui(fn) {
  console.log("Inizio...");
  fn();
  console.log("Fine...");
}

esegui(() => console.log("Funzione passata come parametro!"));

// setTimeout accetta una funzione come parametro
setTimeout(() => console.log("Ciao dopo 2 secondi"), 2000);
