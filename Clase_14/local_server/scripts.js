console.info("Comienzo de los ejemplos");
let primerVariable = 1;
let segundaVariable = "1";

console.log("Son iguales?: " + (primerVariable == segundaVariable));
console.log("Son iguales?: " + (primerVariable === segundaVariable));
console.log("Son distintos?: " + (primerVariable != segundaVariable));
console.log("Son distintos?: " + (primerVariable !== segundaVariable));

let edadIngresada = parseInt(prompt("Ingrese su edad "));
let sueldoIngresado = parseInt(prompt("Ingrese su sueldo"));

if (edadIngresada <= 18 && sueldoIngresado < 100000) {
    document.write("<h1> Página para pobres </h1> ");
} else {
    document.write("<h1> Segui sobreviviendo </h1> ");
}


if (edadIngresada == 1) {
    console.log("tenes un año");
} else if (edadIngresada == 2) {
    console.log("tenes dos años");
}else if (edadIngresada == 3) {
    console.log("tenes tres años");
} else {
    console.log("tenes otra edad que no sea ni uno ni dos ni tres");
}

if (edadIngresada == 1) {
    console.log("un años")
} else {
   
}

edadIngresada == 1 ? console.log("un años") : console.log("cualquier cosa");

switch (edadIngresada) {
    case 1:
        console.log("tenes un año");
        break;
    case 2:
        console.log("tenes dos años");
        break
    case 3:
        console.log("tenes tres años");
        break
    default:
        console.log("tenes otra edad que no sea ni uno ni dos ni tres");
        break;
}

for (let i = 0; i < 20; i++) {
    console.log(i);
   
}

let frenarIngreso = false;

while (!frenarIngreso) {
    let nombre = prompt("Ingrese su nombre")
    console.log("Welcome " + nombre);
    if (nombre == "diego") {
        frenarIngreso = true;
    }
}

// Código de satán
// while (true) {
//     let nombre = prompt("Ingrese su nombre")
//     console.log("Welcome " + nombre);
//     if (nombre == "diego") {
//         break
//     }
// }

do {
    console.log("do while");
} while (!frenarIngreso);


let valorDeVerdad = true;

if (valorDeVerdad) {
    
}










