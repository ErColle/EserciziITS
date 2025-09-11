
// Introduzione alle Promise

const miaPromise = new Promise((resolve, reject) => {
  setTimeout(() => {
    const successo = true;
    if (successo) resolve("Operazione completata!");
    else reject("Errore!");
  }, 2000);
});

miaPromise.then(r => console.log(r)).catch(e => console.log(e));
