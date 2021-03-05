$(function() {
    console.log(urlLazy)
    $('#clienteForm').on('submit', function (e){
        e.preventDefault();
        var parameters = new FormData(this);
        parameters.append('action', $('input[name="action"]').val());
        console.log(parameters)
        submitAjaxFormData(window.location.pathname, parameters, function () {
            location.href = urlLazy}, 'Esta seguro de crerar este nuevo cliente', 'Crear nuevo Cliente');
    });
});