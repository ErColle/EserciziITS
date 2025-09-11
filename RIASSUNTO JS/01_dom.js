
// ===============================
// COS'È IL DOM?
/*
Il DOM (Document Object Model) è una rappresentazione ad albero della pagina web.
Ogni elemento HTML diventa un oggetto che può essere manipolato con JavaScript.
*/
 
// Selezione di un elemento tramite id
const titolo = document.getElementById("titolo");

// Modifica del contenuto testuale
titolo.textContent = "Nuovo Titolo";

// Modifica dello stile
titolo.style.color = "red";

// Creazione dinamica di un nuovo elemento
const nuovoParagrafo = document.createElement("p");
nuovoParagrafo.textContent = "Questo paragrafo è stato aggiunto con JS.";
document.body.appendChild(nuovoParagrafo);
