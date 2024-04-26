var miNumero = 3;

function serInservible() {
    console.log("No sirvo para nada");
    console.log("Todavia tengo esperanzas");
}


function informarEdadPorConsola(nombre, apellido, numeroEdad = 0) {
    console.log(`La edad de ${nombre}, ${apellido} es ${numeroEdad}`);
    console.log("La edad de "+nombre+","+ apellido +" es "+numeroEdad);
}

function saludar() {
    alert("Holaaaaa");
}

function calcularJubilacionFutura() {
    let inputEdad = document.getElementById("inputEdad");
    let inputJubilacion = document.getElementById("inputJubilacion");

    let edad = parseInt(inputEdad.value);
    let jubilacion = parseInt(inputJubilacion.value);
    let diaActual = calcularDiaActual();
    
    if (edad > 80 && jubilacion < 2000000 || diaActual == 24) {
        let elementoLabel = document.getElementById("lblJubilacion");
        elementoLabel.innerHTML = "No le va a servir para nada..";
    } else {
        let elementoHtml = document.getElementById("lblJubilacion");
        //let lblMensaje = "<label id="lblJubilacion"> ??? </label>"
        elementoHtml.innerHTML = "<h1>Por ahi le sirve hasta los 80..</h1>";
        //document.getElementById("lblJubilacion").innerHTML = "<h1>Por ahi le sirve hasta los 80..</h1>";
    }
}


function calcularDiaActual() {
    let diaActual = 300;
    diaActual = 25;
    diaActual = 24;
    return diaActual;
    diaActual = 26; //Esto está al pedo
}

serInservible();
informarEdadPorConsola("Alberto", "Hunt", 101, 102);
informarEdadPorConsola();
