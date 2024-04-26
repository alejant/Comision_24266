// Operadores aritmeticos
// https://developer.mozilla.org/es/docs/Learn/JavaScript/First_steps/Math
// https://developer.mozilla.org/es/docs/Web/JavaScript/Guide/Expressions_and_Operators
/*
Operadores Aritméticos
+: Suma 
-: Resta 
*: Multiplicación 
**: Exponenciación 
/: División (división entera con Math.trunc)
%: Módulo: resto de dividir 
i++: operador de incremento (incrementa i en 1)
i--: operador de decremento (decrementa i en 1)
*/

i= 0
i++;
i= i+1;
i+=2; // i= i+2;
console.warn(i);

/*
Operadores posfijo y prefijo
i++: incremento posfijo    a=i++    primero a=i y despues i=i+1
++i: incremento prefijo    a=++i    primero i=i+1 y despues a=i
i--: decremento posfijo    a=i--    primero a=i y despues i=i-1
--i: decremento prefijo    a=--i    primero i=i-1 y despues a=i
*/

// Operadores de bit a bit
console.log(5&1); // AND a nivel de bits: 0101 & 0001 = 0001 -> 1
console.log(5|2); // OR a nivel de bits:  0101 & 0010 = 0111 -> 7
console.log(~9); // NOT a nivel de bits: ~ 0000 0000 ... 0000 1001 = 1111 1111 ... 1111 0110 -> -10
console.log(5^1); // XOR: 0101 ^ 0001 = 0100 = 4
console.log(9<<2); // Desplazamiento a la izquierda (<<). 9<<2 produce 36, porque 1001 desplazado 2 bits a la izquierda se convierte en 100100, que es 36.
console.log(5>>1); // Desplazamiento a la derecha de propagación de signo (>>). 5>>1 produce 2, porque 1001 desplazado 1 bit a la derecha se convierte en 10, que es 2.
