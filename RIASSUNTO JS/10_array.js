
// ===============================
// ARRAY E METODI
/*
Gli array servono a contenere liste ordinate di valori.
*/

const hobbies = ["sport", "cucina", "lettura"];
console.log(hobbies[0]);

// Aggiungere elementi
hobbies.push("viaggio");

// Map -> trasforma elementi
const nuovi = hobbies.map(h => h + "!");
console.log(nuovi);

// findIndex -> trova posizione
const index = hobbies.findIndex(h => h === "cucina");
console.log(index);
