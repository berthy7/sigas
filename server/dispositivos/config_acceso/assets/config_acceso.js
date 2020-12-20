main_route = '/config_acceso'

$(document).ready(function () {
   
});

$(document).ajaxStart(function () { });

$(document).ajaxStop(function () {
    $.Toast.hideToast();
});


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
            // {  extend : 'excelHtml5',
            //    exportOptions : { columns : [0, 1, 2, 3, 4, 5 ,6 ,7]},
            //     sheetName: 'Reporte Areas Sociales',
            //    title: 'reas Sociales'  },
            // {  extend : 'pdfHtml5',
            //     orientation: 'landscape',
            //    customize: function(doc) {
            //         doc.styles.tableBodyEven.alignment = 'center';
            //         doc.styles.tableBodyOdd.alignment = 'center';
            //    },
            //    exportOptions : {
            //         columns : [0, 1, 2, 3, 4, 5 ,6 ,7]
            //     },
            //    title: 'reas Sociales'
            // }
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

$('#fkcondominio').selectpicker({
    size: 10,
    liveSearch: true,
    liveSearchPlaceholder: 'Buscar condominio',
    title: 'Seleccione un Condominio'
})



$('#fkcondominio').change(function () {

    cargar_cerraduras($('#fkcondominio').val())

    cargar_tarjetas($('#fkcondominio').val())

});

function append_input_cerraduras(id_in) {

        $('#cerraduras_div').append(
        '<div class="row">\
            <div class="col-sm-1" hidden>\
                <div class="input-group">\
                <input  id="id'+id_in+'" class="form-control configcerraduras txta-own"readonly>\
                </div>\
            </div>\
            <div class="col-sm-1" hidden>\
                <div class="input-group">\
                <input  id="fkcerraduras'+id_in+'" class="form-control configcerraduras  txta-own"readonly>\
                </div>\
            </div>\
            <div class="col-sm-3">\
                <div class="form-line">\
                    <input id="nombre_dispositivo'+id_in+'" data-id="'+id_in+'" class="form-control txta-own"readonly>\
                </div>\
            </div>\
            <div class="col-sm-1">\
                <div class="form-line">\
                <input  id="numero'+id_in+'" class="form-control txta-own"readonly>\
                </div>\
            </div>\
            <div class="col-sm-3">\
                <div class="form-line">\
                    <input id="nombre'+id_in+'" data-id="'+id_in+'" class="form-control txta-own"readonly>\
                </div>\
            </div>\
            <div class="col-sm-3">\
                <div  class="form-line">\
                    <input id="entrada'+id_in+'" data-id="'+id_in+'" class="form-control  txta-own"readonly>\
                </div>\
            </div>\
            <div class="col-md-2 ">\
                <input id="b_'+id_in+'" type="checkbox" class="regular-checkbox big-checkbox  configcerraduras" data-id="1" >\
                <label for="b_'+id_in+'"></label>\
            </div>\
        </div>\
        </br>'
    )


    }

function obtener_cerraduras() {
        objeto = []
        objeto_inputs = $('.configcerraduras')

        for(i=0;i<objeto_inputs.length;i+=3){
            h0 = objeto_inputs[i].value
            h1 = objeto_inputs[i+1].value
            h2 = objeto_inputs[i+2].checked

            objeto.push((function add_hours(h0,h1,h2) {

                if (h0 ==''){
                    return {
                    'fkcerraduras': h1,
                    'estado': h2

                    }

                }else{
                    return {
                    'id':h0,
                    'fkcerraduras': h1,
                    'estado': h2
                    }
                }

            })(
                    h0,
                    h1,
                    h2))
        }
        return objeto
    }

function cargar_cerraduras(fkcondominio) {

    obj = JSON.stringify({
        'idcondominio': parseInt(JSON.parse(fkcondominio)),
        '_xsrf': getCookie("_xsrf")
    })

    ruta = "dispositivo_listar_condominio";
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
        for (dis in response.response ) {
            dis_descripcion = response.response[dis]['descripcion']
            for (cerr in response.response[dis]['cerraduras']){

                if (response.response[dis]['cerraduras'][cerr]['estado']){
                    cerr_id = response.response[dis]['cerraduras'][cerr]['id']
                    cerr_numero = response.response[dis]['cerraduras'][cerr]['numero']
                    cerr_nombre = response.response[dis]['cerraduras'][cerr]['nombre']
                    estado = response.response[dis]['cerraduras'][cerr]['nombre']

                    if(response.response[dis]['cerraduras'][cerr]['fkentrada'] != "None"){
                        cerr_entrada = response.response[dis]['cerraduras'][cerr]['entrada'].nombre
                    }else{
                        cerr_entrada = ""
                    }

                    append_input_cerraduras(cerr_id)
                    $('#fkcerraduras' + cerr_id).val(cerr_id)
                    $('#nombre_dispositivo' + cerr_id).val(dis_descripcion)
                    $('#numero' + cerr_id).val(cerr_numero)
                    $('#nombre' + cerr_id).val(cerr_nombre)
                    $('#entrada' + cerr_id).val(cerr_entrada)
                    $('#b_' + cerr_id).prop('checked', false)
                }

            }


        }


    })


}

function append_input_tarjetas(id_in) {

        $('#tarjeta_div').append(
        '<div class="row">\
            <div class="col-sm-1" hidden>\
                <div class="input-group">\
                <input  id="id_tarjeta'+id_in+'" class="form-control configtarjetas txta-own"readonly>\
                </div>\
            </div>\
            <div class="col-sm-1">\
                <div class="form-line">\
                <input  id="fknropase'+id_in+'" class="form-control configtarjetas  txta-own"readonly>\
                </div>\
            </div>\
            <div class="col-sm-1">\
                <div class="form-line">\
                    <input id="numero_tarjeta'+id_in+'" data-id="'+id_in+'" class="form-control txta-own"readonly>\
                </div>\
            </div>\
            <div class="col-sm-2">\
                <div class="form-line">\
                <input  id="tarjeta'+id_in+'" class="form-control txta-own"readonly>\
                </div>\
            </div>\
            <div class="col-sm-2">\
                <div class="form-line">\
                <input  id="tipo_tarjeta'+id_in+'" class="form-control txta-own"readonly>\
                </div>\
            </div>\
            <div class="col-md-2 ">\
                <input id="t_'+id_in+'" type="checkbox" class="regular-checkbox big-checkbox  configtarjetas" data-id="1" >\
                <label for="t_'+id_in+'"></label>\
            </div>\
        </div>\
        </br>'
    )


    }

function obtener_tarjetas() {
        objeto = []
        objeto_inputs = $('.configtarjetas')

        for(i=0;i<objeto_inputs.length;i+=3){
            h0 = objeto_inputs[i].value
            h1 = objeto_inputs[i+1].value
            h2 = objeto_inputs[i+2].checked
            
            if(h2){
                objeto.push((function add_hours(h0,h1,h2) {


                if (h0 ==''){
                    return {
                    'fknropase': h1,
                    'estado': h2

                    }

                }else{
                    return {
                    'id':h0,
                    'fknropase': h1,
                    'estado': h2
                    }
                }

                })(
                        h0,
                        h1,
                        h2))
            }


        }
        return objeto
    }

function cargar_tarjetas(fkcondominio) {

    obj = JSON.stringify({
        'idcondominio': parseInt(JSON.parse(fkcondominio)),
        '_xsrf': getCookie("_xsrf")
    })

    ruta = "nropase_listar_condominio";
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

        for (tar in response.response ) {
            id = response.response[tar].id
            numero = response.response[tar].numero
            tarjeta = response.response[tar].tarjeta
            tipo_tarjeta = response.response[tar].tipo

            append_input_tarjetas(id)

            $('#id_tarjeta' + id).val('')
            $('#fknropase' + id).val(id)
            $('#numero_tarjeta' + id).val(numero)
            $('#tarjeta' + id).val(tarjeta)
            $('#tipo_tarjeta' + id).val(tipo_tarjeta)
            $('#t_' + id).prop('checked', false)


        }


    })


}


$('#new').click(function () {
    
    $('#nombre').val('')
    $('#fkcondominio').val('')
    $('#fkcondominio').selectpicker('refresh')
    $('#cerraduras_div').empty()
    $('#tarjeta_div').empty()

    verif_inputs('')


    $('#id_div').hide()
    $('#insert').show()
    $('#update').hide()
    validationInputSelects("form")
    $('#form').modal('show')
})


$('#insert').click(function () {
    notvalid = validationInputSelectsWithReturn("form");
    if (notvalid===false) {
        objeto = JSON.stringify({
            'nombre': $('#nombre').val(),
            'fkcondominio': $('#fkcondominio').val(),
            'configcerraduras': obtener_cerraduras(),
            'configtarjetas': obtener_tarjetas()
        })
        ajax_call('config_acceso_insert', {
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


function editar(elemento){
    obj = JSON.stringify({
        'id': parseInt(JSON.parse($(elemento).attr('data-json')))
    })
    ajax_call_get('config_acceso_update', {
        _xsrf: getCookie("_xsrf"),
        object: obj
    }, function (response) {
        var self = response;
        $('#id').val(self.id)
        $('#nombre').val(self.nombre)
        $('#fkcondominio').val(self.fkcondominio)
        $('#fkcondominio').selectpicker('refresh')
        $('#cerraduras_div').empty()
        $('#tarjeta_div').empty()

        for (cerr in self.configcerraduras){

            append_input_cerraduras(self.configcerraduras[cerr].id)
            $('#fkcerraduras' + self.configcerraduras[cerr].id).val(self.configcerraduras[cerr].fkcerraduras)
            $('#nombre_dispositivo' + self.configcerraduras[cerr].id).val(self.configcerraduras[cerr].cerraduras.dispositivo.descripcion)
            $('#numero' + self.configcerraduras[cerr].id).val(self.configcerraduras[cerr].cerraduras.numero)
            $('#nombre' + self.configcerraduras[cerr].id).val(self.configcerraduras[cerr].cerraduras.nombre)
            $('#entrada' + self.configcerraduras[cerr].id).val(self.configcerraduras[cerr].cerraduras.entrada.nombre)
            $('#b_' + self.configcerraduras[cerr].id).prop('checked', self.configcerraduras[cerr].estado)
            
        }
        
        cargar_tarjetas(self.fkcondominio)

        for (tar in self.configtarjetas){

            $('#id_tarjeta' + self.configtarjetas[tar].fknropase).val(self.configtarjetas[tar].id)
            $('#fknropase' + self.configtarjetas[tar].fknropase).val(self.configtarjetas[tar].fknropase)
            $('#t_' + self.configtarjetas[tar].fknropase).prop('checked', self.configtarjetas[tar].estado)


        }




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
            'nombre': $('#nombre').val(),
            'fkcondominio': $('#fkcondominio').val(),
            'configcerraduras': obtener_cerraduras(),
            'configtarjetas': obtener_tarjetas()
        })
        ajax_call('config_acceso_update', {
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
        cb_title = "¿Deshabilitar  Dispositivo?"

    } else {
        cb_title = "¿Habilitar  Dispositivo?"
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
        ajax_call('config_acceso_delete', {
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