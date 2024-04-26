function retornarMultiplo2(numero) {
    return numero*2; 
}
let resultado = retornarMultiplo2(2);

let variableQueGuardaFuncion = (numeroP) => numeroP * 2;
resultado = variableQueGuardaFuncion(4);

if (variableQueGuardaFuncion(3) > 10) {
    ///Hacer cosas locas
}


function saludarJubilado(nombre) {
    let numero = 4;
    alert(`Hola pobre ${nombre}`);

    function adiosGente(dato) {
        alert(`Adios ${dato} ${numero} veces`);
    }

    adiosGente(nombre);
}




function calcularJubilacion(nombre, edad, jubilacion, funcionEjecutable) {
    if (edad > 60 || jubilacion < 100000) {
        funcionEjecutable(nombre);   
    }
}

// adiosGente("pepe");


calcularJubilacion("Juan",30, 10000000, saludarJubilado);
calcularJubilacion("Perez", 70, 10000000, saludarJubilado);


let persona = {
    nombre: "Ale",
    apellido: "hunt"
}

let otraPersona = new Object();
otraPersona.nombre = "Pepe";
otraPersona.apellido = "Argento";
otraPersona.edad = 33;

console.log(typeof (persona));
console.log(typeof (otraPersona));



