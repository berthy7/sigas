main_route = '/nropase'

$(document).ready(function () {
    
    if ($('#sigas').val()  == "True"){
        console.log("rol sigas")
        $('#div_filtro').show()


    }else{
         console.log("rol condominio")
        $('#div_filtro').hide()

    }
   
});

id_gv = 0

$(document).ajaxStart(function () { });

$(document).ajaxStop(function () {
    $.Toast.hideToast();
});

$('#condominios').selectpicker({
    size: 10,
    liveSearch: true,
    liveSearchPlaceholder: 'Buscar condominio',
    title: 'Seleccione condominio'
})

$('#fkcondominio').selectpicker({
    size: 10,
    liveSearch: true,
    liveSearchPlaceholder: 'Buscar condominio',
    title: 'Seleccione un Condominio'
})

$('#tipo').selectpicker({
    size: 10,
    liveSearch: true,
    liveSearchPlaceholder: 'Buscar',
    title: 'Seleccione'
})

    $('#condominios').change(function () {
        obj = JSON.stringify({
            'id': parseInt(JSON.parse($('#condominios').val())),
            '_xsrf': getCookie("_xsrf")
        })

        ruta = "condominio_obtener";

        $.ajax({
            method: "POST",
            url: ruta,
            data: {_xsrf: getCookie("_xsrf"), object: obj},
            async: false
        }).done(function (response) {
            response = JSON.parse(response)
            console.log(response)
            append_input_condominio('')
            
            var fkcondominio = ''
            $("input.fkcondominio").each(function() {
                fkcondominio = $(this).prop('id');
            });

            var nombre = ''
            $("input.nombre").each(function() {
                nombre = $(this).prop('id');
            });
            

            $('#' + fkcondominio).val(response.response.id)
            $('#' + fkcondominio).parent().addClass('focused')
            $('#' + nombre).val(response.response.nombre)
            $('#' + nombre).parent().addClass('focused')
            
        })

        $('#condominios').val('')
        $('#condominios').selectpicker('refresh')

    });

    function append_input_condominio(id_in) {
        if(id_in === ''){
            id_gv++;
            id_in = id_gv;
        }

        $('#condominio_div').append(
        '<div class="row">\
            <div class="col-sm-1 hidden">\
                <div class="input-group">\
                <input  id="idv'+id_in+'" class="form-control idcondominio condominio readonly txta-own">\
                </div>\
            </div>\
            <div class="col-sm-1 hidden">\
                <div class="input-group">\
                <input  id="fkcondominio'+id_in+'" class="form-control fkcondominio condominio txta-own">\
                </div>\
            </div>\
            <div class="col-sm-6">\
                <div class="form-line">\
                    <input id="nombre'+id_in+'" data-id="'+id_in+'" class="form-control nombre  txta-own"readonly>\
                </div>\
            </div>\
            <div class="col-sm-2">\
                <button type="button" class="btn bg-red waves-effect white-own clear_condominio" title="Eliminar">\
                    <i class="material-icons">clear</i>\
                </button>\
            </div>\
        </div>'
    )

        $('.clear_condominio').last().click(function () {
            $(this).parent().parent().remove()
        })

        $('.nombre').focus(function () {
            $(this).parent().addClass('focused');
            current_input = $(this).prop('id');
        })



    }

    function get_condominio() {
        objeto = []
        objeto_inputs = $('.condominio')

        for (i = 0; i < objeto_inputs.length; i += 2) {
            h0 = objeto_inputs[i].value
            h1 = objeto_inputs[i + 1].value
            
            if (h1 !=""){
                
                objeto.push((function add_(h0, h1) {

                if (h0 ==''){
                    return {
                        'fkcondominio': h1

                    }

                }else{
                    return {
                    'id':h0,
                    'fkcondominio': h1
                    }
                }
                    
                })(
                    h0,
                    h1))
                
                
            }

        }
        
        return objeto
    }

$('#agregar_condominio').click(function () {

    $('#div_agregar_condominio').hide()
    $('#div_buscar_condominio').show()
    $('#div_cancelar_condominio').show()

})

$('#cancelar_condominio').click(function () {

    $('#div_buscar_condominio').hide()
    $('#div_cancelar_condominio').hide()
    $('#div_agregar_condominio').show()

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
        "order": [[ 0, "asc" ]],
        language : {
            'url': '/resources/js/spanish.json',
        },
        "pageLength": 50
    });
}
   
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

    ruta = "nropase_importar";
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
    $('#numero').val('')
    $('#tarjeta').val('')
    $('#tipo').val('')
    $('#tipo').selectpicker('refresh')
    
    $('#condominio_div').empty()

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
            'numero': $('#numero').val(),
            'tarjeta': $('#tarjeta').val(),
            'tipo': $('#tipo').val(),
            'condominios': get_condominio()
        })
        ajax_call('nropase_insert', {
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
    ajax_call_get('nropase_update', {
        _xsrf: getCookie("_xsrf"),
        object: obj
    }, function (response) {
        var self = response;
        $('#id').val(self.id)
        $('#numero').val(self.numero)
        $('#tarjeta').val(self.tarjeta)
        $('#tipo').val(self.tipo)
        $('#tipo').selectpicker('refresh')

        $('#condominio_div').empty()

            for (invi in self.condominios) {
                id = self.condominios[invi]['id']
                fkcondominio= self.condominios[invi]['fkcondominio']
                nombre = self.condominios[invi]['nombre']

                append_input_condominio(id)
                $('#idv' + id).val(id)
                $('#fkcondominio' + id).val(fkcondominio)
                $('#nombre' + id).val(nombre)
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
            'numero': $('#numero').val(),
            'tarjeta': $('#tarjeta').val(),
            'tipo': $('#tipo').val(),
            'condominios': get_condominio()
        })
        ajax_call('nropase_update', {
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
        cb_title = "¿Deshabilitar Nro de Pase?"

    } else {
        cb_title = "¿Habilitar Nro de Pase?"
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
        ajax_call('nropase_delete', {
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


function sincronizacion(elemento){
    obj = JSON.stringify({
        'id': parseInt(JSON.parse($(elemento).attr('data-json')))
    })
    ajax_call('nropase_sincronizacion', {
        _xsrf: getCookie("_xsrf"),
        object: obj
    }, null, function () {

    })
}

validationKeyup("form")
validationSelectChange("form")