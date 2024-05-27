function form1() {
  document
    .querySelector(".agregar_pro_form")
    .addEventListener("submit", function (event) {
      var nombre_libr = document.getElementById("nombre_libr").value;
      var isbn = document.getElementById("isbn").value;
      var confirm_isbn = document.getElementById("confirm_isbn").value;
      var valor_libr = document.getElementById("valor_libr").value;
      var imagen = document.querySelector('input[type="file"]').files[0];

      var nombre_libro_ingre_error = document.getElementById(
        "nombre_libro_ingre_error"
      );
      var nombre_isbn_error_1 = document.getElementById("nombre_isbn_error_1");
      var nombre_isbn_error = document.getElementById("nombre_isbn_error");
      var valor_libro_error = document.getElementById("valor_libro_error");
      var imagen_error = document.getElementById("imagen_error");

      nombre_libro_ingre_error.innerHTML = "";
      nombre_isbn_error_1.innerHTML = "";
      nombre_isbn_error.innerHTML = "";
      valor_libro_error.innerHTML = "";
      imagen_error.innerHTML = "";

      if (nombre_libr.length < 3 || nombre_libr.length > 60) {
        nombre_libro_ingre_error.innerHTML =
          "El nombre del libro ingresado tiene que tener un paramentro minimo de 3 caracteres o un maximo de 60.";
        event.preventDefault();
      }
      if (isbn.length !== 13) {
        nombre_isbn_error_1.innerHTML =
          "Los datos de ISBN no tiene el largo de 13 caracteres.";
        event.preventDefault();
      }

      if (isbn !== confirm_isbn) {
        nombre_isbn_error.innerHTML = "Los datos de ISBN no son iguales.";
        event.preventDefault();
      }
      if (
        valor_libr.toString().length < 2 ||
        valor_libr.toString().length > 7
      ) {
        valor_libro_error.innerHTML =
          "El valor del libro ingresado tiene que tener un paramentro minimo de 3 cifras, un maximo de 7 o no puede ingresar el valor 0 en solo.";
        event.preventDefault();
      }
      if (valor_libr < 1) {
        valor_libro_error.innerHTML = "xd";
        event.preventDefault();
      }

      if (!imagen) {
        imagen_error.innerHTML = "Por favor, seleccione una imagen.";
        event.preventDefault();
      } else {
        var extension = imagen.name.split(".").pop().toLowerCase();
        if (extension !== "jpg") {
          imagen_error.innerHTML = "Por favor, seleccione un archivo JPG.";
          event.preventDefault();
        }
      }
    });
}

function form_buscar() {
  document
    .querySelector(".buscar_pro_form")
    .addEventListener("submit", function (event) {
      var nombre_libr = document.getElementById("nombre_libr1").value;
      var isbn = document.getElementById("buscar_isbn1").value;
      var descrip = document.getElementById("detall_libr1").value;

      var nombre_libro_ingre_error = document.getElementById(
        "nombre_libro_ingre_error1"
      );
      var nombre_isbn_error = document.getElementById("nombre_isbn_error1");
      var descrip_error_libr = document.getElementById("descrip_error_libr1");

      nombre_libro_ingre_error.innerHTML = "";
      nombre_isbn_error.innerHTML = "";
      descrip_error_libr.innerHTML = "";

      if (nombre_libr.length < 3 || nombre_libr.length > 60) {
        nombre_libro_ingre_error.innerHTML =
          "El nombre del libro ingresado debe tener entre 3 y 60 caracteres.";
        event.preventDefault();
      }

      if (isbn.length !== 13) {
        nombre_isbn_error.innerHTML = "El ISBN debe tener 13 caracteres.";
        event.preventDefault();
      }

      if (descrip.length < 10 || descrip.length > 600) {
        descrip_error_libr.innerHTML =
          "Los detalles del libro deben tener entre 10 y 600 caracteres.";
        event.preventDefault();
      }
    });
}

function crear_c() {
  document
    .getElementById("crear_cuenta_Form")
    .addEventListener("submit", function (event) {
      var nombreCuenta = document.getElementById("nombreCuenta").value;
      var password_1 = document.getElementById("password_1").value;
      var confirmPassword = document.getElementById("confirmPassword").value;

      var nombreCuentaError = document.getElementById(
        "nombre_libro_ingre_error"
      );
      var passwordError = document.getElementById("passwordError");
      var passwordError_confirm = document.getElementById(
        "passwordError_confirm"
      );

      nombreCuentaError.innerHTML = "";
      passwordError.innerHTML = "";
      passwordError_confirm.innerHTML = "";

      if (nombreCuenta.length < 3 || nombreCuenta.length > 30) {
        nombreCuentaError.innerHTML =
          "El nombre de cuenta debe tener entre 3 y 30 caracteres.";
        event.preventDefault();
      }

      if (password_1.length < 3 || password_1.length > 30) {
        passwordError.innerHTML =
          "La contraseña debe tener entre 3 y 30 caracteres.";
        event.preventDefault();
      }

      if (password_1 !== confirmPassword) {
        passwordError_confirm.innerHTML = "Las contraseñas no coinciden.";
        event.preventDefault();
      }
    });
}

function elim() {
  document
    .getElementById("agregar_pro_form")
    .addEventListener("submit", function (event) {
      var isbn = document.getElementById("isbn").value;

      var nombre_isbn_error_1 = document.getElementById("nombre_isbn_error_1");

      nombre_isbn_error_1.innerHTML = "";

      if (isbn.length !== 13) {
        nombre_isbn_error_1.innerHTML =
          "Los datos de ISBN no tiene el largo de 13 caracteres.";
        event.preventDefault();
      }
    });
}

function mod() {
  document
    .getElementById("agregar_pro_form")
    .addEventListener("submit", function (event) {
      var nombre_libr = document.getElementById("nombre_libr").value;
      var isbn = document.getElementById("isbn").value;
      var valor_libr = document.getElementById("valor_libr").value;

      var nombre_libro_ingre_error = document.getElementById(
        "nombre_libro_ingre_error"
      );
      var nombre_isbn_error_1 = document.getElementById("nombre_isbn_error_1");
      var valor_libro_error = document.getElementById("valor_libro_error");

      nombre_libro_ingre_error.innerHTML = "";
      nombre_isbn_error_1.innerHTML = "";
      valor_libro_error.innerHTML = "";

      if (nombre_libr.length < 3 || nombre_libr.length > 60) {
        nombre_libro_ingre_error.innerHTML =
          "El nombre del libro ingresado tiene que tener un paramentro minimo de 3 caracteres o un maximo de 60.";
        event.preventDefault();
      }
      if (isbn.length !== 13) {
        nombre_isbn_error_1.innerHTML =
          "Los datos de ISBN no tiene el largo de 13 caracteres.";
        event.preventDefault();
      }

      if (valor_libr.length < 2 || valor_libr.length > 7) {
        valor_libro_error.innerHTML =
          "El valor del libro ingresado tiene que tener un paramentro minimo de 3 cifras, un maximo de 7 o no puede ingresar el valor 0 en solo.";
        event.preventDefault();
      }
    });
}
