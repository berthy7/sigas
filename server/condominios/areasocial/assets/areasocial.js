main_route = '/areasocial'

$(document).ready(function () {

    if ($('#sigas').val() == "True"){
        console.log("rol sigas")
        $('#div_filtro').show()


    }else{
         console.log("rol condominio")
        $('#div_filtro').hide()

    }

});

$(document).ajaxStart(function () { });

$(document).ajaxStop(function () {
    $.Toast.hideToast();
});

$('#fkcondominio').selectpicker({
    size: 10,
    liveSearch: true,
    liveSearchPlaceholder: 'Buscar condominio',
    title: 'Seleccione un Condominio'
})

$('#fcondominio').selectpicker({
    size: 10,
    liveSearch: true,
    liveSearchPlaceholder: 'Buscar condominio',
    title: 'Seleccione un Condominio'
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
    $('#nombre').val('')
    $('#ubicacion').val('')

    $('#fkcondominio').val($('#idcondominio').val())
    $('#fkcondominio').selectpicker('refresh')

    if ($('#sigas').val()  == "True"){
        console.log("rol sigas")
        $('#fkcondominio').prop('disabled', false);


    }else{
         console.log("rol condominio")
        $('#fkcondominio').prop('disabled', true);

    }


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
            'ubicacion': $('#ubicacion').val(),
            'fkcondominio': $('#fkcondominio').val()
        })
        ajax_call('areasocial_insert', {
            object: objeto,
            _xsrf: getCookie("_xsrf")
        }, null, function (response) {
            response = JSON.parse(response)

            var data = [];
            var id
            for (var i = 0; i < Object.keys(response.response).length; i++) {
                id = response['response'][i]['id']
                data.push( [
                    response['response'][i]['id'],
                    response['response'][i]['nombre'],
                    response['response'][i]['ubicacion'],
                    response['response'][i]['condominio']['nombre'],
                    "<input id='" + id + "' onClick='event.preventDefault();eliminar(this)' data-id='" + id + "' type='checkbox' class='chk-col-indigo 'checked /><label for='" + id + "'></label>",
                    "<button id='edit' onClick='editar(this)' data-json='" + id + "' type='button' class='btn bg-indigo waves-effect waves-light edit' title='Editar'><i class='material-icons'>create</i></button>"
                ]);
            }

            cargar_tabla(data)


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
    ajax_call_get('areasocial_update', {
        _xsrf: getCookie("_xsrf"),
        object: obj
    }, function (response) {
        var self = response;
        $('#id').val(self.id)
        $('#nombre').val(self.nombre)
        $('#ubicacion').val(self.ubicacion)
        $('#fkcondominio').val(self.fkcondominio)
        $('#fkcondominio').selectpicker('refresh')
        
        if ($('#sigas').val()  == "True"){
        console.log("rol sigas")
        $('#fkcondominio').prop('disabled', false);


    }else{
         console.log("rol condominio")
        $('#fkcondominio').prop('disabled', true);

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
            'ubicacion': $('#ubicacion').val(),
            'fkcondominio': $('#fkcondominio').val()
        })
        ajax_call('areasocial_update', {
            object: objeto,
            _xsrf: getCookie("_xsrf")
        }, null, function (response) {
            response = JSON.parse(response)

            var data = [];
            var id
            for (var i = 0; i < Object.keys(response.response).length; i++) {
                id = response['response'][i]['id']
                data.push( [
                    response['response'][i]['id'],
                    response['response'][i]['nombre'],
                    response['response'][i]['ubicacion'],
                    response['response'][i]['condominio']['nombre'],
                    "<input id='" + id + "' onClick='event.preventDefault();eliminar(this)' data-id='" + id + "' type='checkbox' class='chk-col-indigo delete' 'checked' /><label for='" + id + "'></label>",
                    "<button id='edit' onClick='editar(this)' data-json='" + id + "' type='button' class='btn bg-indigo waves-effect waves-light edit' title='Editar'><i class='material-icons'>create</i></button>"
                ]);
            }

            cargar_tabla(data)


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
        cb_title = "¿Deshabilitar Area Social?"

    } else {
        cb_title = "¿Habilitar Area Social?"
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
        ajax_call('areasocial_delete', {
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

$('#fcondominio').change(function () {
    obj = JSON.stringify({
        'idcondominio': $('#fcondominio').val(),
        '_xsrf': getCookie("_xsrf")
    })
    ruta = "areasocial_filtrar";
    $.ajax({
        method: "POST",
        url: ruta,
        data: {_xsrf: getCookie("_xsrf"), object: obj},
        async: true
    }).done(function (response) {
        response = JSON.parse(response)

        var data = [];
        var id
        for (var i = 0; i < Object.keys(response.response).length; i++) {
            id = response['response'][i]['id']
            data.push( [
                response['response'][i]['id'],
                response['response'][i]['nombre'],
                response['response'][i]['ubicacion'],
                response['response'][i]['condominio']['nombre'],
                "<input id='" + response['response'][i]['id'] + "' onClick='event.preventDefault();eliminar(this)' data-id='" + response['response'][i]['id'] + "' type='checkbox' class='chk-col-indigo delete' checked /><label for='" + response['response'][i]['id'] + "'></label>",
                "<button id='edit' onClick='editar(this)' data-json='" + response['response'][i]['id'] + "' type='button' class='btn bg-indigo waves-effect waves-light edit' title='Editar'><i class='material-icons'>create</i></button>"
            ]);
        }

        cargar_tabla(data)
    })
});

validationKeyup("form")
validationSelectChange("form")
