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


// calcularJubilacion("Juan",30, 10000000, saludarJubilado);
// calcularJubilacion("Perez", 70, 10000000, saludarJubilado);


let persona = {
    nombre: "Ale",
    apellido: "hunt"
}

let otraPersona = new Object();
otraPersona.nombre = "Pepe";
otraPersona.apellido = "Argento";
otraPersona.edad = 33;

new Object();


console.log(typeof (persona));
console.log(typeof (otraPersona));



class Prestamo {
    constructor(beneficiario, monto, cuotas) {
        this.el_beneficiario = beneficiario;
        this.el_monto = monto;
        this.cantidad_cuotas = cuotas;
    }

    retornarTasa() {
        let tasa;
        if (this.el_beneficiario === "Alejandro") {
            tasa = 0;
        } else {
            if (this.cantidad_cuotas > 6) {
                tasa = 500;
            } else {
                tasa = 300;
            }
        }

        return tasa;
    }
}

let un_monto = 1000000;
let un_bene = "Alejandro";
let las_cuotas = 6;

let mi_prestamo = new Prestamo(un_bene, un_monto, las_cuotas);
let prestamo_alfredo = new Prestamo("Alfredo", 10000, 8);
let segundo_prestamo_alfredo = new Prestamo("Alfredo", 10000, 8);
//let segundo_prestamo_alfredo = prestamo_alfredo;
let basta_prestamo = new Prestamo("Carlos", 6000, 3);

console.log(typeof mi_prestamo);
console.log(typeof prestamo_alfredo);
console.log(typeof segundo_prestamo_alfredo);
console.log(typeof basta_prestamo);
console.log(mi_prestamo === prestamo_alfredo);
console.log(prestamo_alfredo === segundo_prestamo_alfredo);
// Asigno el objeto de prestamo_alfredo en la variable segundo_prestamo_alfredo y lo
// que había en esta segunda variable se pierde
segundo_prestamo_alfredo = prestamo_alfredo;
//Y ahora si son iguales
console.log(prestamo_alfredo === segundo_prestamo_alfredo);
document.write(`<h1>Tenes una tasa de ${mi_prestamo.retornarTasa()}% </h1>`); 

let array = ["Hola", 3, 0];


