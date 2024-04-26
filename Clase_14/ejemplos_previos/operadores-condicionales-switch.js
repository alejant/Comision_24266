// MATERIAL EXTRA
// Cómo solicitar datos por teclado
var numTeclado= parseInt(prompt("Ingrese un número por teclado: ", ""));

// OPERADORES
// Operadores aritméticos: + - / * ** % ++ --
resultado= 5*2;
console.log("Resultado: " + resultado); // Se concatena sin necesidad de convertir el número a String
resultado--;
console.log("Resultado: " + resultado);
resultado= 5**2;
console.log("Resultado: " + resultado);
resultado= 9**(1/2);
console.log("Resultado: " + resultado);

// Operadores de asignación
num= 0;
num= num+2;
num+= 2;
console.log("Número: " + num);
num-= 2;
console.log("Número: " + num);

// Operadores Relacionales
var A= 5;
var B= 2;
console.log(A==B); // false
console.log(A!=B); // true
console.log(A>=B); // true

// Operadores Lógicos
// AND: &&, OR: ||, NOT: !
console.log(A>=5-2 && B==0) // AND: todos tienen que ser true para que la condición COMPUESTA sea true
console.log(true&&true); // true
console.log(true&&false); // false
console.log(true||false); // true
console.log(false||false); // false

// Operadores de cadena
texto1= "Ramiro";
texto2= "Escalante Leiva"
texto3= texto1+texto2;
console.log(texto3); // RamiroEscalante Leiva
texto3= texto1+" "+texto2;
console.log(texto3); // Ramiro Escalante Leiva
texto1+=texto2;
console.log(texto1); // RamiroEscalante Leiva

// ESTRUCTURAS DE CONTROL
// Condicionales
var num= parseInt(prompt("Ingrese un número por teclado: ", ""));
// Condicional Simple
// Ejemplo: evaluar si un número es positivo.
if (num>0){
    alert("El número es positivo");
}

// Condicional Doble
// Ejemplo: evaluar si un número es positivo o no.
if (num>0){ // Bloque de Verdad
    alert("El número es positivo.");
}
else { // Bloque de Falsedad
    alert("El número es negativo o cero.");
}

// Condicional Anidado
// Ejemplo: evaluar si un número es positivo, negativo o cero.
if (num>0) { // Bloque de Verdad
    alert("El número es positivo.");
} 
else {
    if (num<0){
        alert("El número es negativo.");
    }
    else {
        alert("El número es cero.");
    }
}

// else-if: elif -> NO existe en JavaScript. Si en Python. En JS tenemos la combinación else if.
if (num>0){ // Bloque de Verdad
    alert("El número es positivo.");
}
else if (num<0){
    alert("El número es negativo.");
}
else {
    alert("El número es cero.");
}

// Switch: https://www.w3schools.com/js/js_switch.asp
// Ejemplo: menú de opciones.
var menu= parseInt(prompt("Ingrese una opción: ", ""));
switch(menu) {
    case 1:
        console.log("Opción 1.");
        break;
    case 2:
    case 3:
        console.log("Opción 2 o 3.");
        break;
    default:
        console.log("Opción por defecto.");
}

// Operador ternario
var num= parseInt(prompt("Ingrese un número por teclado: ", ""));
console.log(num>0 ? "Positivo" : "Negativo o cero");
