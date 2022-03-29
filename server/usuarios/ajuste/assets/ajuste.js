main_route = '/ajuste'

$(document).ready(function () {
 cargar_reserva_minima()
});

$(function () {
    $('#sign_in').validate({
        highlight: function (input) {
            $(input).parents('.form-line').addClass('error');
        },
        unhighlight: function (input) {
            $(input).parents('.form-line').removeClass('error');
        },
        errorPlacement: function (error, element) {
            $(element).parents('.input-group').append(error);
        }
    });
});

$('#see-pass').mousedown(function(){
    $("#ic-pass").css("color", "lightgrey");
    $("#clavesecreta").prop("type", "text");
    $("#ic-pass").html("visibility");
});

$("#see-pass").mouseup(function(){
    $("#ic-pass").css("color", "grey");
    $("#clavesecreta").prop("type", "password");
    $("#ic-pass").html("visibility_off");
});

$(document).ajaxStart(function () { });

$(document).ajaxStop(function () {
    $.Toast.hideToast();
});

function cargar_reserva_minima(){

    $('#fkmonedaReserva').val($('#input_fkmonedaReserva').val())
    $('#fkmonedaReserva').selectpicker('refresh');

}

$('#EjecutarconsultaSql').click(function () {

    objeto = JSON.stringify({
        'consultaSql': $('#consultaSql').val()
    })
    ajax_call('ajuste_ejecutar_consulta', {
        object: objeto,
        _xsrf: getCookie("_xsrf")
    }, null, function () {
        setTimeout(function () {
            window.location = main_route
        }, 2000);
    })

})

$('#actualizarVersionmovil').click(function () {

    objeto = JSON.stringify({
        'version': $('#versionmovil').val(),
        'id_movil': $('#id_movil').val()
    })
    ajax_call('ajuste_update_movil', {
        object: objeto,
        _xsrf: getCookie("_xsrf")
    }, null, function () {
        setTimeout(function () {
            window.location = main_route
        }, 2000);
    })

})


$('#actualizar_onesignal').click(function () {

    objeto = JSON.stringify({
        'app_id': $('#app_id').val(),
        'rest_api_key': $('#rest_api_key').val(),
        'channel_id': $('#channel_id').val()
    })
    ajax_call('ajuste_onesignal', {
        object: objeto,
        _xsrf: getCookie("_xsrf")
    }, null, function () {
        setTimeout(function () {
            window.location = main_route
        }, 2000);
    })

})

$('#actualizarcuotasMora').click(function () {

    objeto = JSON.stringify({
        'cuotasMora': $('#cuotasMora').val()
    })
    ajax_call('ajuste_update', {
        object: objeto,
        _xsrf: getCookie("_xsrf")
    }, null, function () {
        setTimeout(function () {
            window.location = main_route
        }, 2000);
    })

})

$('#residentecondominio').click(function () {

    objeto = JSON.stringify({
    })
    ajax_call('ajuste_residente_movimiento', {
        object: objeto,
        _xsrf: getCookie("_xsrf")
    }, null, function () {
        setTimeout(function () {
            window.location = main_route
        }, 2000);
    })

})


reload_form()




validationKeyup("form")
validationSelectChange("form")

