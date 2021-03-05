$(document).ready(function() {
    var prueba = 'hola';
    // Creaoms una funcion raiz para hacer submit de forms con ajax y FormDATA


    // Funcion para eliminar por ajax
    function eliminarAjax(id, url, callback){
        $.ajax({
            type: 'POST',
            url: url,
            data: 'action=delete id='+id,
            dataType: 'json',
            processData: false,
            contentType: false,
        }).done(function (data) {
            if (!data.hasOwnProperty('error')) {
                callback();
                return false;
            }
            alertaError(data.error)
        }).fail(function (jqXHR, textStatus, errorThrown) {
            alertaError(textStatus + ': ' + errorThrown)
        }).always(function (data) {
        });
    };

});