function fxEjemplo(nombre, edad){
    // console.log("Mi nombre es " + nombre + " y mi edad es " + edad);
    console.log(`Mi nombre es ${nombre} y mi edad es ${edad}`);
}

function suma(a,b){
    return a+b;
   }

fxEjemplo("Carlos", 32);

// Cadenas multinea
var cadena = `Línea número 1 de la cadena
Línea número 2 de la cadena`;
console.log(cadena);

var a=Number(prompt("ingrese un numero a:"));
var b=Number(prompt("ingrese un numero b:"));
console.log("la suma entre " + a + " y " + b + " es: " + suma(a,b));  //  la suma entre 12 y 21 es: 33
console.log(`la suma entre ${a} y ${b} es: ${suma(a,b)}`);          //  la suma entre 12 y 21 es: 33

// Luego de esto ver el ejemplo en carpeta "ej-template-string"
