main_route = '/movimiento';
var refrescar = false;
var sw_visita = false;

var data_lista = [];

var ult_registro = 0;

var data_lista_pendientes = [];


$(document).ready(function () {

    auxiliar_method()
    verificar_qr()
    verificar_qr_residente()

});

var fechahoy = new Date();
var hoy = fechahoy.getDate()+"/"+(fechahoy.getMonth()+1) +"/"+fechahoy.getFullYear()

document.getElementById("fechai").value=hoy
document.getElementById("fechaf").value=hoy

function auxiliar_method() {
    //main_method()
    //setTimeout(auxiliar_method, 10000)
    setInterval(function(){

        if($("#form").is(":visible")){
            console.log("actualizar desactivado")
        }else{
            if(refrescar == false){
                actualizar_tabla_x_fechas(hoy,hoy,ult_registro)
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
                $('.div_vehiculo').show()

                if (response.success) {
                    $('#fkinvitacion').val(response.response.id)

                    if(!response.response.evento.multiple ){
                        if(!response.response.evento.paselibre){

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
                        $('.div_visita').show()

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

function actualizar_tabla_x_fechas(fechainicio,fechafin,ult_registro_parametro) {
        obj = JSON.stringify({
        'fechainicio': fechainicio,
        'fechafin': fechafin, 
        'ult_registro': ult_registro_parametro,
        '_xsrf': getCookie("_xsrf")
    })
    ruta = "movimiento_recargar";
    $.ajax({
        method: "POST",
        url: ruta,
        data: {_xsrf: getCookie("_xsrf"), object: obj},
        async: true,

    }).done(function (response) {
        response = JSON.parse(response)

        var data = [];
        var salida;
        var fechainicio;

        for (var i = 0; i < Object.keys(response.response).length; i++) {

                if(i == 0){
                ult_registro = response['response'][i].id
                    // console.log("i = 0 : "+ult_registro)
                }

                if(response['response'][i].descripcion_fechaf != '-----'){
                    salida= "<i class='Medium material-icons icon-cog'>check_circle</i>"
                }else{
                    salida ="<button id='exit' onClick='salida(this)' data-json="+response['response'][i].id+" type='button' class='btn bg-indigo white-own waves-effect waves-light salida' title='Actualizar Salida'><i class='material-icons'>exit_to_app</i></button>"
                }

                if($('#idperfil').val() == 1){
                    salida += "<button id='delete' onClick='eliminar(this)' data-json='"+response['response'][i].id+"' type='button' class='btn bg-indigo waves-effect waves-light white-own' title='Eliminar'><i class='material-icons'>delete</i></button> "
                }
                console.log("cargar Tabla: "+response['response'][i].fechai)
                 if(response['response'][i].fechai){
                    fechainicio = response['response'][i].descripcion_fechai
                }else{
                    fechainicio = response['response'][i].fechar.strftime('%d/%m/%Y %H:%M:%S')
                }

                data_lista.push( [
                    response['response'][i].id,
                    fechainicio,
                    response['response'][i].descripcion_fechaf,
                    response['response'][i].descripcion_documento,
                    response['response'][i].descripcion_ci_invitado,
                    response['response'][i].descripcion_nombre_invitado,
                    response['response'][i].descripcion_nombre_conductor,
                    response['response'][i].cantpasajeros,
                    response['response'][i].descripcion_placa,
                    response['response'][i].descripcion_tipo,
                    response['response'][i].descripcion_marca,
                    response['response'][i].descripcion_color,
                    response['response'][i].descripcion_destino,
                    response['response'][i].descripcion_residente,
                    response['response'][i].autorizacion.nombre,
                    response['response'][i].descripcion_nropase,
                    response['response'][i].tipopase.nombre,
                    salida
                ]);
        }

        cargar_tabla(data_lista)
    })
}

$('#fdomicilio').selectpicker({
    size: 10,
    liveSearch: true,
    liveSearchPlaceholder: 'Buscar',
    title: 'Seleccione'
})

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

$('#fresidente').selectpicker({
    size: 10,
    liveSearch: true,
    liveSearchPlaceholder: 'Buscar',
    title: 'Seleccione'
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

$('#fkcolor').selectpicker({
    size: 10,
    liveSearch: true,
    liveSearchPlaceholder: 'Buscar',
    title: 'Seleccione'
})

    $('#reporte-xls').click(function () {

        obj = JSON.stringify({
            'fechainicio': $('#fechai').val(),
            'fechafin': $('#fechaf').val(),
            '_xsrf': getCookie("_xsrf")
        })
        ruta = "/movimiento_reporte_xls";
        $.ajax({
            method: "POST",
            url: ruta,
            data:{_xsrf: getCookie("_xsrf"), object: obj},
            async: false
        }).done(function(response){
            response = JSON.parse(response)

            if (response.success) {
                $('#link_excel').attr('href', response.response.url).html(response.response.nombre)
            }
        })
        $('#modal-rep-xls').modal('show')
    })

    $('#importar_Excel').click(function () {
    $(".xlsfl").each(function () {
        $(this).fileinput('refresh',{
            allowedFileExtensions: ['xlsx', 'txt'],
            maxFileSize: 2000,
            maxFilesNum: 1,
            showUpload: false,
            layoutTemplates: {
                main1: '{preview}\n' +
                    '<div class="kv-upload-progress hide"></div>\n' +
                    '<div class="input-group {class}">\n' +
                    '   {caption}\n' +
                    '   <div class="input-group-btn">\n' +
                    '       {remove}\n' +
                    '       {cancel}\n' +
                    '       {browse}\n' +
                    '   </div>\n' +
                    '</div>',
                main2: '{preview}\n<div class="kv-upload-progress hide"></div>\n{remove}\n{cancel}\n{browse}\n',
                preview: '<div class="file-preview {class}">\n' +
                    '    {close}\n' +
                    '    <div class="{dropClass}">\n' +
                    '    <div class="file-preview-thumbnails">\n' +
                    '    </div>\n' +
                    '    <div class="clearfix"></div>' +
                    '    <div class="file-preview-status text-center text-success"></div>\n' +
                    '    <div class="kv-fileinput-error"></div>\n' +
                    '    </div>\n' +
                    '</div>',
                icon: '<span class="glyphicon glyphicon-file kv-caption-icon"></span>',
                caption: '<div tabindex="-1" class="form-control file-caption {class}">\n' +
                    '   <div class="file-caption-name"></div>\n' +
                    '</div>',
                btnDefault: '<button type="{type}" tabindex="500" title="{title}" class="{css}"{status}>{icon}{label}</button>',
                btnLink: '<a href="{href}" tabindex="500" title="{title}" class="{css}"{status}>{icon}{label}</a>',
                btnBrowse: '<div tabindex="500" class="{css}"{status}>{icon}{label}</div>',
                progress: '<div class="progress">\n' +
                    '    <div class="progress-bar progress-bar-success progress-bar-striped text-center" role="progressbar" aria-valuenow="{percent}" aria-valuemin="0" aria-valuemax="100" style="width:{percent}%;">\n' +
                    '        {percent}%\n' +
                    '     </div>\n' +
                    '</div>',
                footer: '<div class="file-thumbnail-footer">\n' +
                    '    <div class="file-caption-name" style="width:{width}">{caption}</div>\n' +
                    '    {progress} {actions}\n' +
                    '</div>',
                actions: '<div class="file-actions">\n' +
                    '    <div class="file-footer-buttons">\n' +
                    '        {delete} {other}' +
                    '    </div>\n' +
                    '    {drag}\n' +
                    '    <div class="file-upload-indicator" title="{indicatorTitle}">{indicator}</div>\n' +
                    '    <div class="clearfix"></div>\n' +
                    '</div>',
                actionDelete: '<button type="button" class="kv-file-remove {removeClass}" title="{removeTitle}"{dataUrl}{dataKey}>{removeIcon}</button>\n',
                actionDrag: '<span class="file-drag-handle {dragClass}" title="{dragTitle}">{dragIcon}</span>'
            }
        })
    });
    verif_inputs('')

    $('#id_div').hide()
    $('#insert-importar').show()
    $('#form-importar').modal('show')
})

$('#insert-importar').on('click',function (e) {
     e.preventDefault();

    var data = new FormData($('#importar-form')[0]);

    ruta = "movimiento_importar";
    data.append('_xsrf', getCookie("_xsrf"))
    render = null
    callback = function () {
        setTimeout
        (function () {
            window.location = main_route
        }, 2000);
    }
    $.ajax({
        url: ruta,
        type: "post",
        data: data,
        contentType: false,
        processData: false,
        cache: false,
        async: false
    }).done(function (response) {
        $('.page-loader-wrapper').hide();
        $('#form').modal('hide');
        response = JSON.parse(response)

        if (response.success) {
            swal({
                title: "Operacion Correcta...",
                text: response.message,
                type: "success",
                showCancelButton: false,
                confirmButtonColor: "#DD6B55",
                confirmButtonText: "Confirmar"
            }).then(function () {
                $('#form-importar').modal('hide')
                setTimeout(function () {
                    window.location = main_route
                }, 500);
            });
        } else {
            swal("Operacion Fallida", response.message, "error").then(function () {
                query_render('/movimiento');
            });
        }
    })
    $('#form').modal('hide')
})

$('#fresidente').change(function() {
    $('#fdomicilio').val('')
    $('#fdomicilio').selectpicker('refresh')
})

$('#fdomicilio').change(function() {
    $('#fresidente').val('')
    $('#fresidente').selectpicker('refresh')
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
    $('.div_vehiculo').show()
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

    }else{
        refrescar = false;
    }

})

function cargar_tabla(data){
    data_lista = data

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
    var salida;
    var fechai;

    for (var i = 0; i < Object.keys(response.response).length; i++) {

            if(response['response'][i].fechaf != '-----'){
                salida= "<i class='Medium material-icons icon-cog'>check_circle</i>"
            }else{
                salida ="<button id='exit' onClick='salida(this)' data-json="+response['response'][i].id+" type='button' class='btn bg-indigo white-own waves-effect waves-light salida' title='Actualizar Salida'><i class='material-icons'>exit_to_app</i></button>"
            }

                if($('#idperfil').val() == 1){
                    salida += "<button id='delete' onClick='eliminar(this)' data-json="+response['response'][i].id+" type='button' class='btn bg-indigo waves-effect waves-light white-own' title='Eliminar'><i class='material-icons'>delete</i></button> "
                }

             if(response['response'][i].fechai == '-----'){
                fechai= response['response'][i].fechar
            }else{
                fechai =response['response'][i].fechai
            }

        
            data.push( [
            response['response'][i].id,
            fechai,
            response['response'][i].fechaf,
            response['response'][i].documento,
            response['response'][i].ci_invitado,
            response['response'][i].nombre_invitado,
            response['response'][i].nombre_conductor,
            response['response'][i].cantpasajeros,
            response['response'][i].placa,
            response['response'][i].tipo,
            response['response'][i].marca,
            response['response'][i].color,
            response['response'][i].destino,
            response['response'][i].residente,
            response['response'][i].autorizacion,
            response['response'][i].nropase,
            response['response'][i].tipopase,
                salida
            ]);
    }

    cargar_tabla(data)

}

$('#codigoautorizacion').change(function () {
    console.log("cambio input")


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
    
    // cargar_residente($('#fkdomicilio').val())

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

$('#fkareasocial').change(function () {

        cargar_residente('0')

        $('#fkdomicilio').val('')
        $('#fkdomicilio').selectpicker('refresh')

});

$('#fkresidente').change(function () {
    
    obj = JSON.stringify({
        'id': parseInt($('#fkresidente').val())
    })
    ajax_call_get('residente_update', {
        _xsrf: getCookie("_xsrf"),
        object: obj
    }, function (response) {

        var self = response;

            for (invi in self.domicilios) {
                $('#fkdomicilio').val(self.domicilios[invi]['fkdomicilio'])
                $('#fkdomicilio').selectpicker('refresh')

            }

            $('#fkautorizacion').val(1)
            $('#fkautorizacion').selectpicker('refresh')


    })

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
        // $('#cantpasajeros').val('0')
        $('#placa').val('')
        $('#fktipo').val('')
        $('#fktipo').selectpicker('refresh')
        $('#fkcolor').val('')
        $('#fkcolor').selectpicker('refresh')
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

        // $('#cantpasajeros').val(response.response.cantpasajeros)
        $('#placa').val(response.response.placa)
        $('#fktipo').val(response.response.fktipo)
        $('#fktipo').selectpicker('refresh')
        $('#fkcolor').val(response.response.fkcolor)
        $('#fkcolor').selectpicker('refresh')
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
    $('#cantpasajeros').val('0')
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
    $('#fkresidente').val('')
    $('#fkresidente').selectpicker("refresh")
    $('#codigoautorizacion').val('')
    $('#codigoautorizacion_residente').val('')
    $('#nropase').val('')
    $('#nropase').selectpicker("refresh")
     $('#observacion').val('')

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
    $('#placa').val('')
    $('#fktipo').val('')
    $('#fktipo').selectpicker("refresh")
    $('#cantpasajeros').val('0')
    $('#fkcolor').val('')
    $('#fkcolor').selectpicker("refresh")
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
    $('#fkresidente').val('')
    $('#fkresidente').selectpicker("refresh")
    $('#codigoautorizacion').val('')
    $('#codigoautorizacion_residente').val('')
    $('#nropase').val('')
    $('#nropase').selectpicker("refresh")
    $('#observacion').val('')
    
    $('#fkconductor').val('')
    $('#fkconductor').selectpicker("refresh")

    $('#nombre_conductor').val('')
    $('#apellidop_conductor').val('')
    $('#apellidom_conductor').val('')
    $('#ci_conductor').val('')
    $('#expendido_conductor').val('')
    $('#expendido_conductor').selectpicker("refresh")
    $('#show_img').attr('src', '');
    $('#show_img').parent().parent().show();

    document.getElementById("imagen_mensaje").src = "";

    document.getElementById('switch_visita').checked=true
    $('#switch_visita').change()
    $('#div_accesos').hide()
    document.getElementById('switch_multiacceso').checked=false
    document.getElementById('switch_paselibre').checked=false
    document.getElementById('switch_multiple').checked=false

    $('.div_visita').show()
    $('.div_vehiculo').show()

        $('#expendido_conductor').val('')
    $('#expendido_conductor').selectpicker("refresh")
    
    $('#fktipodocumento').val(1)
    $('#fktipodocumento').selectpicker("refresh")


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
        if ($('#fkresidente').val() == ""){

            swal(
                'Error de datos.',
                 'Seleccione Residente',
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
                        'fkvehiculo': $('#fkvehiculo').val(),
                        'cantpasajeros': $('#cantpasajeros').val(),
                        'placa': $('#placa').val(),
                        'fktipo': $('#fktipo').val(),
                        'fkcolor': $('#fkcolor').val(),
                        'fkmarca': $('#fkmarca').val(),
                        'nombre_marca': $('#nombre_marca').val(),
                        'fkmodelo': $('#fkmodelo').val(),
                        'fkdomicilio': $('#fkdomicilio').val(),
                        'fkareasocial': $('#fkareasocial').val(),
                        'fktipopase': $('#fktipopase').val(),
                        'fkautorizacion': $('#fkautorizacion').val(),
                        'fkresidente': $('#fkresidente').val(),
                        'fknropase': $('#nropase').val(),
                        'observacion': $('#observacion').val(),
                        'visita': sw_visita,

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
                            'fktipo': $('#fktipo').val(),
                            'fkcolor': $('#fkcolor').val(),
                            'fkmarca': $('#fkmarca').val(),
                            'nombre_marca': $('#nombre_marca').val(),
                            'fkmodelo': $('#fkmodelo').val(),
                            'fkdomicilio': $('#fkdomicilio').val(),
                            'fkareasocial': $('#fkareasocial').val(),
                            'fktipopase': $('#fktipopase').val(),
                            'fkautorizacion': $('#fkautorizacion').val(),
                            'fkresidente': $('#fkresidente').val(),
                            'fknropase': $('#nropase').val(),
                            'observacion': $('#observacion').val(),
                            'visita': sw_visita,

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
        'fechaf': $('#fechaf').val(),
        '_xsrf': getCookie("_xsrf")
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
        'fresidente': $('#fresidente').val(),
        'fdomicilio': $('#fdomicilio').val(),
        '_xsrf': getCookie("_xsrf")
    })
    ruta = "movimiento_filtrar";
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
        actualizar_tabla(response)

    })
});


$('#buscarInvitado').click(function () {
    obj = JSON.stringify({
        'ci': $('#ci').val()
    })
    ajax_call_get('invitado_buscar', {
        _xsrf: getCookie("_xsrf"),
        object: obj
    }, function (response) {
        var self = response;

        if (self){
            $('#fkinvitado').val(self.id)
            $('#nombre').val(self.nombre)
            $('#apellidop').val(self.apellidop)
            $('#apellidom').val(self.apellidom)
            $('#expendido').val(self.expendido)
            $('#expendido').selectpicker('refresh')
            validationInputSelects("form")

        }else{
            $('#fkinvitado').val('')
            $('#nombre').val('')
            $('#apellidop').val('')
            $('#apellidom').val('')
            $('#expendido').val('')
            $('#expendido').selectpicker('refresh')

        }



    })
})

$('#buscarConductor').click(function () {
    obj = JSON.stringify({
        'ci': $('#ci_conductor').val()
    })
    ajax_call_get('invitado_buscar', {
        _xsrf: getCookie("_xsrf"),
        object: obj
    }, function (response) {
        var self = response;
        if (self){
            $('#fkconductor').val(self.id)
            $('#nombre_conductor').val(self.nombre)
            $('#apellidop_conductor').val(self.apellidop)
            $('#apellidom_conductor').val(self.apellidom)
            $('#expendido_conductor').val(self.expendido)
            $('#expendido_conductor').selectpicker('refresh')
            validationInputSelects("form")

        }else{
            $('#fkconductor').val('')
            $('#nombre_conductor').val('')
            $('#apellidop_conductor').val('')
            $('#apellidom_conductor').val('')
            $('#expendido_conductor').val('')
            $('#expendido').selectpicker('refresh')

        }



    })
})


$('#buscarVehiculo').click(function () {
    obj = JSON.stringify({
        'placa': $('#placa').val()
    })
    ajax_call_get('vehiculo_buscar', {
        _xsrf: getCookie("_xsrf"),
        object: obj
    }, function (response) {
        var self = response;

        if (self){

            $('#fktipo').val(self.fktipo)
            $('#fktipo').selectpicker('refresh')
            $('#fkcolor').val(self.fkcolor)
            $('#fkcolor').selectpicker('refresh')
            $('#fkmarca').val(self.fkmarca)
            $('#fkmarca').selectpicker('refresh')
            $('#fkmodelo').val(self.fkmodelo)
            $('#fkmodelo').selectpicker('refresh')

            validationInputSelects("form")

        }else{
            $('#tipo').val('')
            $('#tipo').selectpicker('refresh')
            $('#color').val('')
            $('#color').selectpicker('refresh')
            $('#fkmarca').val('')
            $('#fkmarca').selectpicker('refresh')
            $('#fkmodelo').val('')
            $('#fkmodelo').selectpicker('refresh')

        }



    })
})

function eliminar(elemento){
    cb_delete = elemento
    b = $(elemento).prop('checked')
    if (!b) {
        cb_title = "¿Deshabilitar Movimiento?"

    } else {
        cb_title = "¿Habilitar Movimiento?"
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
        objeto = JSON.stringify({
            id: JSON.parse($(elemento).attr('data-json'))
        })
        ajax_call('movimiento_delete', {
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