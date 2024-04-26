// Condicional simple: if (solo)
num= parseInt(prompt("Ingrese un número: "));
// if (num%2==0) {
//     console.log("El numero es par."); // Bloque de verdad
// }

// Condicional doble: if-else
if (num%2==0) {
    console.log("El numero es par."); // Bloque de verdad
} else {
    console.log("El numero es impar."); // Bloque de falsedad
}

// Condicionales anidados
// if (num>0) {
//     alert("El número es positivo.");
// } else {
//     if (num<0) {
//         alert("El número es negativo.");
//     } else {
//         alert("El número es cero.");
//     }
// }

// else if: elif (Python)
// if (num>0) {
//     alert("El número es positivo.");
// } else if (num<0) {
//     alert("El número es negativo.");
// } else {
//     alert("El número es cero.");
// }

// ejemplo menú de opciones
// if (num==1) {
//     alert("Extraer");
// } else if (num==2) {
//     alert("Depositar");
// } else if (num==3) {
//     alert("Saldo de cuenta");
// } else {
//     alert("Ha ingresado una opción no válida!");
// }

// ejemplo menú de opciones: switch
// estructuras de selección múltiple
// https://www.w3schools.com/js/js_switch.asp
switch (num) {
    case 0:
    case 1:
        alert("Extraer");
        break;
    case 2:
        alert("Depositar");
        break;
    case 3:
        alert("Saldo de cuenta");
        break;
    default:
        alert("Ha ingresado una opción no válida!");
}

// Condicional compuesto
if (num>0) {
    if (num%2==0) {
        alert("Es positivo y par.");
    }
}

if ((num>0) && (num%2==0)) {
        alert("Es positivo y par.");
}

if ((num>0) || (num%2==0)) {
    alert("Es positivo y/o par.");
}
