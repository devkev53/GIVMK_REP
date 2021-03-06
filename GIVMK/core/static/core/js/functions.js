function submitAjaxFormData(url, parameters, callback, content, title) {
    $.confirm({
        type: 'blue',
        icon: 'fa fa-info',
        title: title,
        content: content,
        columnClass: 'small',
        typeAnimated: true,
        draggable: true,
        dragWindowBorder: false,
        buttons: {
            Ok: {
                text: 'Si',
                btnClass: 'btn-blue',
                action: function () {
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
                        console.log(data.error)
                    }).fail(function (jqXHR, textStatus, errorThrown) {
                        console.log(textStatus + ': ' + errorThrown)
                        console.log(jqXHR)
                    }).always(function (data) {
                    })
                }
            },
            cancelar: {
                text: 'Cancelar',
                btnClass: 'btn-orange',
                action: function () {
                }
            },
        }
    });

};

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