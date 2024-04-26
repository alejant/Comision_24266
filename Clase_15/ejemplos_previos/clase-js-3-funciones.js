// Declarar una función
function tabla(num, hasta=10){ // Parámetros por defecto
    // var num= 3;
    for (i= 1; i<=hasta; i++) {
        console.log("Tabla: ", num, " x ", i, "= ", num*i);
    }

    // Al no tener un return, la función devuelve: undefined
}

/*
pre: recibe dos números.
pos: devuelve el resultado de la suma.
*/
function sumar(num1, num2){
    var suma= num1+num2;
    return suma; // Devuelve un valor 
}

/*
pre: recibe dos números.
pos: devuelve el valor del máximo, si son iguales devuelve "".
*/
function obtenerMaximo(num1, num2) {
    if (num1!=num2){
        if (num1>num2){
            maximo= num1;
        } else {
            maximo= num2;
        }
        return maximo; // Al ejecutarse un return, sale de la función
    }
    return ""; // Cadena vacía // Se recomienda un único return, y al final
}

/*
pre: recibe dos números.
pos: devuelve el valor del máximo, si son iguales devuelve indefinido.
*/
function obtenerMaximo(num1, num2) {
    if (num1!=num2){
        if (num1>num2){
            maximo= num1;
        } else {
            maximo= num2;
        }
        return maximo; // Al ejecutarse un return, sale de la función
    }
}

// Ejemplo Función Flecha
function cuadrado(num){
//    resultado= x*x;
//    return resultado;
    return num*num;
}

// Función Arrow
var aCuadrado= num => num*num;
var aSumar= (num1, num2) => num1+num2;

// Programa Ppal
// Llamada/Invocar a mi función
/*
// Una tabla de multiplicar
var num= 3;
for (i= 1; i<=10; i++) {
    console.log("Tabla: ", num, " x ", i, "= ", num*i);
}

var hasta= 5;
var numero= parseInt(prompt("Ingrese un número para mostrar su tabla de multiplicar: ", ""))
tabla(numero);
tabla(numero, 3);
tabla(3, hasta);
console.log(sumar(5,2));
resultado= sumar(10,20);
console.log(resultado);
console.log(obtenerMaximo(5,2));
console.log(obtenerMaximo(1,2));
console.log(obtenerMaximo(5,5));

// Llamada a una fx de flecha
console.log(cuadrado(2));
console.log(aCuadrado(3));
console.log(aSumar(3,2));

// Ejemplos de alcance (scope)
console.log(sumar(5,2));
console.log(suma);
*/

// Ejemplo 2 de scope: variable GLOBAL (No recomendado)
var msj = "Hola Mundo!";

function mostraPorConsola(){
    console.log(msj);
    msj= "Hola Ramiro!";
}

// Ejemplo 2 de scope: variable GLOBAL (No recomendado)
function mostraPorConsola2(msj){
    console.log(msj);
}

// Ejemplo 3 de scope: si modifico una variable en el ámbito de una fx, sólo se modifica en la fx.
function mostraPorConsola3(msj){
    console.log(msj);
    msj= "Hola Ramiro3!"
}

mostraPorConsola();
console.log("msj", msj);
mostraPorConsola2("Hola Ramiro2!");
console.log("msj", msj);
mostraPorConsola3("Hola Ramiro2!");
console.log("msj", msj);
