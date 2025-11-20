
// ===============================
// IMPORT & EXPORT
/*
Servono per organizzare il codice in più file (moduli).
*/

// --- util.js ---
export let API_KEY = "chiave_segreta";

// --- app.js ---
import { API_KEY } from "./util.js";
console.log(API_KEY);

// Export default
// --- util.js ---
export default "chiave_segreta";

// --- app.js ---
import chiave from "./util.js";
console.log(chiave);

// Import multiplo
// --- util.js ---
export let A = 10;
export let B = 20;

// --- app.js ---
import * as util from "./util.js";
console.log(util.A, util.B);
