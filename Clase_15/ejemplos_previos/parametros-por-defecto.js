// https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Functions/Default_parameters
function multiply(a, b = 1) {
    return a * b;
  }
  
console.log(multiply(5, 2));
// expected output: 10

console.log(multiply(5));
// expected output: 5
