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

function eliminarAjax(url, parameters, callback, content, title) {
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
                    console.log(parameters)
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