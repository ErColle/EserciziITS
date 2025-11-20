
// ===============================
// APPROFONDIMENTO SU 'this'
/*
- Nelle funzioni classiche, this dipende da chi chiama la funzione
- Nelle funzioni freccia, this è legato al contesto in cui la funzione è scritta
*/

function mostraNome() {
  console.log(this.nome);
}

const persona = { nome: "Anna", mostraNome };
persona.mostraNome(); // "Anna"

// Arrow function mantiene il contesto
const persona2 = {
  nome: "Luca",
  mostraNome: function () {
    setTimeout(() => {
      console.log(this.nome); // "Luca"
    }, 500);
  },
};
persona2.mostraNome();
