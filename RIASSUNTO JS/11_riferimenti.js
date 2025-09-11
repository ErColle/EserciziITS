
// Assegnazione per riferimento

const persona1 = { nome: "Mario" };
const persona2 = persona1;
persona2.nome = "Luigi";
console.log(persona1.nome); // Luigi

const array1 = [1, 2, 3];
const array2 = array1;
array2.push(4);
console.log(array1); // [1,2,3,4]

// Copie indipendenti
const persona3 = Object.assign({}, persona1);
const array3 = [...array1];
