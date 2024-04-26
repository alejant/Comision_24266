// Operaciones aritméticas
num1= 1-4;
num2= 10;
console.log(num1+num2);

// Declaración de variables
var num3;
console.log(num3);

// Asignación de valor a una variable
num3= 20.2;
console.log(num3);

// Declarar e inicializar la variable
var num4= 10; // Numérico
var numStr4= "10"; // String
var nombreApellidoCompleto= "Ramiro Escalante Leiva";
console.warn("Mi nombre es: " + nombreApellidoCompleto);

// Constantes
const PI= 3.14159;
radio= 10;
sup= PI*radio**2;
const VALOR_IVA= 21;
console.info(PI);

// Valores booleanos
var esPar= true;
console.error(esPar);

// Tipado dinámico
var numero= 5;
console.log(numero);
console.log(typeof numero);
numero= "5";
console.log(numero);

// Uso de typeof
console.log(typeof PI);
console.log(typeof(numero));
console.clear(); // Para limpiar la pantalla

// Objeto Math Fuente: https://www.w3schools.com/js/js_math.asp
radio= 10;
console.log(Math.PI*radio*2) // Perimetro 
console.log(Math.sqrt(4));
aleatorio= Math.random();
console.log(aleatorio*100);
console.log(Math.round(aleatorio*100));
console.log(Math.round(2.4999));
console.log(Math.round(2.5));
console.log(Math.ceil(aleatorio*100));
console.log(Math.floor(aleatorio*100));
console.log(Math.trunc(aleatorio*100));
console.log(Math.floor(-1.11));
console.log(Math.trunc(-1.11));
console.log(Math.pow(5,3));

console.log(parseInt("123"));
console.log(parseFloat("123.45"));
