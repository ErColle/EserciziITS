
// Funzioni come parametri

setTimeout(() => {
  console.log("Sono passati 3 secondi!");
}, 3000);

function greeter(greetFn) {
  console.log("Inizio saluto...");
  greetFn();
  console.log("Fine saluto.");
}
greeter(() => console.log("Ciao a tutti!"));
