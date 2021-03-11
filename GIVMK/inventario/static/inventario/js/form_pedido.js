$(function (){
    $('#id_precio_consultora').mask("###0.00", {reverse: true});
    $('#id_precio_catalogo').mask("###0.00", {reverse: true});

    // Funcion para validar que las cantidades sean distintas a cero
    function cantidades(){
        var consultora = $('#id_precio_consultora').val();
        var catalogo = $('#id_precio_catalogo').val();
        if (consultora <= 0 || catalogo <= 0){
            menssage_info('Error',
                'Verifique las cantidades no puedes ser menor o igual a: 0');
            return false;
        }
    };

    var disparado = false;
    // Funcion para validar el cambio

    function changeImg(){
        input_imagen.addEventListener('change', function(e) {
            validarTipoArchivo2(input_imagen);
            // Creamos el objeto de la clase FileReader
            let reader = new FileReader();

            // Leemos el archivo subido y se lo pasamos a nuestro fileReader
            reader.readAsDataURL(e.target.files[0]);

            // Le decimos que cuando este listo ejecute el código interno
            reader.onload = function () {
                let preview = document.getElementById('preview');
                image = document.createElement('img');

                image.src = reader.result;
                image.setAttribute("id", "view_img;");
                image.setAttribute("width", "150");
                image.setAttribute("height", "150");
                image.setAttribute("overflow", "hidden");
                image.classList.add('img-responsive')
                image.classList.add('rounded-circle')

                preview.innerHTML = '';
                preview.append(image);
            }
            return 1;
        });
    }
    // Limpiar el formulario al ocultar el modal
    $('#miModal').on('hidden.bs.modal', function (e){
        $('#miFormProducto').trigger('reset');
        // Limpiamos el preview colocando la imagen de principio;
        input_imagen.addEventListener('change',(event) => {disparado = true});
        if (disparado==true){
            image.src = img_original;
        };
    });

    // Cerrar el modal con el boton cancelar
    $('#btnCerrarMiModal').on('click', function (){
        cerrarMiModal();
    })

    // Funcion para cerrar miModal
    function cerrarMiModal(){
        $('#miModal').modal('hide');
    }

    // Campturamos el input de la imagen
    var input_imagen = document.getElementById('id_img');

    // Capturamos la ruta de la imagen que muestra inicialmente
    var img_original = $('#view_img').attr('src');

    // Con esta funcion validaremos que el tipo de archivo a subir sea jpg, jpeg, png de lo contrario lanzara un mensaje de erro
	function validarTipoArchivo2(dato){
		var fileInput = dato;
	    var filePath = fileInput.value;
	    var allowedExtensions = /(.jpg|.jpeg|.png)$/i;
	    if(!allowedExtensions.exec(filePath)){
	    	$.alert({
					icon: 'icon-error',
				    title: 'Error..!',
				    type: 'red',
    				typeAnimated: true,
				    content: 'Solamente se admiten archivos con extensiones .jpeg/.jpg/.png',
				});
	        fileInput.value = '';
	        text_edit.innerHTML = 'Seleccione Imagen..!';
	        return false;
	    }
	}

    // Funcion para llamar al modal y poder crear el producto
    function abrirModalProd(){
	    // Seteamos que no se pueda cerrar solo con los botones
        $("#miModal").modal({
            backdrop: 'static',
            keyboard: false
        });
        // Abrimos el Modal
        $("#miModal").modal('show');
        // Agreamos el evento de cambio
        changeImg();
    };

    // Enviando el formulario del Pedido por ajax
    $('#miForm').on('submit', function (e) {
        e.preventDefault();
        if (pedido.items.productos.length <= 0){
            menssage_info('Alerta..!', 'Debe tener al menos un item en su detalle');
            return false;
        };
        pedido.items.fecha = $('input[name="fecha"]').val();
        pedido.items.referencia = $('input[name="referencia"]').val();
        var parameters = new FormData();
        parameters.append('action', $('input[name="action"]').val());
        parameters.append('ingr', JSON.stringify(pedido.items));
        submitAjaxFormData(window.location.pathname, parameters, function () {
		location.href = urlLazy}, content, title, icon, color )
    });

    // Enviando el formulario del Producto por ajax
    $('#miFormProducto').on('submit', function (e) {
        e.preventDefault();
        if (cantidades() == false){
            return false;
        }
        // Tomamos los datos del Formulario
        var parameters = new FormData(this);
        parameters.append('ingr', JSON.stringify(pedido.items));
        submitAjaxFormData(window.location.pathname, parameters, function (response) {
            cerrarMiModal(); var prod = response; prod.cantidad = 1; prod.sub = 0.00; pedido.add(prod);}, 'Esta seguro de crear este Producto..?',
            'Crear Producto', icon, color )
    });

    // Guardamos la tabla de la lista de productos en la siguiente variable
    var tblProducts;

    // Creamos el diccionario con la lista de productos y las funciones
    var pedido = {
        items: {
            fecha: '',
            referencia: '',
            totalConsultora: 0.0,
            totalCatalogo: 0.0,
            productos: []
        },
        calculate: function () {
            var subtotal1 = 0.00;
            var subtotal2 = 0.00;
            var sub2 = 0.00;
            $.each(this.items.productos, function (pos, dic) {
                dic.sub = dic.cantidad * parseFloat(dic.precio_consultora);
                sub2 = dic.cantidad * parseFloat(dic.precio_catalogo);
                subtotal1 += dic.sub;
                subtotal2 += sub2;
            });
            this.items.totalConsultora = subtotal1;
            this.items.totalCatalogo = subtotal2;
            $('#id_totalConsultora').val(this.items.totalConsultora.toFixed(2));
            $('#id_totalCatalogo').val(this.items.totalCatalogo.toFixed(2));
        },
        add: function (item) {
            // Validamos que sea el primer item en el listado
            if (this.items.productos.length == 0) {
                this.items.productos.push(item);
            } else {
                // De loc ontrario creamos un listado con los id de los items
                listado = [];
                $.each(this.items.productos, function (index, value) {
                    // Recorremos y guardamos en la lista temporal
                    listado.push(value.id);
                });
                // Preguntamos si existe el id en la lista temporal
                if (listado.includes(item.id)) {
                    alertMsg('Opps..!', 'El Producto ya esta en la lista..!');
                } else {
                    // Si no existe lo agregamos
                    this.items.productos.push(item);
                }
            }
            console.log(item);
            ;
            this.list();
        },
        list: function () {
            this.calculate();
            tblProducts = $('#products_table').DataTable({
                responsive: true,
                autoWidth: false,
                destroy: true,
                deferRender: true,
                rowCallback: function (row, data) {
                    $(row).find('input[name="cantidad"]').TouchSpin({
                        min: 1,
                        max: 1000000,
                        step: 1,
                        boostat: 4,
                        buttondown_class: 'btn btn-secondary',
                        buttonup_class: 'btn btn-secondary',
                    });
                },
                language: {
                    "lengthMenu": "Mostrar _MENU_ registros por página",
                    "zeroRecords": "No se encontraron Registros - Lo sentimos..!",
                    "info": "Mostrando página _PAGE_ de _PAGES_",
                    "infoEmpty": "",
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
                data: this.items.productos,
                columns: [
                    {'data': 'id'},
                    {'data': 'nombre'},
                    {'data': 'precio_consultora'},
                    {'data': 'precio_catalogo'},
                    {'data': 'cantidad'},
                    {'data': 'sub'},
                ],
                columnDefs: [
                    {
                        targets: [0],
                        class: 'text-center',
                        orderable: false,
                        render: function (data, type, row) {
                            return '<button rel="remove" class="rounded btn-danger align-items-center" title="Eliminar"' +
                                'style="vertical-align: middle;"><i class="fas fa-minus-circle"></i></button>';
                        }
                    },
                    {
                        targets: [2, 3, 5],
                        class: 'text-center',
                        orderable: false,
                        render: function (data, type, row) {
                            return 'Q. ' + parseFloat(data).toFixed(2);
                        }
                    },
                    {
                        targets: [4],
                        class: 'text-center',
                        orderable: false,
                        render: function (data, type, row) {
                            return '<input type="text" name="cantidad" class="form-control form-control-sm input-sm"  value="' + row.cantidad + '" autocomplete="off">';
                        }
                    },
                ],
                initComplete: function (settings, json) {
                }
            });
        }
    };

    // Auto Completado con Select2
    $('input[name="search"]').select2({
        language: "es",
        theme: 'bootstrap4',
        //allowClear: true,
        ajax: {
            delay: 250,
            type: 'POST',
            url: window.location.pathname,
            data: function (params) {
                var queryParameters = {
                    term: params.term,
                    action: 'autocomplete',
                }

                return queryParameters;
            },
            processResults: function (data) {
                return {
                    results: data
                };
            },
        },
        placeholder: 'Ingrese una descripcion de producto',
        minimumInputLength: 2,
        templateResult: formatRepo,
    }).on('select2:select', function (e) {
        var prod = e.params.data;
        prod.cantidad = 1;
        prod.sub = 0.00;
        pedido.add(prod);
    });

    // Funcion para enviar el template en el Select2
    function formatRepo(repo) {
        if (repo.loading) {
            return repo.text;
        }

        var contenedor = $(
            '<div class="wrapper container">' +
            '<div class="row">' +
            '<div class="col-lg-2">' +
            '<img src="' + repo.img + '" class="img-fluid img-thumbnail d-block mx-auto rounded">' +
            '</div>' +
            '<div class="col-lg-10 text-left shadow-sm d-flex align-items-center">' +
            '<p style="margin-bottom: 0;">' +
            '<b>Nombre:</b>' + repo.nombre + '<br>' +
            '<b>P/Consultora:</b> <span class="badge badge-dark">' + repo.precio_consultora + '</span><br>' +
            '<b>P/Catalogo:</b> <span class="badge badge-warning">' + repo.precio_catalogo + '</span>' +
            '</p>' +
            '</div>' +
            '</div>' +
            '</div>'
        );
        return contenedor;
    }

    // Limpiar dealle
    $('.btnRemoveAll').on('click', function () {
        if (pedido.items.productos.length == 0) return false;
        menssage_alert('orange', 'fa-trash',
            'Borar Detalle', 'Esta seguro de eliminar el detalle..?'
            , function () {
            pedido.items.productos = [];
            pedido.list();})
    });

    // Evento cambio de cantidad
$('#products_table tbody')
	.on('click', 'button[rel="remove"]', function () {
		// Obtenemos la posision del elemento
		var tr = tblProducts.cell($(this).closest('td, li')).index();
		pedido.items.productos.splice(tr.row, 1);
		pedido.list();
	})
	.on('change', 'input[name="cantidad"]', function () {
		var cant = parseInt($(this).val());
		var tr = tblProducts.cell($(this).closest('td, li')).index();
		//var data = tblProducts.row(tr.row).node();
		pedido.items.productos[tr.row].cantidad = cant;
		pedido.calculate();
		$('td:eq(5)', tblProducts.row(tr.row).node()).html('Q. ' + pedido.items.productos[tr.row].sub.toFixed(2));
	});

    pedido.list();

    //Llamamos un modal para agregar un nuevo producto
    $('#add_new_prod_in_pedido').on('click', function (){
        abrirModalProd();
    });
});