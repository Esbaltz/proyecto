function formini (){
    document.getElementById("registroForm").addEventListener("submit", function (event) {
        var nombreCuenta = document.getElementById("nombreCuenta").value;
        var password = document.getElementById("password").value;
        var nombreCuentaError = document.getElementById("nombreCuentaError");
        var passwordError = document.getElementById("passwordError");

        nombreCuentaError.innerHTML = "";
        passwordError.innerHTML = "";

        if (nombreCuenta.length < 3 || nombreCuenta.length > 30) {
            nombreCuentaError.innerHTML = "Ingrese un nombre valido (3 a 30 caracteres)";
            event.preventDefault();
        }
        if (password.length < 3 || password.length > 30) {
            passwordError.innerHTML = "Ingrese una contrasela valida (3 a 30 caracteres.)";
            event.preventDefault();
        }
    }); 
}

function formreg(){
    document.getElementById("registroForm").addEventListener("submit", function (event) {
        var nombreCuenta = document.getElementById("nombreCuenta").value;
        var password = document.getElementById("password").value;
        var confirmPassword = document.getElementById("confirmPassword").value;
        var correo = document.getElementById("correo").value;
        var direccion = document.getElementById("direccion").value;

        var nombreCuentaError = document.getElementById("nombreCuentaError");
        var correoError = document.getElementById("correoErrorr"); // Corregido el nombre del ID
        var direccionError = document.getElementById("direccionError");
        var passError = document.getElementById("passwordError");
        var passconError = document.getElementById("passwordconError");

        nombreCuentaError.innerHTML = "";
        correoError.innerHTML = "";
        direccionError.innerHTML = "";
        passError.innerHTML = "";
        passconError.innerHTML = "";

        if (nombreCuenta.length < 3 || nombreCuenta.length > 30) {
            nombreCuentaError.innerHTML = "El nombre de cuenta debe tener entre 3 y 30 caracteres.";
            event.preventDefault();
        }

        if (password.length < 3 || password.length > 30) {
            passError.innerHTML = "La contraseña debe tener entre 3 y 30 caracteres.";
            event.preventDefault();
        }

        if (password !== confirmPassword) {
            passconError.innerHTML = "Las contraseñas no coinciden.";
            event.preventDefault();
        }

        if (direccion.length < 3 || direccion.length > 60) {
            direccionError.innerHTML = "Ingrese una dirección valida";
            event.preventDefault();
        }

        if (correo.length < 3 || correo.length > 60) { // Corregido el nombre de la variable
            correoError.innerHTML = "Ingrese un correo valido";
            event.preventDefault();
        }
        var correoRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!correoRegex.test(correo)) {
            correoError.innerHTML = "Ingrese un correo electrónico válido.";
            event.preventDefault();
        }
    });
}

function formc(){
    document.getElementById("registroForm").addEventListener("submit", function (event) {
        var nombreCuenta = document.getElementById("nombreCuenta").value;
        var password = document.getElementById("password").value;
        var confirmPassword = document.getElementById("confirmPassword").value;
        var nombreCuentaError = document.getElementById("nombreCuentaError");
        var passwordError = document.getElementById("passwordError");

        nombreCuentaError.innerHTML = "";
        passwordError.innerHTML = "";

        if (nombreCuenta.length < 3 || nombreCuenta.length > 30) {
            nombreCuentaError.innerHTML = "El nombre de cuenta debe tener entre 3 y 30 caracteres.";
            event.preventDefault();
        }

        if (password.length < 3 || password.length > 30) {
            passwordError.innerHTML = "La contraseña debe tener entre 3 y 30 caracteres.";
            event.preventDefault();
        }

        if (password !== confirmPassword) {
            passwordError.innerHTML = "Las contraseñas no coinciden.";
            event.preventDefault();
        }
    });
}