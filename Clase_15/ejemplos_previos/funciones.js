// Declaración de la función "saludar"
function saludar () {
    console.log("Hola, soy una función!"); // Contenido de la función
}

// Ejecución de la función
saludar ();

// Tabla de multiplicar
// Declaración
function mostrarTablaDeMultiplicar(num) {
    console.log("Tabla de multiplicar de " + num.toString() + ":")
    for (var i = 1; i <= 10; i++)
        console.log(String(num) + " x " + String(i) + " = " + String(num * i));
}

// Ejecución
mostrarTablaDeMultiplicar(1); // Tabla del 1, calcula desde el 1 hasta el 10
mostrarTablaDeMultiplicar(5); // Tabla del 5, calcula desde el 1 hasta el 10

// Declaración
function promedio(a, b) {
    return (a+b)/2; // Devolvemos (retornamos) el promedio entre a y b
}

// Ejecución
// var a= 5, b= 7; // Asignación de valores a las variables
var a= Number.parseInt(prompt("Ingrese un número: "));
var b= Number.parseInt(prompt("Ingrese otro número: "));

var resultado = promedio(a,b); // Se guarda 10 en la variable "resultado"

console.log("El promedio entre " + a + " y " + b + " es: " + resultado);

/* 
Función Flecha (Arrow Functions):
https://developer.mozilla.org/es/docs/Web/JavaScript/Referencia/Funciones/Arrow_functions
https://www.youtube.com/watch?v=eXwEYSRk73U&ab_channel=Bluuweb%21
https://www.youtube.com/watch?v=aIKL5tQP25Y&ab_channel=DominiCode
*/

// Función tradicional 
function cuadrado(x){ 
    return x*x;
} 
console.log(cuadrado(2));

// Función Arrow
// var aCuadrado = x => x*x;
var aCuadrado = (x) => { return x*x; };
console.log(aCuadrado(2));
