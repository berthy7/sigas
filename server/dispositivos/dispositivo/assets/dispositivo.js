main_route = '/dispositivo'

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
        "order": [[ 0, "asc" ]],
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

$('#fktipodispositivo').selectpicker({
    size: 10,
    liveSearch: true,
    liveSearchPlaceholder: 'Buscar',
    title: 'Seleccione'
})

$('#fkentrada1').selectpicker({
    size: 10,
    liveSearch: true,
    liveSearchPlaceholder: 'Buscar',
    title: 'Seleccione'
})
$('#fkentrada2').selectpicker({
    size: 10,
    liveSearch: true,
    liveSearchPlaceholder: 'Buscar',
    title: 'Seleccione'
})
$('#fkentrada3').selectpicker({
    size: 10,
    liveSearch: true,
    liveSearchPlaceholder: 'Buscar',
    title: 'Seleccione'
})
$('#fkentrada4').selectpicker({
    size: 10,
    liveSearch: true,
    liveSearchPlaceholder: 'Buscar',
    title: 'Seleccione'
})

$('#fktipodispositivo').change(function () {
    ocultar_div($('#fktipodispositivo').val())

});

function ocultar_div(tipodispositivo) {

    if("1" == tipodispositivo){
        $('#div_cerradura').show()
        $('#div_cerradura_titulo').show()
        $('#div_cerradura1').show()
        $('#div_cerradura2').hide()
        $('#div_cerradura3').hide()
        $('#div_cerradura4').hide()

        $('#b_1').prop('checked', true)
        $('#b_2').prop('checked', false)
        $('#b_3').prop('checked', false)
        $('#b_4').prop('checked', false)

        $('#nombre2').val('')
        $('#nombre3').val('')
        $('#nombre4').val('')


        $('#fkentrada2').val('')
        $('#fkentrada2').selectpicker('refresh')

        $('#fkentrada3').val('')
        $('#fkentrada3').selectpicker('refresh')

        $('#fkentrada4').val('')
        $('#fkentrada4').selectpicker('refresh')


    }else if("2" == tipodispositivo){
        $('#div_cerradura').show()
        $('#div_cerradura_titulo').show()
        $('#div_cerradura1').show()
        $('#div_cerradura2').show()
        $('#div_cerradura3').hide()
        $('#div_cerradura4').hide()

        $('#b_1').prop('checked', true)
        $('#b_2').prop('checked', true)
        $('#b_3').prop('checked', false)
        $('#b_4').prop('checked', false)

        $('#nombre3').val('')
        $('#nombre4').val('')

        $('#fkentrada3').val('')
        $('#fkentrada3').selectpicker('refresh')

        $('#fkentrada4').val('')
        $('#fkentrada4').selectpicker('refresh')


    }else if("3" == tipodispositivo){
        $('#b_1').prop('checked', true)
        $('#b_2').prop('checked', true)
        $('#b_3').prop('checked', true)
        $('#b_4').prop('checked', true)

        $('#div_cerradura').show()
        $('#div_cerradura_titulo').show()
        $('#div_cerradura1').show()
        $('#div_cerradura2').show()
        $('#div_cerradura3').show()
        $('#div_cerradura4').show()


    }else if("4" == tipodispositivo){
        $('#div_cerradura').hide()
        $('#div_cerradura_titulo').hide()
        $('#div_cerradura1').hide()
        $('#div_cerradura2').hide()
        $('#div_cerradura3').hide()
        $('#div_cerradura4').hide()

        $('#b_1').prop('checked', false)
        $('#b_2').prop('checked', false)
        $('#b_3').prop('checked', false)
        $('#b_4').prop('checked', false)

        $('#nombre1').val('')
        $('#nombre2').val('')
        $('#nombre3').val('')
        $('#nombre4').val('')

        $('#fkentrada1').val('')
        $('#fkentrada1').selectpicker('refresh')

        $('#fkentrada2').val('')
        $('#fkentrada2').selectpicker('refresh')

        $('#fkentrada3').val('')
        $('#fkentrada3').selectpicker('refresh')

        $('#fkentrada4').val('')
        $('#fkentrada4').selectpicker('refresh')


    }

}

function obtener_cerraduras() {
        objeto = []
        objeto_inputs = $('.cerraduras')

        for(i=0;i<objeto_inputs.length;i+=6){
            h0 = objeto_inputs[i].value
            h1 = objeto_inputs[i+1].value
            h2 = objeto_inputs[i+2].value
            h3 = objeto_inputs[i+4].value
            h4 = objeto_inputs[i+5].checked

            if (h3 == ""){
                h3 = null;
            }

            objeto.push((function add_hours(h0,h1,h2,h3,h4) {

                if (h0 ==''){
                    return {
                    'numero': h1,
                    'nombre': h2,
                    'fkentrada': h3,
                    'estado': h4

                    }

                }else{
                    return {
                    'id':h0,
                    'numero': h1,
                    'nombre': h2,
                    'fkentrada': h3,
                    'estado': h4
                    }
                }

            })(
                    h0,
                    h1,
                    h2,
                    h3,
                    h4))
        }
        return objeto
    }

function cargar_interpretes() {
    obj = JSON.stringify({
        '_xsrf': getCookie("_xsrf")
    })
    ruta = "dispositivo_interpretes";
    $.ajax({
        method: "POST",
        url: ruta,
        data: {_xsrf: getCookie("_xsrf"), object: obj},
        async: true
    }).done(function (response) {
        response = JSON.parse(response)
        var self = response;

        $('#interpretes_div').empty()

        for(i in self.response){
            aux0 = self.response[i]['id']
            aux1 = self.response[i]['nombre']

            append_input_interpretes(aux0)
            $('#fkinterprete' + aux0).val(aux0)
            $('#nombre_interprete' + aux0).val(aux1)
            $('#b_interprete' + aux0).prop('checked', false)
        }

    })

}

//////////////////////////////////////////////////editar///////////////////////////////////////////////////////////////////////
    function append_input_interpretes(id_in) {

        $('#interpretes_div').append(
            '<div class="row" >\
                 <div class="col-sm-1" hidden>\
                    <div class="input-group">\
                    <input  id="id_interprete'+id_in+'" class="form-control interpretes readonly" hidden>\
                    </div>\
                 </div>\
                 <div class="col-sm-1">\
                    <div class="input-group">\
                    <input  id="fkinterprete'+id_in+'" value="'+id_in+'" class="form-control interpretes readonly">\
                    </div>\
                 </div>\
                 <div class="col-sm-5">\
                    <div class="input-group">\
                        <div><input id="nombre_interprete'+id_in+'" type="text" class="form-control" readonly></div>\
                    </div>\
                 </div>\
                 <div class="col-md-2">\
                    <input id="b_interprete'+id_in+'" type="checkbox" class="regular-checkbox big-checkbox interpretes" data-id="1" >\
                    <label for="b_interprete'+id_in+'"></label>\
                 </div>\
             </div>'
        )
    }

///////////////////////////////////////////////////////////////////////////////////////////////////////////////


function obtener_interpretes() {
        objeto = []
        objeto_inputs = $('.interpretes')

        for(i=0;i<objeto_inputs.length;i+=3){
            h0 = objeto_inputs[i].value
            h1 = objeto_inputs[i+1].value
            h2 = objeto_inputs[i+2].checked

                objeto.push((function add_hours(h0,h1,h2) {
                    if (h0 ==''){
                        return {
                        'fkinterprete': h1,
                        'estado': h2

                        }

                    }else{
                        return {
                        'id':h0,
                        'fkinterprete': h1,
                        'estado': h2
                        }
                    }
                })(h0,
                   h1,
                   h2))

        }
        return objeto
    }


$('#new').click(function () {
    cargar_interpretes()
    $('#ip').val('')
    $('#puerto').val('4370')
    $('#fktipodispositivo').val('')
    $('#fktipodispositivo').selectpicker('refresh')
    $('#modelo').val('')
    $('#descripcion').val('')
    $('#fkcondominio').val('')
    $('#fkcondominio').selectpicker('refresh')

    $('#id1').val('')
    $('#id2').val('')
    $('#id3').val('')
    $('#id4').val('')

    $('#numero1').val('1')
    $('#numero2').val('2')
    $('#numero3').val('3')
    $('#numero4').val('4')

    $('#nombre1').val('')
    $('#nombre2').val('')
    $('#nombre3').val('')
    $('#nombre4').val('')

    $('#fkentrada1').val('')
    $('#fkentrada1').selectpicker('refresh')
    $('#fkentrada2').val('')
    $('#fkentrada2').selectpicker('refresh')
    $('#fkentrada3').val('')
    $('#fkentrada3').selectpicker('refresh')
    $('#fkentrada4').val('')
    $('#fkentrada4').selectpicker('refresh')

    verif_inputs('')

    $('#div_cerradura').hide()
    $('#div_cerradura_titulo').hide()
    $('#div_cerradura1').hide()
    $('#div_cerradura2').hide()
    $('#div_cerradura3').hide()
    $('#div_cerradura4').hide()

    $('#div_abrir1').hide()
    $('#div_abrir2').hide()
    $('#div_abrir3').hide()
    $('#div_abrir4').hide()


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
            'ip': $('#ip').val(),
            'puerto': $('#puerto').val(),
            'fktipodispositivo': $('#fktipodispositivo').val(),
            'modelo': $('#modelo').val(),
            'descripcion': $('#descripcion').val(),
            'fkcondominio': $('#fkcondominio').val(),
            'cerraduras': obtener_cerraduras(),
            'interpretes': obtener_interpretes()
        })
        ajax_call('dispositivo_insert', {
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
    ajax_call_get('dispositivo_update', {
        _xsrf: getCookie("_xsrf"),
        object: obj
    }, function (response) {
        var self = response;
        //cargar_interpretes()
        $('#id').val(self.id)
        $('#ip').val(self.ip)
        $('#puerto').val(self.puerto)
        $('#fktipodispositivo').val(self.fktipodispositivo)
        $('#fktipodispositivo').selectpicker('refresh')
        $('#modelo').val(self.modelo)
        $('#descripcion').val(self.descripcion)
        $('#fkcondominio').val(self.fkcondominio)
        $('#fkcondominio').selectpicker('refresh')

        ocultar_div(self.fktipodispositivo)

        for(i in self.cerraduras){
            aux0 = self.cerraduras[i]['id']
            aux1 = self.cerraduras[i]['numero']
            aux2 = self.cerraduras[i]['nombre']
            aux3 = self.cerraduras[i]['fkentrada']
            
            $('#id' + aux1).val(aux0)
            $('#numero' + aux1).val(aux1)
            $('#nombre' + aux1).val(aux2)
            $('#fkentrada' + aux1).val(aux3)
            $('#fkentrada' + aux1).selectpicker('refresh')
        }
        
        $('#interpretes_div').empty()
        for(i in self.interpretes){
            aux0 = self.interpretes[i]['id']
            aux1 = self.interpretes[i]['fkinterprete']
            aux2 = self.interpretes[i]['interprete'].nombre
            aux3 = self.interpretes[i]['estado']

            append_input_interpretes(aux0)
            $('#id_interprete' + aux0).val(aux0)
            $('#fkinterprete' + aux0).val(aux1)
            $('#nombre_interprete' + aux0).val(aux2)
            $('#b_interprete' + aux0).prop('checked', aux3)
        }

        validationInputSelects("form")
        verif_inputs('')

        $('#div_abrir1').show()
        $('#div_abrir2').show()
        $('#div_abrir3').show()
        $('#div_abrir4').show()

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
            'ip': $('#ip').val(),
            'puerto': $('#puerto').val(),
            'fktipodispositivo': $('#fktipodispositivo').val(),
            'modelo': $('#modelo').val(),
            'descripcion': $('#descripcion').val(),
            'fkcondominio': $('#fkcondominio').val(),
            'cerraduras': obtener_cerraduras(),
            'interpretes': obtener_interpretes()
        })
        ajax_call('dispositivo_update', {
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
        ajax_call('dispositivo_delete', {
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


$('#abrir1').click(function () {
    objeto = JSON.stringify({
        'id': parseInt($('#id').val()),
        'cerradura': '1'

    })
    ajax_call('dispositivo_abrir_cerradura', {
        object: objeto,
        _xsrf: getCookie("_xsrf")
    }, null, function () {

    })

})

$('#abrir2').click(function () {

    objeto = JSON.stringify({
        'id': parseInt($('#id').val()),
        'cerradura': '2'

    })
    ajax_call('dispositivo_abrir_cerradura', {
        object: objeto,
        _xsrf: getCookie("_xsrf")
    }, null, function () {

    })

})

$('#abrir3').click(function () {

    objeto = JSON.stringify({
        'id': parseInt($('#id').val()),
        'cerradura': '3'

    })
    ajax_call('dispositivo_abrir_cerradura', {
        object: objeto,
        _xsrf: getCookie("_xsrf")
    }, null, function () {

    })

})

$('#abrir4').click(function () {

    objeto = JSON.stringify({
        'id': parseInt($('#id').val()),
        'cerradura': '4'

    })
    ajax_call('dispositivo_abrir_cerradura', {
        object: objeto,
        _xsrf: getCookie("_xsrf")
    }, null, function () {

    })

})
function configuracion(elemento){
    obj = JSON.stringify({
        'id': parseInt(JSON.parse($(elemento).attr('data-json')))
    })
    ajax_call('dispositivo_configuracion', {
        _xsrf: getCookie("_xsrf"),
        object: obj
    }, null, function () {

    })
}

validationKeyup("form")
validationSelectChange("form")