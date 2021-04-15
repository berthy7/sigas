main_route = '/evento'

var multiacceso = false;
var paselibre = false;
var multiple = false;

$(document).ready(function () {
   
});

id_gv = 0

$(".hr").inputmask("h:s",{ "placeholder": "__/__" });

$(document).ajaxStart(function () { });

$(document).ajaxStop(function () {
    $.Toast.hideToast();
});

var fechahoy = new Date();
var hoy = fechahoy.getDate()+"/"+(fechahoy.getMonth()+1) +"/"+fechahoy.getFullYear()
console.log(hoy)
document.getElementById("ffechai").value=hoy
document.getElementById("ffechaf").value=hoy

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

$('#fkresidente').selectpicker({
    size: 10,
    liveSearch: true,
    liveSearchPlaceholder: 'Buscar residente',
    title: 'Seleccione residente'
})

$('#fktipoevento').selectpicker({
    size: 10,
    liveSearch: true,
    liveSearchPlaceholder: 'Buscar evento',
    title: 'Seleccione evento'
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

$('#personas').selectpicker({
    size: 10,
    liveSearch: true,
    liveSearchPlaceholder: 'Buscar',
    title: 'Seleccione'
})

$('#switch_multiacceso').change(function() {
   multiacceso = $(this).prop('checked')

})

$('#switch_paselibre').change(function() {
   paselibre = $(this).prop('checked')

})

$('#switch_multiple').change(function() {
   multiple = $(this).prop('checked')

})

function actualizar_tabla(response){

    var data = [];
    var id;
    var fechai;
    var fechaf;
    var destino;
    var estado;
    var editar;


    for (var i = 0; i < Object.keys(response.response).length; i++) {
            id = response['response'][i].id

            if(response['response'][i].fechai){
                fechai= response['response'][i].fechai
            }else{
                fechai = '-----'
            }

            if(response['response'][i].fechaf){
                fechaf = response['response'][i].fechaf
            }else{
                fechaf = '-----'

            }
        


            if(response['response'][i].fkdomicilio != "None"){
                destino = response['response'][i].domicilio.ubicacion + " " + response['response'][i].domicilio.numero
            }else if(response['response'][i].fkareasocial != "None"){
                destino = response['response'][i].areasocial.nombre
            }else{
                destino = '-----'
            }

            if(response['response'][i]['estado']){
                estado = "<input id='" + id + "' onClick='event.preventDefault();estado(this)' data-id='" + id + "' type='checkbox' class='chk-col-indigo' checked /><label for='" + id + "'></label>"
            }else{
               estado = "<input id='" + id + "' onClick='event.preventDefault();estado(this)' data-id='" + id + "' type='checkbox' class='chk-col-indigo' /><label for='" + id + "'></label>"
            }

            editar ="<button id='edit' onClick='editar(this)' data-json="+id+" type='button' class='btn bg-indigo white-own waves-effect waves-light' title='Editar'><i class='material-icons'>create</i></button>"
        

            data.push( [
                id,
                response['response'][i].tipoevento.nombre,
                response['response'][i].residente.fullname,
                destino,
                fechai,
                fechaf,
                estado,
                editar
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
               exportOptions : { columns : [0, 1, 2, 3, 4, 5 ,6 ,7]},
                sheetName: 'Reporte Eventos',
               title: 'Eventos'  },
            {  extend : 'pdfHtml5',
                orientation: 'landscape',
               customize: function(doc) {
                    doc.styles.tableBodyEven.alignment = 'center';
                    doc.styles.tableBodyOdd.alignment = 'center';
               },
               exportOptions : {
                    columns : [0, 1, 2, 3, 4, 5 ,6 ,7]
                },
               title: 'Eventos'
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
        "order": [[ 0, "desc" ]],
        language : {
            'url': '/resources/js/spanish.json',
        },
        "pageLength": 50
    });
}

$('#fkdomicilio').change(function () {

    $('#fkareasocial').val('')
    $('#fkareasocial').selectpicker('refresh')

});

$('#fkareasocial').change(function () {

        $('#fkdomicilio').val('')
        $('#fkdomicilio').selectpicker('refresh')

});


    $('#new_integrante').click(function () {
        append_input_integrante('')
    })

    function get_invitado() {
        invitado = []
        invitado_inputs = $('.invitado')
        console.log(invitado_inputs)

        for (i = 0; i < invitado_inputs.length; i += 9) {
            h0 = invitado_inputs[i].value
            h1 = invitado_inputs[i + 1].value
            h2 = invitado_inputs[i + 2].value
            h3 = invitado_inputs[i + 3].value
            h4 = invitado_inputs[i + 4].value
            h5 = invitado_inputs[i + 5].value
            h6 = invitado_inputs[i + 6].value
            h7 = invitado_inputs[i + 8].value


            invitado.push((function add_invitado(h0, h1, h2, h3,h4,h5,h6,h7) {

                if (h0 ==''){
                    return {
                        'fkinvitado': h1,
                        'nombre': h2,
                        'apellidop': h3,
                        'apellidom': h4,
                        'ci': h5,
                        'expendido': h6,
                        'fktipopase': h7

                    }

                }else{
                    return {
                    'id':h0,
                    'fkinvitado': h1,
                    'nombre': h2,
                    'apellidop': h3,
                    'apellidom': h4,
                    'ci': h5,
                    'expendido': h6,
                    'fktipopase': h7
                    }
                }


            })(
                h0,
                h1,
                h2,
                h3,
                h4,
                h5,
                h6,
                h7))
        }
        return invitado
    }

    $('#fkresidente').change(function () {
        cargar_domicilio(parseInt(JSON.parse($('#fkresidente').val())))

    });

    function cargar_domicilio(idresidente) {
        obj = JSON.stringify({
            'id': idresidente,
            '_xsrf': getCookie("_xsrf")
        })
        ruta = "residente_obtener_domicilios";
        var iddomicilio;
        $.ajax({
            method: "POST",
            url: ruta,
            data: {_xsrf: getCookie("_xsrf"), object: obj},
            async: false
        }).done(function (response) {
            response = JSON.parse(response)
            console.log(response)
            iddomicilio = response['response']['id']
            $('#fkdomicilio').html('');

            var select = document.getElementById("fkdomicilio")
            var option = document.createElement("OPTION");
            option.innerHTML = response['response']['ubicacion'] + " "+response['response']['numero'];
            option.value = response['response']['id'];
            select.appendChild(option);

            $('#fkdomicilio').selectpicker('refresh');
        });

        $('#fkdomicilio').val(iddomicilio)
        $('#fkdomicilio').selectpicker('refresh')

    }

    $('#personas').change(function () {
        obj = JSON.stringify({
            'id': parseInt(JSON.parse($('#personas').val())),
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
            append_input_integrante('')

            var id_nombre = ''
            $("input.nombre").each(function() {
                id_nombre  = $(this).prop('id');
            });

            var id_apellidop = ''
            $("input.apellidop").each(function() {
                id_apellidop  = $(this).prop('id');
            });

            var id_apellidom = ''
            $("input.apellidom").each(function() {
                id_apellidom  = $(this).prop('id');
            });


            var id_ci = ''
            $("input.ci").each(function() {
                id_ci  = $(this).prop('id');
            });

            var id_fkinvitado = ''
            $("input.fkinvitado").each(function() {
                id_fkinvitado = $(this).prop('id');
            });

            $('#' + id_fkinvitado ).val(response.response.id)
            $('#' + id_fkinvitado ).parent().addClass('focused')
            $('#' + id_nombre ).val(response.response.nombre)
            $('#' + id_nombre ).parent().addClass('focused')
            $('#' + id_apellidop ).val(response.response.apellidop)
            $('#' + id_apellidop ).parent().addClass('focused')
            $('#' + id_apellidom ).val(response.response.apellidom)
            $('#' + id_apellidom ).parent().addClass('focused')
            $('#' + id_ci ).val(response.response.ci)
            $('#' + id_ci ).parent().addClass('focused')


        })

        $('#personas').val('')
        $('#personas').selectpicker('refresh')

    });


$('#new').click(function () {
    $('#codigo').val('')
    $('#fkresidente').val('')
    $('#fkresidente').selectpicker('refresh')
    $('#fktipoevento').val(1)
    $('#fktipoevento').selectpicker('refresh')
    $('#descripcion').val('')
    $('#fkdomicilio').val('')
    $('#fkdomicilio').selectpicker('refresh')
    $('#fkareasocial').val('')
    $('#fkareasocial').selectpicker('refresh')
    $('#fechai').val('')
    $('#horai').val('')
    $('#fechaf').val('')
    $('#horaf').val('')
    document.getElementById('switch_multiacceso').checked=false
    document.getElementById('switch_paselibre').checked=false
    document.getElementById('switch_multiple').checked=false
    $('#integrante_div').empty()

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
            'codigo': $('#codigo').val(),
            'descripcion': $('#descripcion').val(),
            'fkresidente': $('#fkresidente').val(),
            'fktipoevento': $('#fktipoevento').val(),
            'fkdomicilio': $('#fkdomicilio').val(),
            'fkareasocial': $('#fkareasocial').val(),
            'fechai': $('#fechai').val(),
            'horai': $('#horai').val(),
            'fechaf': $('#fechaf').val(),
            'horaf': $('#horaf').val(),
            'multiacceso':multiacceso,
            'paselibre': paselibre,
            'multiple': multiple,
            'invitaciones': get_invitado()
        })
        ajax_call('evento_insert', {
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
    ajax_call_get('evento_update', {
        _xsrf: getCookie("_xsrf"),
        object: obj
    }, function (response) {
        var self = response;
            $('#id').val(self.id)
            $('#codigo').val(self.codigo)
            $('#fkresidente').val(self.fkresidente)
            $('#fkresidente').selectpicker('refresh')
            $('#fktipoevento').val(self.fktipoevento)
            $('#fktipoevento').selectpicker('refresh')
            $('#descripcion').val(self.descripcion)
            cargar_domicilio(self.fkresidente)
            $('#fkdomicilio').val(self.fkdomicilio)
            $('#fkdomicilio').selectpicker('refresh')
            $('#fkareasocial').val(self.fkareasocial)
            $('#fkareasocial').selectpicker('refresh')
            $('#fechai').val(self.fechai)
            $('#horai').val(self.horai)
            $('#fechaf').val(self.fechaf)
            $('#horaf').val(self.horaf)
            document.getElementById('switch_multiacceso').checked=self.multiacceso
            document.getElementById('switch_paselibre').checked=self.paselibre
            document.getElementById('switch_multiple').checked=self.multiple


            $('#integrante_div').empty()

            for (invi in self.invitaciones) {

                append_input_integrante(self.invitaciones[invi].id)
                $('#id' + self.invitaciones[invi].id).val(self.invitaciones[invi].id)
                $('#fkinvitado' + self.invitaciones[invi].id).val(self.invitaciones[invi].fkinvitado)
                $('#nombre' + self.invitaciones[invi].id).val(self.invitaciones[invi].nombre)
                $('#apellidop' + self.invitaciones[invi].id).val(self.invitaciones[invi].apellidop)
                $('#apellidom' + self.invitaciones[invi].id).val(self.invitaciones[invi].apellidom)
                $('#ci' + self.invitaciones[invi].id).val(self.invitaciones[invi].ci)
                $('#codigo' + self.invitaciones[invi].id).val(self.invitaciones[invi].codigoautorizacion)
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
            'codigo': $('#codigo').val(),
            'fkresidente': $('#fkresidente').val(),
            'fktipoevento': $('#fktipoevento').val(),
            'descripcion': $('#descripcion').val(),
            'fkdomicilio': $('#fkdomicilio').val(),
            'fkareasocial': $('#fkareasocial').val(),
            'fechai': $('#fechai').val(),
            'horai': $('#horai').val(),
            'fechaf': $('#fechaf').val(),
            'horaf': $('#horaf').val(),
            'multiacceso':multiacceso,
            'paselibre': paselibre,
            'invitaciones': get_invitado()
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
reload_form()


function eliminar(elemento){
    cb_delete = elemento
    b = $(elemento).prop('checked')
    if (!b) {
        cb_title = "¿Deshabilitar Evento?"

    } else {
        cb_title = "¿Habilitar Evento?"
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
        ajax_call('evento_delete', {
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

$('#filtrar').click(function () {
    $("#rgm-loader").show();
    //document.getElementById("filtrar").disabled = true
    obj = JSON.stringify({
        'fechainicio': $('#ffechai').val(),
        'fechafin': $('#ffechaf').val(),
        '_xsrf': getCookie("_xsrf")
    })
    ruta = "evento_filtrar";
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

var inputHoraInicio = document.getElementById('horai') ,
    inputHoraFin = document.getElementById('horaf')
inputHoraInicio.onfocusout = function (){ this.parentElement.classList.add('focused')}
inputHoraFin.onfocusout = function (){ this.parentElement.classList.add('focused')}