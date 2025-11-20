
// ===============================
// OGGETTI
/*
Gli oggetti raggruppano proprietà e metodi.
*/

const utente = {
  nome: "Mario",
  eta: 30,
  saluta: function () {
    console.log("Ciao! Sono " + this.nome);
  },
};

utente.saluta();

// Con classi (ES6)
class Utente {
  constructor(nome, eta) {
    this.nome = nome;
    this.eta = eta;
  }
  descrizione() {
    console.log(this.nome + " ha " + this.eta + " anni.");
  }
}

const u1 = new Utente("Giulia", 25);
u1.descrizione();
