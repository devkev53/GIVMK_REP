$(function() {
    // Campturamos el input de la imagen
    var input_imagen = document.getElementById('id_img');

    input_imagen.addEventListener('change', function(e){
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
            image.setAttribute("width", "75");
            image.setAttribute("height", "75");
            image.setAttribute("overflow", "hidden");
            image.classList.add('img-responsive')
            image.classList.add('rounded-circle')

            preview.innerHTML = '';
            preview.append(image);
        }

        console.log($('#id_img').val());
	});

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
    // Pasamos el la fecha por datepicker
    $( '#id_nacimiento').datepicker({
        dateFormat: "yy-mm-dd",
        changeYear: true,
        changeMonth: true,
    });
    // Aplicamos las mascaras a los formatos
    $('#id_tel').mask('0000-0000');
    $('#id_idNumber').mask('0000 00000 0000');
    $('#id_NIT').mask('0000 00000 0000');

    $('#miForm').on('submit', function (e){
        e.preventDefault();
        var parameters = new FormData(this);
        parameters.append('action', $('input[name="action"]').val());
        console.log(parameters)
        submitAjaxFormData(window.location.pathname, parameters, function () {
            location.href = urlLazy}, content, title, icon, color);
    });
});