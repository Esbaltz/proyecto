function confirmarCompra() {
    Swal.fire({
      title: 'Producto agregado',
      text: '¿Deseas seguir comprando o ir al carrito?',
      icon: 'success',
      showCancelButton: true,
      confirmButtonText: 'Ir al carrito',
      cancelButtonText: 'Seguir comprando',
    }).then((result) => {
      if (result.isConfirmed) {
        window.location.href = "{% url 'carrito' %}";
      }
    });
  }

  window.onload = function () {
      desc();
  };