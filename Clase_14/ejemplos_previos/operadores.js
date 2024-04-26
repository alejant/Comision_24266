i= 0;
console.info(i);
i= i+1;
console.info(i);
i++;
console.info(i);
i--;
console.info(i);
i+=1; // i= i+1
console.info(i);

// Operadores de asignación: == += -= ...
// Operadores aritméticos: + - * / % **
console.clear();
// Convertir de texto a número: parseInt
num1= parseInt(prompt("Ingrese un número:"));
num2= parseInt(prompt("Ingrese otro número:"));
suma= num1+num2;
console.log("Resultado:", suma);

// Operadores relacionales (o de comparación) -> true/false
console.log(num1>=0);
console.log(num1==0);
console.log(num1===0); // Compara valor y tipo de dato
console.log(num1!=5);

// Operadores lógicos
console.log(true&&true); // &&: AND / Y
console.log(true||true); // ||: OR / O
console.log(true&&false&&true); // &&: AND / Y
console.log(true||false||true); // ||: OR / O
console.log(!true);

// Operador ternario
console.log(num1>0 ? "Positivo" : "Negativo o cero.");
// Es equivalente a:
if (num1>0){
    console.log("Positivo");
} else {
    console.log("Negativo o cero.");
}
