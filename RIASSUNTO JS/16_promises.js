
// ===============================
// PROMISE
/*
Le Promise rappresentano operazioni asincrone.
*/

const miaPromise = new Promise((resolve, reject) => {
  setTimeout(() => {
    let successo = true;
    if (successo) resolve("Operazione completata!");
    else reject("Errore!");
  }, 1000);
});

miaPromise
  .then(risultato => console.log(risultato))
  .catch(err => console.log(err));
