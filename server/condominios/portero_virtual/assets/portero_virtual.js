main_route = '/portero_virtual'
var refrescar = false;
var sw_visita = false;

$(document).ready(function () {

    auxiliar_method()
    verificar_qr()
    verificar_qr_residente()

});

function auxiliar_method() {
    //main_method()
    //setTimeout(auxiliar_method, 10000)
    setInterval(function(){
        if($("#form").is(":visible")){
            console.log("actualizar desactivado")
        }else{
            console.log(refrescar)
            if(refrescar == false){
                window.location = main_route
            }
        }
    }, 5000);
}

function verificar_qr() {
    //main_method()
    //setTimeout(auxiliar_method, 10000)
    setInterval(function(){
        if($('#codigoautorizacion').val() != ""){
            obj = JSON.stringify({
                'codigoautorizacion': $('#codigoautorizacion').val()
            })
            ruta = "evento_validar_invitacion";

            $.ajax({
                method: "POST",
                url: ruta,
                data: {_xsrf: getCookie("_xsrf"), object: obj},
                async: false
            }).done(function (response) {
                response = JSON.parse(response)

                if (response.success) {
                    $('#fkinvitacion').val(response.response.id)
                    $('#fkinvitado').selectpicker('refresh')
                    $('#fkinvitado').val(response.response.fkinvitado)
                    $('#fkinvitado').selectpicker('refresh')
                    cargar_invitado(response.response.fkinvitado)

                    $('#fkdomicilio').val(response.response.evento.fkdomicilio)
                    $('#fkdomicilio').selectpicker('refresh')

                    $('#fkareasocial').val(response.response.evento.fkareasocial)
                    $('#fkareasocial').selectpicker('refresh')

                    $('#fktipopase').val(response.response.fktipopase)
                    $('#fktipopase').selectpicker('refresh')

                    $('#fkautorizacion').val(1)
                    $('#fkautorizacion').selectpicker('refresh')
                    cargar_nropase($( "#fktipopase option:selected" ).text())


                    document.getElementById("imagen_mensaje").src = response.message;
                    $('#codigoautorizacion').val('')

                } else {
                    document.getElementById("imagen_mensaje").src = response.message;

                    limpiar_formulario()

                }

            })
            validationInputSelects("form")
            $('#form').animate({scrollTop: 0}, 'slow');
        }

    }, 1000);
}

function verificar_qr_residente() {
    //main_method()
    //setTimeout(auxiliar_method, 10000)
    setInterval(function(){
        if($('#codigoautorizacion_residente').val() != ""){
            obj = JSON.stringify({
                'codigoautorizacion': $('#codigoautorizacion_residente').val()
            })
            ruta = "residente_validar_codigo";

            $.ajax({
                method: "POST",
                url: ruta,
                data: {_xsrf: getCookie("_xsrf"), object: obj},
                async: false
            }).done(function (response) {
                response = JSON.parse(response)
                console.log(response);

                if (response.success) {
                    $('#show_img').attr('src', response.response.fotoresidente);
                    $('#show_img').parent().parent().show();
                    // $('#fkinvitacion').val(response.response.id)
                    // $('#fkinvitado').selectpicker('refresh')
                    // $('#fkinvitado').val(response.response.fkinvitado)
                    // $('#fkinvitado').selectpicker('refresh')
                    // cargar_invitado(response.response.fkinvitado)
                    $('#fkautorizacion').val(1)
                    $('#fkautorizacion').selectpicker('refresh')

                    $('#fkdomicilio').val(response.response.iddomicilio)
                    $('#fkdomicilio').selectpicker('refresh')

                    cargar_residente(response.response.iddomicilio)
                    //
                    $('#fkresidente').val(response.response.idresidente)
                    $('#fkresidente').selectpicker('refresh')
                    //
                    $('#fktipodocumento').val(response.response.tipodocumento)
                    $('#fktipodocumento').selectpicker('refresh')
                    //

                    //
                    // cargar_nropase($( "#fktipopase option:selected" ).text())


                    document.getElementById("imagen_mensaje").src = response.message;
                    $('#codigoautorizacion_residente').val('')

                } else {
                    document.getElementById("imagen_mensaje").src = response.message;

                    limpiar_formulario()

                }

            })
            validationInputSelects("form")
            $('#form').animate({scrollTop: 0}, 'slow');
        }

    }, 1000);
}

$(document).ajaxStart(function () { });

$(document).ajaxStop(function () {
    $.Toast.hideToast();
});

var fechahoy = new Date();
var hoy = fechahoy.getDate()+"/"+(fechahoy.getMonth()+1) +"/"+fechahoy.getFullYear()

document.getElementById("fechai").value=hoy
document.getElementById("fechaf").value=hoy

$('#fkinvitado').selectpicker({
    size: 10,
    liveSearch: true,
    liveSearchPlaceholder: 'Buscar Personas',
    title: 'Seleccione Personas'
})
$('#fkcerradura').selectpicker({
    size: 10,
    liveSearch: true,
    liveSearchPlaceholder: 'Buscar',
    title: 'Seleccione'
})

$('#fkresidente').selectpicker({
    size: 10,
    liveSearch: true,
    liveSearchPlaceholder: 'Buscar Residente',
    title: 'Seleccione Residente'
})

$('#fkconductor').selectpicker({
    size: 10,
    liveSearch: true,
    liveSearchPlaceholder: 'Buscar Personas',
    title: 'Seleccione Personas'
})



$('#fkdomicilio').selectpicker({
    size: 10,
    liveSearch: true,
    liveSearchPlaceholder: 'Buscar',
    title: 'Seleccione'
})



$('#fktipopase').selectpicker({
    size: 10,
    liveSearch: true,
    liveSearchPlaceholder: 'Buscar Tipo de pase',
    title: 'Seleccione Tipo de pase'
})

$('#fkautorizacion').selectpicker({
    size: 10,
    liveSearch: true,
    liveSearchPlaceholder: 'Buscar Autorizado por',
    title: 'Seleccione Autorizacion'
})



$('#expendido').selectpicker({
    size: 10,
    liveSearch: true,
    liveSearchPlaceholder: 'Buscar',
    title: 'Seleccione'
})


$('#switch').change(function() {
   var sw = $(this).prop('checked')

    if(sw){
        $('#div_conductor').show()

    }else{
        $('#div_conductor').hide()
        
        $('#nombre_conductor').val('')
        $('#apellidop_conductor').val('')
        $('#apellidom_conductor').val('')
        $('#ci_conductor').val('')
        $('#expendido_conductor').val('')
        $('#expendido_conductor').selectpicker('refresh')
    }

})

$('#switch_visita').change(function() {
   sw_visita = $(this).prop('checked')

    if(sw_visita){

        $('#div_residente').hide()
        $('#div_invitacion').show()
        $('#div_datos_visita').show()
        $('#nombre').prop("required", true);
        $('#apellidop').prop("required", true);
        $('#ci').prop("required", true);
        $('#fkresidente').removeAttr("required");
        eraseError('fkresidente')
        $('#show_img').attr('src', '');
        $('#show_img').parent().parent().show();
        
        
    }else{
        $('#div_residente').show()
        $('#div_invitacion').hide()
        $('#div_datos_visita').hide()
        $('#nombre').removeAttr("required");
        eraseError('nombre')
        $('#apellidop').removeAttr("required");
        eraseError('apellidop')
        $('#ci').removeAttr("required");
        eraseError('ci')


        $('#fkresidente').prop("required", true);


    }

})

$('#switch_refrescar').change(function() {
   var sw_refrescar = $(this).prop('checked')

    if(sw_refrescar){
       refrescar = true;

    }else{
        refrescar = false;
    }

})

function cargar_tabla(data){
    if ( $.fn.DataTable.isDataTable( '#data_table' ) ) {
        var table = $('#data_table').DataTable();
        table.destroy();
    }

    $('#data_table').DataTable({
        data:           data,
        deferRender:    true,
        scrollCollapse: true,
        scroller:       true,

        dom: "Bfrtip" ,
        buttons: [
            {  extend : 'excelHtml5',
               exportOptions : { columns : [0, 1, 2, 3, 4, 5 ,6 ,7,8,9,10,11,12,13,14,15,16]},
                sheetName: 'Reporte Registro Vehicular',
               title: 'Control y Registro Vehicular'  },
            {  extend : 'pdfHtml5',
                orientation: 'landscape',
               customize: function(doc) {
                    doc.styles.tableBodyEven.alignment = 'center';
                    doc.styles.tableBodyOdd.alignment = 'center';
               },
               exportOptions : {
                    columns : [0, 1, 2, 3, 4, 5 ,6 ,7,8,9,10,11,12,13,14,15,16]
                },
               title: 'Control y Registro Vehicular'
            }
        ],
        initComplete: function () {


        },
        "order": [[ 0, "desc" ]],
        language : {
            'url': '/resources/js/spanish.json',
        },
        "pageLength": 5,
        fixedHeader: {
            header: true,
            headerOffset: $('.navbar-header').outerHeight()
        },
        paging: true,
        select: true
    });


}

function actualizar_tabla(response){

    var data = [];
    var id;
    var fechai;
    var fechaf;
    var ci;
    var nombre;
    var conductor;
    var placa;
    var tipo;
    var marca;
    var modelo;
    var color;
    var destino;
    var nropase;
    var salida;

    for (var i = 0; i < Object.keys(response.response).length; i++) {
            id = response['response'][i].id

            if(response['response'][i].fechai){
                fechai= response['response'][i].fechai
            }else{
                fechai = '-----'
            }

            if(response['response'][i].fechaf){
                fechaf = response['response'][i].fechaf
                salida= '✓'
            }else{
                fechaf = '-----'
                salida ="<button id='exit' onClick='salida(this)' data-json="+id+" type='button' class='btn bg-indigo waves-effect waves-light salida' title='Actualizar Salida'><i class='material-icons'>exit_to_app</i></button>"

            }

            if(response['response'][i].fkinvitado != "None"){
                ci = response['response'][i].invitado.ci,
                nombre = response['response'][i].invitado.nombre +" "+response['response'][i].invitado.apellidop+" "+response['response'][i].invitado.apellidom

            }else{
                ci ='Residente'
                nombre = response['response'][i].residente.nombre +" "+response['response'][i].residente.apellidop+" "+response['response'][i].residente.apellidom
            }


            if(response['response'][i].fkconductor != "None"){
                conductor= response['response'][i].conductor.nombre +" "+response['response'][i].conductor.apellidop+" "+response['response'][i].conductor.apellidom
            }else{
                conductor ='-----'
            }

            placa= response['response'][i].vehiculo.placa
            tipo = response['response'][i].vehiculo.tipo.nombre

            if(response['response'][i].vehiculo.fkmarca != "None"){
                marca = response['response'][i].vehiculo.marca.nombre
            }else{
                marca ='-----'
            }
            if(response['response'][i].vehiculo.fkmodelo != "None"){
                modelo = response['response'][i].vehiculo.modelo.nombre
            }else{
                modelo ='-----'
            }

            color = response['response'][i].vehiculo.color.nombre


            if(response['response'][i].fkdomicilio != "None"){
                destino = response['response'][i].domicilio.ubicacion + " " + response['response'][i].domicilio.numero
            }else if(response['response'][i].fkareasocial != "None"){
                destino = response['response'][i].areasocial.nombre
            }else{
                destino = '-----'
            }

            if(response['response'][i].fknropase != "None"){
                nropase = response['response'][i].nropase.numero + " " + response['response'][i].nropase.tipo
            }else{
                nropase = '-----'
            }

            data.push( [
                id,
                fechai,
                fechaf,
                response['response'][i].tipodocumento.nombre,
                ci,
                nombre,
                conductor,
                response['response'][i].cantpasajeros,
                placa,
                tipo,
                marca,
                modelo,
                color,
                destino,
                response['response'][i].autorizacion.nombre,
                nropase,
                response['response'][i].tipopase.nombre,
                salida
            ]);
        }


    if ( $.fn.DataTable.isDataTable( '#data_table' ) ) {
        var table = $('#data_table').DataTable();
        table.destroy();
    }

    $('#data_table').DataTable({
        data:           data,
        deferRender:    true,
        scrollCollapse: true,
        scroller:       true,

        dom: "Bfrtip" ,
        buttons: [
            {  extend : 'excelHtml5',
               exportOptions : { columns : [0, 1, 2, 3, 4, 5 ,6 ,7,8,9,10,11,12,13,14,15,16]},
                sheetName: 'Reporte Control y Registro Vehicular',
               title: 'Control y Registro Vehicular'  },
            {  extend : 'pdfHtml5',
                orientation: 'landscape',
               customize: function(doc) {
                    doc.styles.tableBodyEven.alignment = 'center';
                    doc.styles.tableBodyOdd.alignment = 'center';
               },
               exportOptions : {
                    columns : [0, 1, 2, 3, 4, 5 ,6 ,7,8,9,10,11,12,13,14,15,16]
                },
               title: 'Control y Registro Vehicular'
            }
        ],
        initComplete: function () {


        },
        "order": [[ 1, "desc" ]],
        language : {
            'url': '/resources/js/spanish.json',
        },
        "pageLength": 5,
        fixedHeader: {
            header: true,
            headerOffset: $('.navbar-header').outerHeight()
        },
        paging: true,
        select: true
    });


}

$('#codigoautorizacion').change(function () {
    console.log("cambio input")


});

$('#fkinvitado').change(function () {
    if (parseInt(JSON.parse($('#fkinvitado').val())) != 0){
        cargar_invitado(parseInt(JSON.parse($('#fkinvitado').val())))
    }else{
        $('#nombre').val('')
        $('#apellidop').val('')
        $('#apellidom').val('')
        $('#ci').val('')
        $('#expendido').val('')
        $('#expendido').selectpicker('refresh')

        validationInputSelects("form")
    }
});



$('#fkdomicilio').change(function () {
    
    cargar_residente($('#fkdomicilio').val())


});

function cargar_residente(fkdomicilio) {

    obj = JSON.stringify({
        'fkdomicilio': fkdomicilio,
        '_xsrf': getCookie("_xsrf")
    })

    ruta = "domicilio_listar_residente";
    //data.append('object', obj)
    //data.append('_xsrf',getCookie("_xsrf"))

    $.ajax({
        method: "POST",
        url: ruta,
        data: {_xsrf: getCookie("_xsrf"), object: obj},
        async: false
    }).done(function (response) {
        response = JSON.parse(response)
        console.log(response)

        $('#fkresidente').html('');
        var select = document.getElementById("fkresidente")
        for (var i = 0; i < Object.keys(response.response).length; i++) {
            var option = document.createElement("OPTION");
            option.innerHTML = response['response'][i]['fullname'];
            option.value = response['response'][i]['id'];
            select.appendChild(option);
        }
        $('#fkresidente').selectpicker('refresh');

    })

}



function cargar_invitado(id) {
    obj = JSON.stringify({
        'id': id,
        '_xsrf': getCookie("_xsrf")
    })

    ruta = "invitado_obtener";

    $.ajax({
        method: "POST",
        url: ruta,
        data: {_xsrf: getCookie("_xsrf"), object: obj},
        async: false
    }).done(function (response) {
        response = JSON.parse(response)

        console.log(response)
        $('#nombre').val(response.response.nombre)
        $('#apellidop').val(response.response.apellidop)
        $('#apellidom').val(response.response.apellidom)
        $('#ci').val(response.response.ci)
        $('#expendido').val(response.response.expendido)
        $('#expendido').selectpicker('refresh')

        // if(response.response.vehiculos.length > 0){
        //     $('#fkvehiculo').val(response.response.vehiculos[0].id)
        //     $('#fkvehiculo').selectpicker('refresh')
        //     cargar_vehiculo(response.response.vehiculos[0].id)
        // }
        validationInputSelects("form")
    })

    $('#personas').val('')
    $('#personas').selectpicker('refresh')

}



function limpiar_formulario() {
    $('#fkinvitacion').val('')
    $('#fkinvitado').val('')
    $('#fkinvitado').selectpicker("refresh")

    $('#nombre').val('')
    $('#apellidop').val('')
    $('#apellidom').val('')
    $('#ci').val('')
    $('#expendido').val('')
    $('#expendido').selectpicker("refresh")
    $('#fkdomicilio').val('')
    $('#fkdomicilio').selectpicker("refresh")

    $('#fktipopase').val('')
    $('#fktipopase').selectpicker("refresh")
    $('#fkautorizacion').val('')
    $('#fkautorizacion').selectpicker("refresh")
    $('#codigoautorizacion').val('')
    $('#codigoautorizacion_residente').val('')

}

$('#new').click(function () {
    $('#fkinvitacion').val('')
    $('#fkinvitado').val('')
    $('#fkinvitado').selectpicker("refresh")

    $('#nombre').val('')
    $('#apellidop').val('')
    $('#apellidom').val('')
    $('#ci').val('')
    $('#expendido').val('')
    $('#expendido').selectpicker("refresh")

    $('#fkdomicilio').val('')
    $('#fkdomicilio').selectpicker("refresh")

    $('#fktipopase').val('')
    $('#fktipopase').selectpicker("refresh")
    $('#fkautorizacion').val('')
    $('#fkautorizacion').selectpicker("refresh")
    $('#fkresidente').val('')
    $('#fkresidente').selectpicker("refresh")
    $('#codigoautorizacion').val('')
    $('#codigoautorizacion_residente').val('')

    $('#observaciones').val('')

    $('#show_img').attr('src', '');
    $('#show_img').parent().parent().show();

    document.getElementById("imagen_mensaje").src = "";

    document.getElementById('switch_visita').checked=true
    $('#switch_visita').change()

    verif_inputs('')
    validationInputSelects("form")
    $('#id_div').hide()
    $('#insert').show()
    $('#update').hide()
    $('#form').modal('show')

})

$('#insert').click(function () {
    notvalid = validationInputSelectsWithReturn("form");
    if (notvalid===false) {
        objeto = JSON.stringify({
            'fkcerradura': $('#fkcerradura').val(),
            'fkinvitacion': $('#fkinvitacion').val(),
            'codigoautorizacion': $('#codigoautorizacion').val(),
            'fktipodocumento': $('#fktipodocumento').val(),
            'fkinvitado': $('#fkinvitado').val(),
            'nombre': $('#nombre').val(),
            'apellidop': $('#apellidop').val(),
            'apellidom': $('#apellidom').val(),
            'ci': $('#ci').val(),
            'expendido': $('#expendido').val(),
            'fktipopase': $('#fktipopase').val(),
            'fkautorizacion': $('#fkautorizacion').val(),
            'fkresidente': $('#fkresidente').val(),
            'observacion': $('#observacion').val()

        })
        ajax_call('portero_virtual_insert', {
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

function attach_edit() {
    $('.edit').click(function () {
        obj = JSON.stringify({
            'id': parseInt(JSON.parse($(this).attr('data-json')))
        })
        ajax_call_get('evento_update', {
            _xsrf: getCookie("_xsrf"),
            object: obj
        }, function (response) {
            var self = response;
            $('#id').val(self.id)
            $('#fkresidente').val(self.fkresidente)
            $('#fkresidente').selectpicker('refresh')
            $('#fktipoevento').val(self.fktipoevento)
            $('#fktipoevento').selectpicker('refresh')
            $('#descripcion').val(self.descripcion)
            $('#domicilio').val(self.lugar)
            $('#domicilio').selectpicker('refresh')
            $('#fechai').val(self.fechai)
            $('#horai').val(self.horai)
            $('#fechaf').val(self.fechaf)
            $('#horaf').val(self.horaf)


            validationInputSelects("form")
            verif_inputs('')
            $('#id_div').hide()
            $('#insert').hide()
            $('#update').show()
            $('#form').modal('show')
        })
    })

}
attach_edit()

$('#update').click(function () {
    notvalid = validationInputSelectsWithReturn("form");
    if (notvalid===false) {
        objeto = JSON.stringify({
            'id': parseInt($('#id').val()),
            'fktipodocumento': $('#fktipodocumento').val(),
            'fktipodocumento_conductor': $('#fktipodocumento_conductor').val(),
            'fkinvitado': $('#fkinvitado').val(),
            'nombrecompleto': $('#nombrecompleto').val(),
            'ci': $('#ci').val(),
            'fkvehiculo': $('#fkvehiculo').val(),
            'placa': $('#placa').val(),
            'tipo': $('#tipo').val(),
            'color': $('#color').val(),
            'fkmarca': $('#fkmarca').val(),
            'fkmodelo': $('#fkmodelo').val(),
            'fkdomicilio': $('#fkdomicilio').val(),
            'fkareasocial': $('#fkareasocial').val(),
            'fktipopase': $('#fktipopase').val(),
            'fkautorizacion': $('#fkautorizacion').val(),
            'fknropase': $('#nropase').val()
        })
        ajax_call('evento_update', {
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

$('#validar_invitacion').click(function () {

        obj = JSON.stringify({
            'codigoautorizacion': $('#codigoautorizacion').val()
        })
        ruta = "evento_validar_invitacion";

        $.ajax({
            method: "POST",
            url: ruta,
            data: {_xsrf: getCookie("_xsrf"), object: obj},
            async: false
        }).done(function (response) {
            response = JSON.parse(response)

            if (response.success) {
                $('#fkinvitacion').val(response.response.id)
                $('#fkinvitado').selectpicker('refresh')
                $('#fkinvitado').val(response.response.fkinvitado)
                $('#fkinvitado').selectpicker('refresh')
                cargar_invitado(response.response.fkinvitado)

                $('#fkdomicilio').val(response.response.evento.fkdomicilio)
                $('#fkdomicilio').selectpicker('refresh')
                
                $('#fkareasocial').val(response.response.evento.fkareasocial)
                $('#fkareasocial').selectpicker('refresh')

                $('#fktipopase').val(response.response.fktipopase)
                $('#fktipopase').selectpicker('refresh')

                $('#fkautorizacion').val(1)
                $('#fkautorizacion').selectpicker('refresh')


                document.getElementById("imagen_mensaje").src = response.message;

            } else {
                document.getElementById("imagen_mensaje").src = response.message;

                limpiar_formulario()

            }

        })
        validationInputSelects("form")
        $('#form').animate({scrollTop: 0}, 'slow');
        
    })
reload_form()

$('.delete').click(function (e) {
        console.log("delete")
        e.preventDefault()
        cb_delete = this
        b = $(this).prop('checked')
        if (!b) {
            cb_title = "Deshabilitar Propietario"

        } else {
            cb_title = "Habilitar Propietario"
        }
        swal({
            text: cb_title,
            type: "warning",
            showCancelButton: true,
            confirmButtonColor: "#673AB7",
            cancelButtonColor: "#F44336",
            confirmButtonText: "Aceptar",
            cancelButtonText: "Cancelar"
        }).then(function () {
            $(cb_delete).prop('checked', !$(cb_delete).is(':checked'))
            objeto = JSON.stringify({
                id: parseInt($(cb_delete).attr('data-id')),
                enabled: $(cb_delete).is(':checked')
            })

            ajax_call("portero_virtual_delete", {
                object: objeto,
                _xsrf: getCookie("_xsrf")
            }, null, function () {
                setTimeout(function () {
                    window.location = main_route
                }, 2000);
            })
            $('#form').modal('hide')
        })
    })

function salida(elemento){
    obj = JSON.stringify({
        'id': parseInt(JSON.parse($(elemento).attr('data-json'))),
        'fechai': $('#fechai').val(),
        'fechaf': $('#fechaf').val()
    })
    ajax_call('portero_virtual_salida', {
        _xsrf: getCookie("_xsrf"),
        object: obj
    }, null, function (response) {
        response = JSON.parse(response)
        actualizar_tabla(response)

    })



    }

$('#filtrar').click(function () {
    $("#rgm-loader").show();
    //document.getElementById("filtrar").disabled = true
    obj = JSON.stringify({
        'fechainicio': $('#fechai').val(),
        'fechafin': $('#fechaf').val(),
        '_xsrf': getCookie("_xsrf")
    })
    ruta = "portero_virtual_filtrar";
    $.ajax({
        method: "POST",
        url: ruta,
        data: {_xsrf: getCookie("_xsrf"), object: obj},
        async: true
    }).done(function (response) {

        response = JSON.parse(response)
        actualizar_tabla(response)
    })
});

validationKeyup("form")
validationSelectChange("form")