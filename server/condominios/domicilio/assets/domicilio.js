main_route = '/domicilio'

$(document).ready(function () {
    document.getElementById("primero").click();
    
    if ($('#sigas').val()  == "True"){
        $('#div_filtro').show()


    }else{
        $('#div_filtro').hide()

    }
});

$(document).ajaxStart(function () { });

$(document).ajaxStop(function () {
    $.Toast.hideToast();
});

function cargar_tabla(response){

    var data =[]
    var id
    var interno
    for (var i = 0; i < Object.keys(response.response).length; i++) {
        id = response['response'][i]['id']
        if(response['response'][i]['interno'] != "None"){
            interno = response['response'][i]['interno']
        }else{
            interno = ""
        }
        data.push( [
            id,
            response['response'][i]['codigo'],
            response['response'][i]['ubicacion'],
            response['response'][i]['numero'],
            interno,
            response['response'][i]['condominio']['nombre'],
            "<button id='edit' onClick='editar(this)' data-json='" + response['response'][i]['id'] + "' type='button' class='btn bg-indigo waves-effect waves-light edit' title='Editar'><i class='material-icons'>create</i></button>"
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
        "order": [[0, "asc" ]],
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

$('#fkcondominio_departamento').selectpicker({
    size: 10,
    liveSearch: true,
    liveSearchPlaceholder: 'Buscar condominio',
    title: 'Seleccione un Condominio'
})



    $('#primero').click(function () {
        obj = JSON.stringify({
            '_xsrf': getCookie("_xsrf")
        })
        ruta = "domicilio_obtener_casas";
        $.ajax({
            method: "POST",
            url: ruta,
            data: {_xsrf: getCookie("_xsrf"), object: obj},
            async: true
        }).done(function (response) {
            response = JSON.parse(response)

            cargar_tabla(response)
        })
        $('#new').show()
        $('#new_departamento').hide()
        $('#idomicilio').val('Casa')
    })

    $('#segundo').click(function () {
        obj = JSON.stringify({
            '_xsrf': getCookie("_xsrf")
        })
        ruta = "domicilio_obtener_departamentos";
        $.ajax({
            method: "POST",
            url: ruta,
            data: {_xsrf: getCookie("_xsrf"), object: obj},
            async: true
        }).done(function (response) {
            response = JSON.parse(response)

            cargar_tabla(response)
        })
        $('#new').hide()
        $('#new_departamento').show()
        $('#idomicilio').val('Departamento')

    })

$('#fcondominio').change(function () {
    obj = JSON.stringify({
        'idcondominio': $('#fcondominio').val(),
        'domicilio': $('#idomicilio').val(),
        '_xsrf': getCookie("_xsrf")
    })
    ruta = "domicilio_filtrar";
    $.ajax({
        method: "POST",
        url: ruta,
        data: {_xsrf: getCookie("_xsrf"), object: obj},
        async: true
    }).done(function (response) {
        response = JSON.parse(response)

        cargar_tabla(response)
    })
});

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

    ruta = "domicilio_importar";
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
                query_render('/residente');
            });
        }
    })
    $('#form').modal('hide')
})

$('#new').click(function () {
    $('#codigo').val('')
    $('#numero').val('')
    $('#ubicacion').val('')
    $('#interno').val('')

    $('#fkcondominio').val($('#idcondominio').val())
    $('#fkcondominio').selectpicker('refresh')

    if ($('#sigas').val()  == "True"){
        console.log("rol sigas")
        $('#fkcondominio').prop('disabled', false);


    }else{
         console.log("rol condominio")
        $('#fkcondominio').prop('disabled', true);

    }

    $('#tipo').val('Casa')
    verif_inputs('')
    $('#id_div').hide()
    $('#insert').show()
    $('#update').hide()
    $('#casa_tittle').show()
    $('#departamento_tittle').hide()
    validationInputSelects("form")
    $('#form').modal('show')
})

$('#new_departamento').click(function () {
    $('#codigo').val('')
    $('#numero').val('')
    $('#ubicacion').val('')
    $('#interno').val('')

    $('#fkcondominio').val($('#idcondominio').val())
    $('#fkcondominio').selectpicker('refresh')

    if ($('#sigas').val()  == "True"){
        console.log("rol sigas")
        $('#fkcondominio').prop('disabled', false);


    }else{
         console.log("rol condominio")
        $('#fkcondominio').prop('disabled', true);

    }

    $('#tipo').val('Departamento')
    verif_inputs('')
    $('#id_div').hide()
    $('#insert').show()
    $('#update').hide()
    $('#casa_tittle').hide()
    $('#departamento_tittle').show()
    validationInputSelects("form")
    $('#form').modal('show')
})


$('#insert').click(function () {
    notvalid = validationInputSelectsWithReturn("form");
    if (notvalid===false) {
        objeto = JSON.stringify({
            'codigo': $('#codigo').val(),
            'numero': $('#numero').val(),
            'ubicacion': $('#ubicacion').val(),
            'tipo': $('#tipo').val(),
            'interno': $('#interno').val(),
            'fkcondominio': $('#fkcondominio').val()
        })
        ajax_call('domicilio_insert', {
            object: objeto,
            _xsrf: getCookie("_xsrf")
        }, null, function (response) {
            response = JSON.parse(response)

            cargar_tabla(response)

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
    ajax_call_get('domicilio_update', {
        _xsrf: getCookie("_xsrf"),
        object: obj
    }, function (response) {
        var self = response;
         $('#id').val(self.id)
        $('#codigo').val(self.codigo)
        $('#ubicacion').val(self.ubicacion)
        $('#numero').val(self.numero)
        $('#interno').val(self.interno)
        $('#fkcondominio').val(self.fkcondominio)
        $('#fkcondominio').selectpicker('refresh')
        $('#tipo').val(self.tipo)

        if (self.tipo== "Casa"){
            $('#casa_tittle').show()
            $('#departamento_tittle').hide()

        }else{
            $('#casa_tittle').hide()
            $('#departamento_tittle').show()
        }

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
            'codigo': $('#codigo').val(),
            'numero': $('#numero').val(),
            'ubicacion': $('#ubicacion').val(),
            'interno': $('#interno').val(),
            'tipo': $('#tipo').val(),
            'fkcondominio': $('#fkcondominio').val()
        })
        ajax_call('domicilio_update', {
            object: objeto,
            _xsrf: getCookie("_xsrf")
        }, null, function (response) {
            response = JSON.parse(response)
            cargar_tabla(response)


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

    
$('.delete').click(function () {
    id = parseInt(JSON.parse($(this).attr('data-json')))
    enabled = false
    swal({
        title: "¿Desea eliminar el domicilio?",
        type: "warning",
        showCancelButton: true,
        confirmButtonColor: "#006227",
        cancelButtonColor: "#F44336",
        confirmButtonText: "Aceptar",
        cancelButtonText: "Cancelar"
    }).then(function () {
        ajax_call('domicilio_delete', {
            id: id,
            enabled: enabled,
            _xsrf: getCookie("_xsrf")
        }, null, function () {
            setTimeout(function () {
                window.location = main_route
            }, 2000);
        })
    })
})

validationKeyup("form")
validationSelectChange("form")
