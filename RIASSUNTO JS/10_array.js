
// Array e metodi

const hobbies = ["sport", "cucina", "lettura"];
console.log(hobbies[0]); // sport

hobbies.push("lavoro");
console.log(hobbies);

const index = hobbies.findIndex(item => item === "sport");
console.log(index);

const modified = hobbies.map(item => item + "!");
console.log(modified);
