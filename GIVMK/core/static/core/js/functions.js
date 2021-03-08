// Funcion para mostrar mensajes de error
function message_error(obj) {
    var html = '';
    if (typeof (obj) === 'object') {
        html = '<ul style="text-align: left;">';
        $.each(obj, function (key, value) {
            html += '<li>' + key + ': ' + value + '</li>';
        });
        html += '</ul>';
    } else {
        html = '<p>' + obj + '</p>';
    }
    $.alert({
        title: 'Alerta..!',
        content: html,
        type: 'red',
        icon: 'fas fa-exclamation-triangle',
    });
}

// Funcion para hacer submit con Ajax e imagenes
function submitAjaxFormData(url, parameters, callback, content, title, icon, color) {
    $.confirm({
        type: color,
        icon: icon,
        title: title,
        content: content,
        columnClass: 'small',
        typeAnimated: true,
        draggable: true,
        dragWindowBorder: false,
        buttons: {
            Ok: {
                text: 'Si',
                btnClass: 'btn-success',
                action: function () {
                    console.log( parameters.get('img') );
                    $.ajax({
                        type: 'POST',
                        url: url,
                        data: parameters,
                        dataType: 'json',
                        processData: false,
                        contentType: false,
                    }).done(function (data) {
                        if (!data.hasOwnProperty('error')) {
                            callback();
                            return false;
                        }
                        message_error(data.error)
                    }).fail(function (jqXHR, textStatus, errorThrown) {
                        message_error(textStatus + ': ' + errorThrown)
                    }).always(function (data) {
                    })
                }
            },
            cancelar: {
                text: 'Cancelar',
                btnClass: 'btn-secondary',
                action: function () {
                }
            },
        }
    });

};

// Funcion para eliminar con Ajax
function eliminarAjaxList(url, parameters, callback, content, title) {
    $.confirm({
        type: 'red',
        icon: 'fas fa-exclamation-triangle',
        title: title,
        content: content,
        columnClass: 'small',
        typeAnimated: true,
        draggable: true,
        dragWindowBorder: false,
        buttons: {
            Ok: {
                text: 'Si',
                btnClass: 'btn-red',
                action: function () {
                    for (var pair of parameters.entries()) {
                        console.log(pair[0] + ', ' + pair[1]);
                    }
                    $.ajax({
                        type: 'POST',
                        url: url,
                        data: parameters,
                        processData: false,
                        contentType: false,
                    }).done(function (data) {
                        if (!data.hasOwnProperty('error')) {
                            callback();
                            return false;
                        }
                        console.log(data.error)
                    }).fail(function (jqXHR, textStatus, errorThrown) {
                        console.log('entro aqui XD')
                    }).always(function (data) {
                    })
                }
            },
            cancelar: {
                text: 'Cancelar',
                btnClass: 'btn-secondary',
                action: function () {
                }
            },
        }
    });

};

// Funcion para abrir modal
function abrir_modal(url) {
    $("#miModal").load(url, function(){
        $(this).modal({
            backdrop: 'static',
            keyboard: false
        });
        $(this).modal('show');
    });
    return false;
};

// Funcion para cerrar modal
function cerrar_modal(url)
{
    $('#popup').modal('hide');
    return false;
};