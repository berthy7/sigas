main_route = '/movimiento_p'
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
                    if(!response.response.evento.multiple ){
                        if(!response.response.evento.paselibre){

                                console.log("entro invitado")
                                $('#fkinvitado').selectpicker('refresh')
                                $('#fkinvitado').val(response.response.fkinvitado)
                                $('#fkinvitado').selectpicker('refresh')
                                cargar_invitado(response.response.fkinvitado)
                            }
                    }

                    $('#fkdomicilio').val(response.response.evento.fkdomicilio)
                    $('#fkdomicilio').selectpicker('refresh')

                    $('#fkareasocial').val(response.response.evento.fkareasocial)
                    $('#fkareasocial').selectpicker('refresh')

                    $('#fktipopase').val(response.response.fktipopase)
                    $('#fktipopase').selectpicker('refresh')

                    $('#fkautorizacion').val(1)
                    $('#fkautorizacion').selectpicker('refresh')
                    cargar_nropase($( "#fktipopase option:selected" ).text())
                    
                    $('#fkresidente').val(response.response.evento.fkresidente)
                    $('#fkresidente').selectpicker('refresh')

                    document.getElementById("imagen_mensaje").src = response.message;
                    $('#codigoautorizacion').val('')
                    
                    document.getElementById('switch_multiacceso').checked=response.response.evento.multiacceso
                    document.getElementById('switch_paselibre').checked=response.response.evento.paselibre
                    document.getElementById('switch_multiple').checked=response.response.evento.multiple

                    $('#div_accesos').show()
                    
                    if (!response.response.evento.paselibre) {
                        $('#nombre').prop("required", true);
                        $('#apellidop').prop("required", true);
                        $('#ci').prop("required", true);

                        $('#placa').prop("required", true);
                        $('#fkcolor').prop("required", true);
                        $('#fkmarca').prop("required", true);

                        $('#fktipodocumento').val(1)
                        $('#fktipodocumento').selectpicker("refresh")

                        $('.div_vehiculo').show()

                    } else {
                        $('#nombre').removeAttr("required");
                        eraseError('nombre')
                        $('#apellidop').removeAttr("required");
                        eraseError('apellidop')
                        $('#ci').removeAttr("required");
                        eraseError('ci')

                        $('#placa').removeAttr("required");
                        eraseError('placa')
                        $('#fkcolor').removeAttr("required");
                        eraseError('fkcolor')
                        $('#fkmarca').removeAttr("required");
                        eraseError('fkmarca')

                        $('#fktipodocumento').val(4)
                        $('#fktipodocumento').selectpicker("refresh")

                        $('.div_visita').hide()
                        $('.div_vehiculo').hide()
                        
                    }

                } else {
                    $('#fktipodocumento').val(1)
                    $('#fktipodocumento').selectpicker("refresh")
                    
                    document.getElementById("imagen_mensaje").src = response.message;

                    document.getElementById('switch_multiacceso').checked=false
                    document.getElementById('switch_paselibre').checked=false
                    document.getElementById('switch_multiple').checked=false
                    $('#div_accesos').hide()
                    
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
                    // // $('#fktipopase').val(response.response.fktipopase)
                    // // $('#fktipopase').selectpicker('refresh')
                    //
                    $('#fktipodocumento').val(response.response.tipodocumento)
                    $('#fktipodocumento').selectpicker('refresh')

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

$('#fkvehiculo').selectpicker({
    size: 10,
    liveSearch: true,
    liveSearchPlaceholder: 'Buscar Vehiculo',
    title: 'Seleccione Vehiculo'
})

$('#fkdomicilio').selectpicker({
    size: 10,
    liveSearch: true,
    liveSearchPlaceholder: 'Buscar',
    title: 'Seleccione'
})

$('#fkareasocial').selectpicker({
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

$('#fkmarca').selectpicker({
    size: 10,
    liveSearch: true,
    liveSearchPlaceholder: 'Buscar',
    title: 'Seleccione'
})

$('#fkmodelo').selectpicker({
    size: 10,
    liveSearch: true,
    liveSearchPlaceholder: 'Buscar',
    title: 'Seleccione'
})

$('#expendido').selectpicker({
    size: 10,
    liveSearch: true,
    liveSearchPlaceholder: 'Buscar',
    title: 'Seleccione'
})

$('#expendido_conductor').selectpicker({
    size: 10,
    liveSearch: true,
    liveSearchPlaceholder: 'Buscar',
    title: 'Seleccione'
})

$('#nropase').selectpicker({
    size: 10,
    liveSearch: true,
    liveSearchPlaceholder: 'Buscar',
    title: 'Seleccione'
})

$('#switch_visita').change(function() {
   sw_visita = $(this).prop('checked')
    limpiar_formulario()
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
        $('#div_accesos').hide()
        document.getElementById('switch_multiacceso').checked=false
        document.getElementById('switch_paselibre').checked=false
        document.getElementById('switch_multiple').checked=false


    }

})

$('#switch_refrescar').change(function() {
   var sw_refrescar = $(this).prop('checked')

    if(sw_refrescar){
       refrescar = true;
       console.log(refrescar)

    }else{
        refrescar = false;
        console.log(refrescar)
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
               exportOptions : { columns : [0, 1, 2, 3, 4, 5 ,6 ,7,8,9]},
                sheetName: 'Control y Registro Peatonal',
               title: 'Control y Registro Peatonal'  },
            {  extend : 'pdfHtml5',
                orientation: 'landscape',
               customize: function(doc) {
                    doc.styles.tableBodyEven.alignment = 'center';
                    doc.styles.tableBodyOdd.alignment = 'center';
               },
               exportOptions : {
                    columns : [0, 1, 2, 3, 4, 5 ,6 ,7,8,9]
                },
               title: 'Control y Registro Peatonal'
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
    var tipodocumento;
    var ci;
    var nombre;

    var destino;
    var nropase;
    var salida;

    for (var i = 0; i < Object.keys(response.response).length; i++) {
        id = response['response'][i].id

        if(response['response'][i].fechai){
            fechai= response['response'][i].fechai
        }else{
            fechai =response['response'][i].fechar
            // fechai = '-----'
        }

        if(response['response'][i].fechaf){
            fechaf = response['response'][i].fechaf
            salida= '✓'
        }else{
            fechaf = '-----'
            salida ="<button id='exit' onClick='salida(this)' data-json="+id+" type='button' class='btn bg-indigo waves-effect waves-light salida' title='Actualizar Salida'><i class='material-icons'>exit_to_app</i></button>"

        }
        
        if(response['response'][i].fktipodocumento){
                tipodocumento= response['response'][i].tipodocumento.nombre
            }else{
                tipodocumento = '-----'
            }

        if(response['response'][i].fkinvitado != "None"){
            ci = response['response'][i].invitado.ci,
            nombre = response['response'][i].invitado.nombre +" "+response['response'][i].invitado.apellidop+" "+response['response'][i].invitado.apellidom

        }else{
            ci ='Residente'
            nombre = response['response'][i].residente.nombre +" "+response['response'][i].residente.apellidop+" "+response['response'][i].residente.apellidom
        }
        
        if(response['response'][i].fkdomicilio != "None"){
            destino = response['response'][i].domicilio.ubicacion
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
            tipodocumento,
            ci,
            nombre,
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
               exportOptions : { columns : [0, 1, 2, 3, 4, 5 ,6 ,7,8,9,10]},
                sheetName: 'Reporte Control y Registro Peaonal',
               title: 'Control y Registro Peaonal'  },
            {  extend : 'pdfHtml5',
                orientation: 'landscape',
               customize: function(doc) {
                    doc.styles.tableBodyEven.alignment = 'center';
                    doc.styles.tableBodyOdd.alignment = 'center';
               },
               exportOptions : {
                    columns : [0, 1, 2, 3, 4, 5 ,6 ,7,8,9,10]
                },
               title: 'Control y Registro Peaonal'
            }
        ],
        initComplete: function () {


        },
        "order": [[ 1, "desc" ]],
        language : {
            'url': '/resources/js/spanish.json',
        },
        "pageLength": 50
    });


}

$('#fktipopase').change(function () {

    obj = JSON.stringify({
        'tipopase': $( "#fktipopase option:selected" ).text(),
        '_xsrf': getCookie("_xsrf")
    })

    ruta = "nropase_listar_tipo";
    //data.append('object', obj)
    //data.append('_xsrf',getCookie("_xsrf"))

    $.ajax({
        method: "POST",
        url: ruta,
        data: {_xsrf: getCookie("_xsrf"), object: obj},
        async: false
    }).done(function (response) {
        response = JSON.parse(response)

        $('#nropase').html('');
        var select = document.getElementById("nropase")
        for (var i = 0; i < Object.keys(response.response).length; i++) {
            var option = document.createElement("OPTION");
            option.innerHTML = response['response'][i]['numero'] +" - "+response['response'][i]['tipo'];
            option.value = response['response'][i]['id'];
            select.appendChild(option);
        }
        $('#nropase').selectpicker('refresh');

    })

});

function cargar_nropase(tipopase) {

        obj = JSON.stringify({
        'tipopase': tipopase,
        '_xsrf': getCookie("_xsrf")
    })

    ruta = "nropase_listar_tipo";
    //data.append('object', obj)
    //data.append('_xsrf',getCookie("_xsrf"))

    $.ajax({
        method: "POST",
        url: ruta,
        data: {_xsrf: getCookie("_xsrf"), object: obj},
        async: false
    }).done(function (response) {
        response = JSON.parse(response)

        $('#nropase').html('');
        var select = document.getElementById("nropase")
        for (var i = 0; i < Object.keys(response.response).length; i++) {
            var option = document.createElement("OPTION");
            option.innerHTML = response['response'][i]['numero'] +" - "+response['response'][i]['tipo'];
            option.value = response['response'][i]['id'];
            select.appendChild(option);
        }
        $('#nropase').selectpicker('refresh');

    })

}

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

    $('#fkareasocial').val('')
    $('#fkareasocial').selectpicker('refresh')

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

        if(Object.keys(response.response).length == 0){
            $('#fkresidente').val('')
            $('#fkresidente').selectpicker('refresh');

        }else{
            for (var i = 0; i < Object.keys(response.response).length; i++) {

                $('#fkresidente').val(response['response'][i]['id'])
                $('#fkresidente').selectpicker('refresh');

                break;

            }

        }




    })

}

$('#fkareasocial').change(function () {
    
        cargar_residente('0')

        $('#fkdomicilio').val('')
        $('#fkdomicilio').selectpicker('refresh')

});

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
    $('#fkvehiculo').val('')
    $('#fkvehiculo').selectpicker("refresh")
    $('#nombre').val('')
    $('#apellidop').val('')
    $('#apellidom').val('')
    $('#ci').val('')
    $('#expendido').val('')
    $('#expendido').selectpicker("refresh")
    $('#fkdomicilio').val('')
    $('#fkdomicilio').selectpicker("refresh")
    $('#fkareasocial').val('')
    $('#fkareasocial').selectpicker("refresh")
    $('#fktipopase').val('')
    $('#fktipopase').selectpicker("refresh")
    $('#fkautorizacion').val('')
    $('#fkautorizacion').selectpicker("refresh")
    $('#codigoautorizacion').val('')
    $('#codigoautorizacion_residente').val('')
    $('#nropase').val('')
    $('#nropase').selectpicker("refresh")

    $('#fkinvitado_conductor').val('')
    $('#fkinvitado_conductor').selectpicker("refresh")

    $('#nombre_conductor').val('')
    $('#apellidop_conductor').val('')
    $('#apellidom_conductor').val('')
    $('#ci_conductor').val('')
    $('#expendido_conductor').val('')
    $('#expendido_conductor').selectpicker("refresh")

    $('#div_accesos').hide()
    document.getElementById('switch_multiacceso').checked=false
    document.getElementById('switch_paselibre').checked=false
    document.getElementById('switch_multiple').checked=false
}

$('#new').click(function () {
    $('#fkinvitacion').val('')
    $('#fkinvitado').val('')
    $('#fkinvitado').selectpicker("refresh")
    $('#fkvehiculo').val('')
    $('#fkvehiculo').selectpicker("refresh")
    $('#nombre').val('')
    $('#apellidop').val('')
    $('#apellidom').val('')
    $('#ci').val('')
    $('#expendido').val('')
    $('#expendido').selectpicker("refresh")
    $('#fkdomicilio').val('')
    $('#fkdomicilio').selectpicker("refresh")
    $('#fkareasocial').val('')
    $('#fkareasocial').selectpicker("refresh")
    $('#fktipopase').val('')
    $('#fktipopase').selectpicker("refresh")
    $('#fkautorizacion').val('')
    $('#fkautorizacion').selectpicker("refresh")
    $('#codigoautorizacion').val('')
    $('#nropase').val('')
    $('#nropase').selectpicker("refresh")
    $('#observaciones').val('')


    document.getElementById("imagen_mensaje").src = "";
    
    document.getElementById('switch_visita').checked=true
    $('#switch_visita').change()
        $('#div_accesos').hide()
    document.getElementById('switch_multiacceso').checked=false
    document.getElementById('switch_paselibre').checked=false
    document.getElementById('switch_multiple').checked=false

    verif_inputs('')
    validationInputSelects("form")
    $('#id_div').hide()
    $('#insert').show()
    $('#update').hide()
    $('#form').modal('show')
})

$('#insert').click(function () {

    if ($('#fkdomicilio').val() == "" && $('#fkareasocial').val() == ""){

        swal(
            'Error de datos.',
             'Seleccione Destino',
            'warning'
        )
    }else{
        if($('#switch_paselibre').prop('checked')){
                    notvalid = validationInputSelectsWithReturn("form");
                    if (notvalid===false) {
                        objeto = JSON.stringify({
                            'fkinvitacion': $('#fkinvitacion').val(),
                            'codigoautorizacion': $('#codigoautorizacion').val(),
                            'fktipodocumento': $('#fktipodocumento').val(),
                            'fkinvitado': $('#fkinvitado').val(),
                            'nombre': $('#nombre').val(),
                            'apellidop': $('#apellidop').val(),
                            'apellidom': $('#apellidom').val(),
                            'ci': $('#ci').val(),
                            'expendido': $('#expendido').val(),
                            'fkdomicilio': $('#fkdomicilio').val(),
                            'fkareasocial': $('#fkareasocial').val(),
                            'fktipopase': $('#fktipopase').val(),
                            'fkautorizacion': $('#fkautorizacion').val(),
                            'fkresidente': $('#fkresidente').val(),
                            'fknropase': $('#nropase').val(),
                            'observacion': $('#observacion').val(),
                            'visita': sw_visita,

                        })
                        ajax_call('movimiento_p_insert', {
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
            }else{

            if($('#fkmarca').val() == 0 && $('#nombre_marca').val() == ""){

                swal(
                    'Error de datos.',
                     'Ingrese Marca del vehiculo',
                    'warning'
                )
            }else{
                notvalid = validationInputSelectsWithReturn("form");
                if (notvalid===false) {
                    objeto = JSON.stringify({
                        'fkinvitacion': $('#fkinvitacion').val(),
                        'codigoautorizacion': $('#codigoautorizacion').val(),
                        'fktipodocumento': $('#fktipodocumento').val(),
                        'fkinvitado': $('#fkinvitado').val(),
                        'nombre': $('#nombre').val(),
                        'apellidop': $('#apellidop').val(),
                        'apellidom': $('#apellidom').val(),
                        'ci': $('#ci').val(),
                        'expendido': $('#expendido').val(),
                        'fkdomicilio': $('#fkdomicilio').val(),
                        'fkareasocial': $('#fkareasocial').val(),
                        'fktipopase': $('#fktipopase').val(),
                        'fkautorizacion': $('#fkautorizacion').val(),
                        'fkresidente': $('#fkresidente').val(),
                        'fknropase': $('#nropase').val(),
                        'observacion': $('#observacion').val(),
                        'visita': sw_visita,

                    })
                    ajax_call('movimiento_p_insert', {
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

            }
        }
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

            ajax_call("movimiento_p_delete", {
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
    ajax_call('movimiento_p_salida', {
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
    ruta = "movimiento_p_filtrar";
    $.ajax({
        method: "POST",
        url: ruta,
        data: {_xsrf: getCookie("_xsrf"), object: obj},
        async: true
    }).done(function (response) {

        response = JSON.parse(response)
        console.log(response)
        actualizar_tabla(response)
    })
});


validationKeyup("form")
validationSelectChange("form")