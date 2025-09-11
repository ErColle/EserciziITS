
// Destrutturazione

const userData = ["Rob", "Del"];
const [firstname, lastname] = userData;
console.log(firstname, lastname);

const user = { name: "Rob", age: 46 };
const { name, age } = user;
console.log(name, age);

// Alias
const { name: userName, age: userAge } = user;
console.log(userName, userAge);
