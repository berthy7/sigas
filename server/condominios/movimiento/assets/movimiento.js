main_route = '/movimiento'
var refrescar = false;

$(document).ready(function () {

    auxiliar_method()
    verificar_qr()

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
                console.log("tipopase:" + response.response.fktipopase)

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

$('#color').selectpicker({
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
                fechai =response['response'][i].fechar
            }

            if(response['response'][i].fechaf){
                fechaf = response['response'][i].fechaf
                salida= '✓'
            }else{
                fechaf = '-----'
                salida ="<button id='exit' onClick='salida(this)' data-json="+id+" type='button' class='btn bg-indigo waves-effect waves-light salida' title='Actualizar Salida'><i class='material-icons'>exit_to_app</i></button>"

            }

            if(response['response'][i].fkconductor != "None"){
                conductor= response['response'][i].conductor.nombre +" "+response['response'][i].conductor.apellidop+" "+response['response'][i].conductor.apellidom
            }else{
                conductor ='-----'
            }

            placa= response['response'][i].vehiculo.placa
            tipo = response['response'][i].vehiculo.tipo

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

            color = response['response'][i].vehiculo.color


            if(response['response'][i].fkdomicilio != "None"){
                destino = response['response'][i].domicilio.ubicacion + " " + response['response'][i].domicilio.numero
            }else if(response['response'][i].fkareasocial != "None"){
                destino = response['response'][i].areasocial.nombre
            }else{
                destino = '-----'
            }

            if(response['response'][i].fknropase != "None"){
                nropase = response['response'][i].nropase.numero
            }else{
                nropase = '-----'
            }

            data.push( [
                id,
                fechai,
                fechaf,
                response['response'][i].tipodocumento.nombre,
                response['response'][i].invitado.ci,
                response['response'][i].invitado.nombre +" "+response['response'][i].invitado.apellidop+" "+response['response'][i].invitado.apellidom,
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

        $('#fkvehiculo').val('')
        $('#fkvehiculo').selectpicker('refresh')
        $('#cantpasajeros').val('')
        $('#placa').val('')
        $('#tipo').val('')
        $('#tipo').selectpicker('refresh')
        $('#color').val('')
        $('#color').selectpicker('refresh')
        $('#fkmarca').val('')
        $('#fkmarca').selectpicker('refresh')
        $('#fkmodelo').val('')
        $('#fkmodelo').selectpicker('refresh')

        validationInputSelects("form")
    }
});

$('#fkconductor').change(function () {
    if (parseInt(JSON.parse($('#fkconductor').val())) != 0){
        cargar_conductor(parseInt(JSON.parse($('#fkconductor').val())))
    }else{
        $('#nombre_conductor').val('')
        $('#apellidop_conductor').val('')
        $('#apellidom_conductor').val('')
        $('#ci_conductor').val('')
        $('#expendido_conductor').val('')
        $('#expendido_conductor').selectpicker('refresh')


        validationInputSelects("form")
    }
});

$('#tipo_reporte').change(function () {
    if (parseInt(JSON.parse($('#fkconductor').val())) != 0){
        cargar_conductor(parseInt(JSON.parse($('#fkconductor').val())))
    }else{
        $('#nombre_conductor').val('')
        $('#apellidop_conductor').val('')
        $('#apellidom_conductor').val('')
        $('#ci_conductor').val('')
        $('#expendido_conductor').val('')
        $('#expendido_conductor').selectpicker('refresh')

        validationInputSelects("form")
    }
});

$('#fkdomicilio').change(function () {

    $('#fkareasocial').val('')
    $('#fkareasocial').selectpicker('refresh')

});

$('#fkareasocial').change(function () {

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

function cargar_conductor(id) {
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
        $('#nombre_conductor').val(response.response.nombre)
        $('#apellidop_conductor').val(response.response.apellidop)
        $('#apellidom_conductor').val(response.response.apellidom)
        $('#ci_conductor').val(response.response.ci)
        $('#expendido_conductor').val(response.response.expendido)
        $('#expendido_conductor').selectpicker('refresh')

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

$('#fkvehiculo').change(function () {
    if (parseInt(JSON.parse($('#fkvehiculo').val())) != 0){
        cargar_vehiculo(parseInt(JSON.parse($('#fkvehiculo').val())))
    }else{
        $('#cantpasajeros').val('')
        $('#placa').val('')
        $('#tipo').val('')
        $('#tipo').selectpicker('refresh')
        $('#color').val('')
        $('#color').selectpicker('refresh')
        $('#fkmarca').val('')
        $('#fkmarca').selectpicker('refresh')
        $('#fkmodelo').val('')
        $('#fkmodelo').selectpicker('refresh')
    }
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

$('#fkmarca').change(function () {

    if(parseInt(JSON.parse($('#fkmarca').val())) != 0){
        $('#div_nombre_marca').hide()
        obj = JSON.stringify({
            'idmarca': parseInt(JSON.parse($('#fkmarca').val())),
            '_xsrf': getCookie("_xsrf")
        })

        ruta = "modelo_listar_x_marca";
        //data.append('object', obj)
        //data.append('_xsrf',getCookie("_xsrf"))

        $.ajax({
            method: "POST",
            url: ruta,
            data: {_xsrf: getCookie("_xsrf"), object: obj},
            async: false
        }).done(function (response) {
            response = JSON.parse(response)
            $('#fkmodelo').html('');
            var select = document.getElementById("fkmodelo")
            for (var i = 0; i < Object.keys(response.response).length; i++) {
                var option = document.createElement("OPTION");
                option.innerHTML = response['response'][i]['nombre'];
                option.value = response['response'][i]['id'];
                select.appendChild(option);
            }
            $('#fkmodelo').selectpicker('refresh');

        })
    }else{
        
        $('#div_nombre_marca').show()
        eraseError(document.getElementById("fkmarca"))

    }


});

function cargar_vehiculo(id) {
    obj = JSON.stringify({
        'id': id,
        '_xsrf': getCookie("_xsrf")
    })

    ruta = "vehiculo_obtener";

    $.ajax({
        method: "POST",
        url: ruta,
        data: {_xsrf: getCookie("_xsrf"), object: obj},
        async: false
    }).done(function (response) {
        response = JSON.parse(response)

        console.log(response)

        // $('#cantpasajeros').val(response.response.cantpasajeros)
        $('#placa').val(response.response.placa)
        $('#tipo').val(response.response.tipo)
        $('#tipo').selectpicker('refresh')
        $('#color').val(response.response.color)
        $('#color').selectpicker('refresh')
        $('#fkmarca').val(response.response.fkmarca)
        $('#fkmarca').selectpicker('refresh')
        $('#fkmodelo').val(response.response.fkmodelo)
        $('#fkmodelo').selectpicker('refresh')
    })
    validationInputSelects("form")
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
    $('#cantpasajeros').val('')
    $('#placa').val('')
    $('#tipo').val('')
    $('#tipo').selectpicker("refresh")
    $('#color').val('')
    $('#color').selectpicker("refresh")
    $('#fkmarca').val('')
    $('#fkmarca').selectpicker("refresh")
    $('#fkmodelo').val('')
    $('#fkmodelo').selectpicker("refresh")
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

    $('#fkinvitado_conductor').val('')
    $('#fkinvitado_conductor').selectpicker("refresh")

    $('#nombre_conductor').val('')
    $('#apellidop_conductor').val('')
    $('#apellidom_conductor').val('')
    $('#ci_conductor').val('')
    $('#expendido_conductor').val('')
    $('#expendido_conductor').selectpicker("refresh")
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
    $('#placa').val('')
    $('#tipo').val('')
    $('#tipo').selectpicker("refresh")
    $('#cantpasajeros').val('1')
    $('#color').val('')
    $('#color').selectpicker("refresh")
    $('#fkmarca').val('')
    $('#fkmarca').selectpicker("refresh")
    $('#fkmodelo').val('')
    $('#fkmodelo').selectpicker("refresh")
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
    
    $('#fkconductor').val('')
    $('#fkconductor').selectpicker("refresh")

    $('#nombre_conductor').val('')
    $('#apellidop_conductor').val('')
    $('#apellidom_conductor').val('')
    $('#ci_conductor').val('')
    $('#expendido_conductor').val('')
    $('#expendido_conductor').selectpicker("refresh")

    document.getElementById("imagen_mensaje").src = "";

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
                    'fkvehiculo': $('#fkvehiculo').val(),
                    'cantpasajeros': $('#cantpasajeros').val(),
                    'placa': $('#placa').val(),
                    'tipo': $('#tipo').val(),
                    'color': $('#color').val(),
                    'fkmarca': $('#fkmarca').val(),
                    'nombre_marca': $('#nombre_marca').val(),
                    'fkmodelo': $('#fkmodelo').val(),
                    'fkdomicilio': $('#fkdomicilio').val(),
                    'fkareasocial': $('#fkareasocial').val(),
                    'fktipopase': $('#fktipopase').val(),
                    'fkautorizacion': $('#fkautorizacion').val(),
                    'fknropase': $('#nropase').val(),
                    'observacion': $('#observacion').val(),

                    'fkconductor': $('#fkconductor').val(),
                    'fktipodocumento_conductor': $('#fktipodocumento_conductor').val(),
                    'nombre_conductor': $('#nombre_conductor').val(),
                    'apellidop_conductor': $('#apellidop_conductor').val(),
                    'apellidom_conductor': $('#apellidom_conductor').val(),
                    'ci_conductor': $('#ci_conductor').val(),
                    'expendido_conductor': $('#expendido_conductor').val()
                })
                ajax_call('movimiento_insert', {
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

            ajax_call("movimiento_delete", {
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
    ajax_call('movimiento_salida', {
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
    ruta = "movimiento_filtrar";
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