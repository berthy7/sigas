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

$('#fkcondominio').selectpicker({
    size: 10,
    liveSearch: true,
    liveSearchPlaceholder: 'Buscar',
    title: 'Seleccione'
})

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
        'fkcondominio': $('#fkcondominio').val(),
        'fechainicio': $('#fechainicio').val(),
        'fechafin': $('#fechafin').val()
    })

    if($('#tipo_reporte').val() && $('#fkcondominio').val()){
        
        
        ruta = 'reporte_'+$('#tipo_reporte').val();
        $.ajax({
            method: "POST",
            url: ruta,
            data: {_xsrf: getCookie("_xsrf"), object: obj},
            async: true,
    
            beforeSend: function () {
               $("#rproc-loader").fadeIn(800);
               $("#new").hide();
            },
            success: function () {
               $("#rproc-loader").fadeOut(800);
               $("#new").show();
            }
    
    
        }).done(function (response) {
            response = JSON.parse(response)
            
            
            console.log("datos en interfaz")
            
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
            'Porfavor Seleccione',
            'warning'
        )


    }

})


$('#filtrar').click(function () {

    actualizar_tabla_filtrar($('#fechai').val(),$('#fechaf').val())
    
});


function actualizar_tabla_filtrar(fechainicio,fechafin) {
        obj = JSON.stringify({
        'fechainicio': fechainicio,
        'fechafin': fechafin,
        '_xsrf': getCookie("_xsrf")
    })
    ruta = "registros_filtrar";
    $.ajax({
        method: "POST",
        url: ruta,
        data: {_xsrf: getCookie("_xsrf"), object: obj},
        async: true,

        beforeSend: function () {
           $("#rproc-loader").fadeIn(800);
           $("#new").hide();
        },
        success: function () {
           $("#rproc-loader").fadeOut(800);
           $("#new").show();
        }


    }).done(function (response) {
        response = JSON.parse(response)

        var data = [];
        for (var i = 0; i < Object.keys(response.response).length; i++) {

            // console.log(response['response'][i]["autorizacion"])

            data.push( [
                response['response'][i]["id"],
                response['response'][i]["tarjeta"],
                response['response'][i]["codigo"],
                response['response'][i]["autorizacion"],
                response['response'][i]["destino"],
                response['response'][i]["dia"],
                response['response'][i]["mes"],
                response['response'][i]["año"],
                response['response'][i]["hora"],
                response['response'][i]['dispositivo'],
                response['response'][i]["cerradura"],
            ]);
        }

        cargar_tabla(data)
    })
}



// $('#reporte-xls').click(function () {
//
//     obj = JSON.stringify({
//         'tipo_reporte': $('#tipo_reporte').val(),
//         'fkcondominio': $('#fkcondominio').val(),
//         'fechainicio': $('#fechainicio').val(),
//         'fechafin': $('#fechafin').val()
//     })
//
//     if($('#tipo_reporte').val() && $('#fkcondominio').val()){
//
//         ruta = "/reporte_general";
//         $.ajax({
//             method: "POST",
//             url: ruta,
//             data:{_xsrf: getCookie("_xsrf"), object: obj},
//             async: false
//         }).done(function(response){
//             response = JSON.parse(response)
//
//             if (response.success) {
//                 $('#link_excel').attr('href', response.response.url).html(response.response.nombre)
//             }
//         })
//         $('#modal-rep-xls').modal('show')
//
//     }else{
//         swal(
//             'Faltan Datos',
//             'Porfavor Seleccione',
//             'warning'
//         )
//
//
//     }
//
// })


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