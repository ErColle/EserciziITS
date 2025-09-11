
// Approfondimento su this

// Funzione normale -> this dinamico
function mostraNome() {
  console.log(this.nome);
}
const persona = { nome: "Max", mostraNome };
persona.mostraNome(); // "Max"

// Funzione freccia -> this lessicale
const persona2 = {
  nome: "Anna",
  mostraNome: function () {
    setTimeout(() => {
      console.log(this.nome);
    }, 1000);
  },
};
persona2.mostraNome();
