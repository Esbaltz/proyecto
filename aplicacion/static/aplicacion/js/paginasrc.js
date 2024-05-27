function infpa() {
    document.getElementById("form2").addEventListener("submit", function (event) {
        var tarjeta = document.getElementById("tarjeta").value;
        var caducidad = document.getElementById("caducidad").value;
        var seguridad = document.getElementById("seguridad").value;
        var tarjetaError = document.getElementById("tarjetaError");
        var caducidadError = document.getElementById("caducidadError");
        var seguridadError = document.getElementById("seguridadError");

        tarjetaError.innerHTML = "";
        caducidadError.innerHTML = "";
        seguridadError.innerHTML = "";

        if (tarjeta.length < 16 || tarjeta.length > 16 || isNaN(tarjeta)) {
            tarjetaError.innerHTML = "Ingrese un número de tarjeta válido. (16 caracteres)";
            event.preventDefault();
        }
        if (caducidad.length !== 5 || !/^\d{2}\/\d{2}$/.test(caducidad)) {
            caducidadError.innerHTML = "Ingrese una fecha de caducidad válida (MM/AA).";
            event.preventDefault();
        }
        if (seguridad.length < 3 || seguridad.length > 4 || isNaN(seguridad)) {
            seguridadError.innerHTML = "Ingrese un código de seguridad válido.";
            event.preventDefault();
        }
    });

    flatpickr("#caducidad", {
        dateFormat: "m/y",
        minDate: "today",
        disableMobile: true
    });
}

function nos(selector) {
    flatpickr(selector, {
        dateFormat: "m/y",
        minDate: "today",
        disableMobile: true
    });
}

function formdom(){
    document.getElementById("form1").addEventListener("submit", function (event) {
        var domicilio = document.getElementById("domicilio").value;
        var casa = document.getElementById("casa").value;
        var region = document.getElementById("region").value;
        var direccionError = document.getElementById("direccionError");
        var casaError = document.getElementById("nCasaError");
        var regionError = document.getElementById("regionError");

        direccionError.innerHTML = "";
        casaError.innerHTML = "";
        regionError.innerHTML = "";

        if (domicilio.length < 3 || domicilio.length > 30) {
            direccionError.innerHTML = "La dirección debe tener entre 3 y 30 caracteres.";
            event.preventDefault();
        }
        if (casa.length < 1 || casa.length > 10 || isNaN(casa)) {
            casaError.innerHTML = "Ingrese un número de casa válido.";
            event.preventDefault();
        }
        if (region === "") {
            regionError.innerHTML = "Seleccione una región.";
            event.preventDefault();
        }
    });
}