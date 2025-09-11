
// Import Export in JavaScript
// Usati per organizzare il codice in moduli.

// --- util.js ---
export let API_KEY = "chiave_segreta";

// --- app.js ---
import { API_KEY } from "./util.js";
console.log(API_KEY);

// Export default
// --- util.js ---
export default "chiave_segreta";

// --- app.js ---
import myKey from "./util.js";
console.log(myKey);
