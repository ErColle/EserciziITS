
// Funzioni freccia (Arrow functions)
const saluta = (nome, messaggio) => {
  console.log(nome + ": " + messaggio);
};
saluta("Max", "Ciao");

// Uso tipico: callback in React o JS
// <button onClick={() => saluta("Max", "Ciao")}>Click</button>
