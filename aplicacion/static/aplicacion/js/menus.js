// Get the Sidebar
var mySidebar = document.getElementById("mySidebar");

// Get the DIV with overlay effect
var overlayBg = document.getElementById("myOverlay");

// Toggle between showing and hiding the sidebar, and add overlay effect
function w3_open() {
  if (mySidebar.style.display === "block") {
    mySidebar.style.display = "none";
    overlayBg.style.display = "none";
  } else {
    mySidebar.style.display = "block";
    overlayBg.style.display = "block";
  }
}

// Close the sidebar with the close button
function w3_close() {
  mySidebar.style.display = "none";
  overlayBg.style.display = "none";
}

function desc(){
  $(document).ready(function () {
    // Realizar solicitud a la API de Google Books para obtener la descripción del libro "Holly" de Stephen King en español
    $.getJSON('https://www.googleapis.com/books/v1/volumes?q=intitle:holly+inauthor:stephen+king&langRestrict=es', function (data) {
      // Esta función se ejecuta cuando la solicitud a la API es exitosa
      console.log('Datos recibidos:', data);
      // Verificar si se encontraron resultados
      if (data.totalItems > 0) {
        // Obtener la descripción del primer libro de los resultados
        var description = data.items[0].volumeInfo.description;
        // Limitar la longitud de la descripción a 500 caracteres
        var briefDescription = description.substring(0, 500);
        // Mostrar la descripción en el elemento HTML correspondiente
        $('#book-description').text(briefDescription + '...');
      } else {
        // Si no se encontraron resultados, mostrar un mensaje de error
        $('#book-description').text('No se encontró la descripción breve del libro "Holly" de Stephen King en español.');
      }
    }).fail(function () {
      // Esta función se ejecuta si hay un error al realizar la solicitud a la API
      console.log('Error al consumir la API de Google Books!');
      // Mostrar un mensaje de error
      $('#book-description').text('Error al obtener la descripción breve del libro.');
    });
  });
}