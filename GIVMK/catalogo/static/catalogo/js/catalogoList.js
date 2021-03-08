$(function (){
   // Programamos el listado de clientes por ajax
    var tblProductos = $('#listadoProd').DataTable({
        responsive: true,
        scrollX: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        language: {
            "lengthMenu": "Mostrar _MENU_ registros por página",
            "zeroRecords": "No se encontraron Registros - Lo sentimos..!",
            "info": "Mostrando página _PAGE_ de _PAGES_",
            "infoEmpty": "No hay registros Disponibles",
            "search": "Buscar:",
            "infoFiltered": "(filtered from _MAX_ total records)",
            "loadingRecords": "Cargando...",
            "processing": "Procesando...",
            "thousands": ",",
            "decimal": "",
            "paginate": {
                "first": "Primero",
                "last": "Ultimo",
                "next": "Siguiente",
                "previous": "Anterior"
            }
        },
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },
        columns: [
            {'data': 'img'},
            {'data': 'nombre'},
            {'data': 'precio_consultora'},
            {'data': 'precio_catalogo'},
            {'data': 'existencia'},
            {'data': 'id'},
        ],
        columnDefs: [
            {
                targets: [5],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var btn = '<button rel="edit" class="btn btn-warning btn-circle mr-2" title="Editar Cliente">';
                    btn += '<i class="fas fa-user-edit"></i></button>';
                    btn += '<button rel="delete" class="btn btn-danger btn-circle mr-2" title="Eliminar Cliente">';
                    btn += '<i class="fas fa-trash"></i></button>';
                    btn += '<button rel="view" class="btn btn-info btn-circle mr-1" title="Eliminar Cliente">';
                    btn += '<i class="fas fa-eye"></i></button>';
                    return btn;
                }
            },
            {
                targets: [0],
                class: 'text-center',
                render: function (data, type, row) {
                    var img = '<img src="' + data + '" class="rounded-circle" width="45" height="45">'
                    return img;
                }
            }
        ],
        initComplete: function (settings, json) {
            console.log('%cSe ha cargado correctamente la tabla', 'color: blue;');
        }
    });
});