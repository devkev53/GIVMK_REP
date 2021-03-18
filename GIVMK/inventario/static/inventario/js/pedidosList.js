$(function () {
    // Programamos el listado de clientes por ajax
    var tblPedidos = $('#listadoPedidos').DataTable({
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
            {'data': 'fecha'},
            {'data': 'referencia'},
            {'data': 'cantidadProd'},
            {'data': 'totalConsultora'},
            {'data': 'totalCatalogo'},
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
                    return btn
                }
            },
            {
                targets: [2],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    return "<td align='center'>"+data+"</td>";
                }
            },
            {
                targets: [3, 4],
                class: 'text-center',
                render: function (data, type, row) {
                    return 'Q. ' + parseFloat(data).toFixed(2);
                }
            }
        ],
        initComplete: function (settings, json) {
            console.log('%cSe ha cargado correctamente la tabla', 'color: blue;');
        }
    });

    // Obtenemos el evento del boton eliminar
    $('#listadoPedidos tbody')
        .on('click', 'button[rel="delete"]', function () {
            // tomamos la linea de la tabla
            var tr = tblPedidos.cell($(this).closest('td, li')).index();
            // tomamos el dato
            var data = tblPedidos.row(tr.row).data();
            // mandamos a pedir la url dinamica
            var url = obtenerUrl(data.id, 'eliminar');
            var parameters = new FormData();
            parameters.append('id', data.id);
            var content = 'Se eliminara el pedido con fecha: ' + data.fecha;
            console.log(url);
            eliminarAjaxList(url, parameters, function () {
                tblPedidos.ajax.reload();
            }, content, 'Eliminar')
        });

    // Obtenemos el evento del boton editar
    $('#listadoPedidos tbody')
        .on('click', 'button[rel="edit"]', function () {
            // tomamos la linea de la tabla
            var tr = tblPedidos.cell($(this).closest('td, li')).index();
            // tomamos el dato
            var data = tblPedidos.row(tr.row).data();
            // mandamos a pedir la url dinamica
            var url = obtenerUrlEdit(data.id);
            // llamamos a el tempalte con el cliente
            location.href = url;
        });

    // Obtenemos el evento del boton vista
    $('#listadoPedidos tbody')
        .on('click', 'button[rel="view"]', function () {

            // tomamos la linea de la tabla
            var tr = tblPedidos.cell($(this).closest('td, li')).index();
            // tomamos el dato
            var data = tblPedidos.row(tr.row).data();
            // Escribimos la fecha del pedido
            $('#fecha').html(data.fecha)

            $('#tblDetalle').DataTable({
                responsive: true,
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
                        'action': 'search_details_prod',
                        'id': data.id
                    },
                    dataSrc: ""
                },
                columns: [
                    {'data': 'producto.nombre'},
                    {'data': 'pConsultora'},
                    {'data': 'pCatalogo'},
                    {'data': 'cantidad'},
                    {'data': 'subConsultora'},
                ],
                columnDefs: [
                    {
                        targets: [1, 2, 4],
                        class: 'text-center',
                        orderable: false,
                        render: function (data, type, row) {
                            return 'Q. ' + parseFloat(data).toFixed(2);
                        }
                    },
                    {
                        targets: [3],
                        class: 'text-center',
                        orderable: false,
                        render: function (data, type, row) {
                            return "<td align='center'>"+data+"</td>";
                        }
                    }
                ],
                initComplete: function (settings, json) {
                    console.log('%cSe ha cargado correctamente la tabla', 'color: blue;');
                }
            });

            abrirModal();

            // Estas variables hacen que el search y el list de datatable se acomode al final
            $('#tblDetalle_filter').addClass("d-flex justify-content-end mr-2");
            $('.dataTables_paginate').addClass("d-flex justify-content-end mr-2");
        });

    // Estas variables hacen que el search y el list de datatable se acomode al final
    $('.dataTables_filter').addClass("d-flex justify-content-end mr-2");
    $('.dataTables_paginate').addClass("d-flex justify-content-end mr-2");
});