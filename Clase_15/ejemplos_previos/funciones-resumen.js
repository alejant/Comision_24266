// Declaración de fx
function saludar(){
    console.log("hola mundo!");
}

function saludarNombre(nombre){
    let cont= 0; // let para limitar el alcance de la variable
    console.log("hola " + nombre + " " + apellido);
}

function sumar(a,b){
    return a+b;
}

var aSumar = (a,b) => a+b;

// function maximo(num1, num2){
//     if (num1>num2) {
//         return num1;
//     } else {
//         return num2;
//     }
//     // instrucciones...
// }

function maximo(num1, num2){
    if (num1>num2) {
        numMax= num1;
    } else {
        numMax= num2;
    }
    return numMax;
    // instrucciones...
}

// Función que retorne true o false
// function esPar(num) {
//     if (num%2==0){
//         es= true;
//     } else {
//         es= false;
//     }
//     return es;
// }

function esPar(num) {
    /*
    pre: recibe un número.
    pos: devuelve true si es par. 
    */
    return num%2==0;
}

// Funciones FLECHA
var aEsPar = num => num%2==0;

// Prog ppal
// miNombre= prompt("Ingrese su nombre: ");
// apellido= prompt("Ingrese su apellido: ");
// Invocar/llamar
console.log(saludar());
// saludarNombre(miNombre);
// console.log(nombre);
// console.log(cont);

var suma= sumar(1,4);
console.log(suma);

num= 4;
if (aEsPar(num)){
    console.log("El número", num, "es PAR.");
} else {
    console.log("El número", num, "es IMPAR.");
}

