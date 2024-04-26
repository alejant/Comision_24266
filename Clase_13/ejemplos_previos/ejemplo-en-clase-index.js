// 3 formas de mostrar info:
console.log("Hola Mundo!");
console.log("1+2");

document.write("Hola Mundo en HTML!");
// alert("Hola Pop!");

// Como hacer calculos aritméticos
num1= 1+4;
num2= 10;
console.log(num1+num2)

// Declaración de una variable
var num3;
console.log(num3)
// Asignación de un valor a una variable
num3= 10;
console.log(num3)

// Declaración y asignación de un valor
var num4 = 5;
var numStr4= "5";
var nombApellido= "Ramiro Escalante Leiva";
console.warn(nombApellido);

// Constantes
const PI= 3.14159;
const VALOR_IVA= 21;
console.info(PI);

// Valores booleanos
// esPar= false;
var esPar= true;
console.info(esPar);

// Ejemplo tipado dinámico
var numero= 5;
console.log(numero);
numero= "50";
console.log(numero);

// Uso de typeof
numero= 5;
tipoDeDato= typeof numero;
console.log(tipoDeDato);
numero= "50";
console.log(typeof numero);

// Objeto Math: https://www.w3schools.com/js/js_math.asp
radio= 10;
console.log(Math.PI*radio*2);
console.log(Math.SQRT2);
console.log(Math.sqrt(9));
console.log(Math.pow(3,2));
console.log(Math.random());
console.log(Math.round(2.5));
console.log(Math.round(2.4999999999999));
console.log(Math.floor(2.5));
console.log(Math.trunc(2.5));

console.log(parseInt("123"));
console.log(parseFloat("123"));
console.log(parseFloat("123.456"));
