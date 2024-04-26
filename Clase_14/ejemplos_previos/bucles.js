// ESTRUCTURAS DE CONTROL
// BUCLES / ITERATIVAS / REPETITIVAS
// While: Mientras
// Ciclo Exacto
var cont= 0; // Variable contadora
while (cont<5) {
    console.log(cont);
    cont++; // cont= cont+1;
}

// Ciclo condicional
/*cont= 0;
suma= 0;
var num= parseInt(prompt("Ingrese un número (-1 para finalizar)): ", ""));
while (num!=-1){
    cont++;
    suma+=num; // suma= suma+num;
    num= parseInt(prompt("Ingrese un número (-1 para finalizar)): ", ""));
}
console.log("Sumatoria: " + suma);
console.log("Cantidad de valores ingresados: " + cont);
*/
// Do-While: Hacer-Mientras (al menos se ejecuta 1 vez)
var num;
do {
    num= parseInt(prompt("Ingrese un número (-1 para finalizar)): ", ""));
} while (num!=-1);

// Ciclo FOR
for (let i=1; i<=10; i++){
    console.log(i);
}

// Su equivalente con while
var i= 1;
while (i<=10){
    console.log(i);
    i++
}

// Ciclo FOR con if
for (let i=1; i<=10; i++){
    if (i%2==0)
        console.log(i);

    if (i==6)
        break; // Esto no se recomienda. Resulta una mala práctica. 
}
