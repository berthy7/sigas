main_route = '/reporte'

$(document).ready(function () {
   
});

$(document).ajaxStart(function () { });

$(document).ajaxStop(function () {
    $.Toast.hideToast();
});

var fechahoy = new Date()
var hoy = fechahoy.getDate()+"/"+(fechahoy.getMonth()+1) +"/"+fechahoy.getFullYear()

document.getElementById("fechainicio").value=hoy
document.getElementById("fechafin").value=hoy

$('.date').bootstrapMaterialDatePicker({
    format: 'DD/MM/YYYY',
    clearButton: false,
    weekStart: 1,
    locale: 'es',
    time: false
}).on('change', function (e, date) {
    $(this).parent().addClass('focused');
    eraseError(this)
});
$('.datepicker').bootstrapMaterialDatePicker({
    format: 'DD/MM/YYYY',
    clearButton: false,
    weekStart: 1,
    locale: 'es',
    time: false
}).on('change', function (e, date) {
    $(this).parent().addClass('focused');
    $('#f_date').bootstrapMaterialDatePicker('setMinDate', date);
});

$('#tipo_reporte').selectpicker({
    size: 10,
    liveSearch: true,
    liveSearchPlaceholder: 'Buscar',
    title: 'Seleccione'
})


$('#tipo_reporte').change(function () {
    
    if ($('#tipo_reporte').val() == "vehicular_visita"){
        $('#row_vehicular_visita').show()
        $('#row_peatonal_visita').hide()
        $('#row_vehicular_residente').hide()
        $('#row_peatonal_residente').hide()
        $('#row_singuardia_visita').hide()
        
        
    }
    else if ($('#tipo_reporte').val() == "peatonal_visita"){
        $('#row_vehicular_visita').hide()
        $('#row_peatonal_visita').show()
        $('#row_vehicular_residente').hide()
        $('#row_peatonal_residente').hide()
        $('#row_singuardia_visita').hide()
        
    }
    else if ($('#tipo_reporte').val() == "vehicular_residente"){
        $('#row_vehicular_visita').hide()
        $('#row_peatonal_visita').hide()
        $('#row_vehicular_residente').show()
        $('#row_peatonal_residente').hide()
        $('#row_singuardia_visita').hide()
        
    }
    else if ($('#tipo_reporte').val() == "peatonal_residente"){
        $('#row_vehicular_visita').hide()
        $('#row_peatonal_visita').hide()
        $('#row_vehicular_residente').hide()
        $('#row_peatonal_residente').show()
        $('#row_singuardia_visita').hide()
        
    }
    else if ($('#tipo_reporte').val() == "singuardia_visita"){
        $('#row_vehicular_visita').hide()
        $('#row_peatonal_visita').hide()
        $('#row_vehicular_residente').hide()
        $('#row_peatonal_residente').hide()
        $('#row_singuardia_visita').show()
        
        
    }
});


$('#generar').click(function () {

    obj = JSON.stringify({
        'tipo_reporte': $('#tipo_reporte').val(),
        'fechainicio': $('#fechainicio').val(),
        'fechafin': $('#fechafin').val()
    })

    if($('#tipo_reporte').val()){

        ajax_call_get('reporte_'+$('#tipo_reporte').val(), {
            _xsrf: getCookie("_xsrf"),
            object: obj
        }, function (response) {
            if ($('#tipo_reporte').val() == "vehicular_visita"){
                preparar_datos_vehicular_visita(response)

            }
            else if ($('#tipo_reporte').val() == "peatonal_visita"){
                preparar_datos_peatonal_visita(response)

            }
            else if ($('#tipo_reporte').val() == "vehicular_residente"){
                preparar_datos_vehicular_residente(response)

            }
            else if ($('#tipo_reporte').val() == "peatonal_residente"){
                preparar_datos_peatonal_residente(response)

            }
            else if ($('#tipo_reporte').val() == "singuardia_visita"){
                preparar_datos_singuardia_visita(response)

            }

        })

    }else{
        swal(
            'Faltan Datos',
            'Porfavor Seleccione tipo de reporte',
            'warning'
        )


    }

})


    function editar(elemento){
    obj = JSON.stringify({
        'id': parseInt(JSON.parse($(elemento).attr('data-json')))
    })
    ajax_call_get('reporte_update', {
        _xsrf: getCookie("_xsrf"),
        object: obj
    }, function (response) {
        var self = response;
        $('#id').val(self.id)
        $('#nombre').val(self.nombre)

        validationInputSelects("form")
        verif_inputs('')
        $('#id_div').hide()
        $('#insert').hide()
        $('#update').show()
        $('#form').modal('show')
    })
    }


$('#update').click(function () {
    notvalid = validationInputSelectsWithReturn("form");
    if (notvalid===false) {
        objeto = JSON.stringify({
            'id': parseInt($('#id').val()),
            'nombre': $('#nombre').val()
        })
        ajax_call('reporte_update', {
            object: objeto,
            _xsrf: getCookie("_xsrf")
        }, null, function () {
            setTimeout(function () {
                window.location = main_route
            }, 2000);
        })
        $('#form').modal('hide')
    } else {
        swal(
            'Error de datos.',
             notvalid,
            'error'
        )
    }
})
reload_form()

    
function eliminar(elemento){
    cb_delete = elemento
    b = $(elemento).prop('checked')
    if (!b) {
        cb_title = "¿Deshabilitar  Marca?"

    } else {
        cb_title = "¿Habilitar  Marca?"
    }
    swal({
        title: cb_title,
        type: "warning",
        showCancelButton: true,
        confirmButtonColor: "#393939",
        cancelButtonColor: "#F44336",
        confirmButtonText: "Aceptar",
        cancelButtonText: "Cancelar"
    }).then(function () {
        $(cb_delete).prop('checked', !$(cb_delete).is(':checked'))
        objeto = JSON.stringify({
            id: parseInt($(cb_delete).attr('data-id')),
            enabled: $(cb_delete).is(':checked')
        })
        ajax_call('reporte_delete', {
            object: objeto,
            _xsrf: getCookie("_xsrf")
        }, null, function () {
            setTimeout(function () {
                window.location = main_route
            }, 2000);
        })
        $('#form').modal('hide')
    })
}

validationKeyup("form")
validationSelectChange("form")