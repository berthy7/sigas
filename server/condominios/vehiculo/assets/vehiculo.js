main_route = '/vehiculo'

$(document).ready(function () {

});

$(document).ajaxStart(function () { });

$(document).ajaxStop(function () {
    $.Toast.hideToast();
});

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


    $('#fkmarca').change(function () {
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

$('#new').click(function () {
    $('#placa').val('')
    $('#color').val('')
    $('#tipo').val('')
    $('#tipo').selectpicker('refresh')
    $('#fkmarca').val('')
    $('#fkmarca').selectpicker('refresh')
    $('#fkmodelo').val('')
    $('#fkmodelo').selectpicker('refresh')

    verif_inputs('')
    validationInputSelects("form")
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
            'placa': $('#placa').val(),
            'color': $('#color').val(),
            'tipo': $('#tipo').val(),
            'fkmarca': $('#fkmarca').val(),
            'fkmodelo': $('#fkmodelo').val()
        })
        ajax_call('vehiculo_insert', {
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
    ajax_call_get('vehiculo_update', {
        _xsrf: getCookie("_xsrf"),
        object: obj
    }, function (response) {
        var self = response;
        $('#id').val(self.id)
        $('#placa').val(self.placa)
        $('#color').val(self.color)
        $('#tipo').val(self.tipo)
        $('#tipo').selectpicker('refresh')
        $('#fkmarca').val(self.fkmarca)
        $('#fkmarca').selectpicker('refresh')
        $('#fkmodelo').val(self.fkmodelo)
        $('#fkmodelo').selectpicker('refresh')

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
            'placa': $('#placa').val(),
            'color': $('#color').val(),
            'tipo': $('#tipo').val(),
            'fkmarca': $('#fkmarca').val(),
            'fkmodelo': $('#fkmodelo').val()
        })
        ajax_call('vehiculo_update', {
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
        cb_title = "¿Deshabilitar Vehiculo?"

    } else {
        cb_title = "¿Habilitar Vehiculo?"
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
        ajax_call('vehiculo_delete', {
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