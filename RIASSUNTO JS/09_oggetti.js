
// Oggetti in JavaScript

const utente = {
  nome: "Rob",
  eta: 46,
  saluta: function () {
    console.log("Ciao!");
    console.log(this.nome);
  },
};
utente.saluta();

// Classi
class Utente {
  constructor(nome, eta) {
    this.nome = nome;
    this.eta = eta;
  }
  saluta() {
    console.log("Ciao! " + this.nome);
  }
}
const utenteUno = new Utente("Manuel", 35);
utenteUno.saluta();
