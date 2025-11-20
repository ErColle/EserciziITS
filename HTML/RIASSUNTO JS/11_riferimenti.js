
// ===============================
// ASSEGNAZIONE PER RIFERIMENTO
/*
Gli oggetti e gli array in JS sono passati per riferimento.
*/

const persona1 = { nome: "Mario" };
const persona2 = persona1;
persona2.nome = "Luigi";

console.log(persona1.nome); // "Luigi"

// Copia indipendente
const persona3 = { ...persona1 };
persona3.nome = "Carlo";
console.log(persona1.nome, persona3.nome);
