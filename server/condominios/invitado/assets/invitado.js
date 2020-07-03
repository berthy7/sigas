main_route = '/invitado'

$(document).ready(function () {

});

id_gv = 0

$(document).ajaxStart(function () { });

$(document).ajaxStop(function () {
    $.Toast.hideToast();
});



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

$('#sexo').selectpicker({
    size: 10,
    liveSearch: true,
    liveSearchPlaceholder: 'Buscar',
    title: 'Seleccione'
})

$('#tipo').selectpicker({
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

$('#tipovehiculo').selectpicker({
    size: 10,
    liveSearch: true,
    liveSearchPlaceholder: 'Buscar',
    title: 'Seleccione'
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


    $('#insertar_vehiculo').click(function () {
            append_input_vehiculos('')

            var id_placa = ''
            $("input.placa").each(function() {
                id_placa  = $(this).prop('id');
            });


            var id_tipo = ''
            $("input.tipo").each(function() {
                id_tipo  = $(this).prop('id');
            });

            var id_color = ''
            $("input.color").each(function() {
                id_color  = $(this).prop('id');
            });

            var id_fkmarca = ''
            $("input.fkmarca").each(function() {
                id_fkmarca  = $(this).prop('id');
            });

            var id_marca = ''
            $("input.marca").each(function() {
                id_marca  = $(this).prop('id');
            });

            var id_fkmodelo = ''
            $("input.fkmodelo").each(function() {
                id_fkmodelo  = $(this).prop('id');
            });

            var id_modelo = ''
            $("input.modelo").each(function() {
                id_modelo  = $(this).prop('id');
            });



            var id_vehiculo = ''
            $("input.id").each(function() {
                id_vehiculo = $(this).prop('id');
            });

            $('#' + id_vehiculo ).val('')
            $('#' + id_vehiculo ).parent().addClass('focused')
            $('#' + id_placa).val($('#placa').val())
            $('#' + id_placa).parent().addClass('focused')
            $('#' + id_tipo).val($('#tipovehiculo').val())
            $('#' + id_tipo).parent().addClass('focused')
            $('#' + id_color).val($('#color').val())
            $('#' + id_color).parent().addClass('focused')
            $('#' + id_fkmarca).val($('#fkmarca').val())
            $('#' + id_fkmarca).parent().addClass('focused')
            $('#' + id_marca).val($( "#fkmarca option:selected" ).text())
            $('#' + id_marca).parent().addClass('focused')
            $('#' + id_fkmodelo).val($('#fkmodelo').val())
            $('#' + id_fkmodelo).parent().addClass('focused')
            $('#' + id_modelo).val($( "#fkmodelo option:selected" ).text())
            $('#' + id_modelo).parent().addClass('focused')
            $('#div_nuevo_vehiculo').hide()

    })

    $('#vehiculos').change(function () {
        if (parseInt(JSON.parse($('#vehiculos').val())) != 0){
            obj = JSON.stringify({
                'id': parseInt(JSON.parse($('#vehiculos').val())),
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
                append_input_vehiculos('')

                var id_placa = ''
                $("input.placa").each(function() {
                    id_placa  = $(this).prop('id');
                });


                var id_tipo = ''
                $("input.tipo").each(function() {
                    id_tipo  = $(this).prop('id');
                });

                var id_color = ''
                $("input.color").each(function() {
                    id_color  = $(this).prop('id');
                });

                var id_fkmarca = ''
                $("input.fkmarca").each(function() {
                    id_fkmarca  = $(this).prop('id');
                });

                var id_marca = ''
                $("input.marca").each(function() {
                    id_marca  = $(this).prop('id');
                });

                var id_fkmodelo = ''
                $("input.fkmodelo").each(function() {
                    id_fkmodelo  = $(this).prop('id');
                });

                var id_modelo = ''
                $("input.modelo").each(function() {
                    id_modelo  = $(this).prop('id');
                });



                var id_vehiculo = ''
                $("input.id").each(function() {
                    id_vehiculo = $(this).prop('id');
                });

                $('#' + id_vehiculo ).val(response.response.id)
                $('#' + id_vehiculo ).parent().addClass('focused')
                $('#' + id_placa).val(response.response.placa)
                $('#' + id_placa).parent().addClass('focused')
                $('#' + id_tipo).val(response.response.tipo)
                $('#' + id_tipo).parent().addClass('focused')
                $('#' + id_color).val(response.response.color)
                $('#' + id_color).parent().addClass('focused')
                $('#' + id_fkmarca).val(response.response.fkmarca)
                $('#' + id_fkmarca).parent().addClass('focused')
                $('#' + id_marca).val(response.response.marca.nombre)
                $('#' + id_marca).parent().addClass('focused')
                $('#' + id_fkmodelo).val(response.response.fkmodelo)
                $('#' + id_fkmodelo).parent().addClass('focused')
                $('#' + id_modelo).val(response.response.modelo.nombre)
                $('#' + id_modelo).parent().addClass('focused')

            })

            $('#div_nuevo_vehiculo').hide()

        }else{
             $('#div_nuevo_vehiculo').show()
            // append_input_vehiculos('')
             $('#tipovehiculo').val('')
            $('#tipovehiculo').selectpicker('refresh')
            $('#placa').val('')
            $('#color').val('')
            $('#fkmarca').val('')
            $('#fkmarca').selectpicker('refresh')
            $('#fkmodelo').val('')
            $('#fkmodelo').selectpicker('refresh')
        }
        $('#vehiculos').val('')
        $('#vehiculos').selectpicker('refresh')

    });

    function append_input_vehiculos(id_in) {
        if(id_in === ''){
            id_gv++;
            id_in = id_gv;
        }

        $('#vehiculo_div').append(
        '<div class="row">\
            <div class="col-sm-1 hidden">\
                <div class="input-group">\
                    <input  id="id'+id_in+'" class="form-control id vehiculo txta-own">\
                </div>\
            </div>\
            <div class="col-sm-1 ">\
                <div class="form-line">\
                    <input id="placa'+id_in+'" data-id="'+id_in+'" class="form-control vehiculo placa  txta-own">\
                </div>\
            </div>\
            <div class="col-sm-1">\
                <div  class="form-line">\
                    <input id="tipo'+id_in+'" data-id="'+id_in+'" class="form-control vehiculo tipo  txta-own">\
                </div>\
            </div>\
            <div class="col-sm-1">\
                <div  class="form-line">\
                    <input id="color'+id_in+'" data-id="'+id_in+'" class="form-control vehiculo color  txta-own">\
                </div>\
            </div>\
            <div class="col-sm-1 hidden">\
                <div  class="form-line">\
                    <input id="fkmarca'+id_in+'" data-id="'+id_in+'" class="form-control vehiculo fkmarca  txta-own">\
                </div>\
            </div>\
            <div class="col-sm-1">\
                <div  class="form-line">\
                    <input id="marca'+id_in+'" data-id="'+id_in+'" class="form-control  marca  txta-own">\
                </div>\
            </div>\
            <div class="col-sm-1 hidden">\
                <div  class="form-line">\
                    <input id="fkmodelo'+id_in+'" data-id="'+id_in+'" class="form-control vehiculo fkmodelo  txta-own">\
                </div>\
            </div>\
            <div class="col-sm-1">\
                <div  class="form-line">\
                    <input id="modelo'+id_in+'" data-id="'+id_in+'" class="form-control  modelo  txta-own">\
                </div>\
            </div>\
            <div class="col-sm-1">\
                <button type="button" class="btn bg-red waves-effect clear_vehiculo" title="Eliminar">\
                    <i class="material-icons">clear</i>\
                </button>\
            </div>\
        </div>'
    )

        $('.clear_vehiculo').last().click(function () {
            $(this).parent().parent().remove()
        })

        $('.id').focus(function () {
            $(this).parent().addClass('focused');
            current_input = $(this).prop('id');
        })

        $('.placa').focus(function () {
            $(this).parent().addClass('focused');
            current_input = $(this).prop('id');
        })

        $('.tipo').focus(function () {
            $(this).parent().addClass('focused');
            current_input = $(this).prop('id');
        })

        $('.color').focus(function () {
            $(this).parent().addClass('focused');
            current_input = $(this).prop('id');
        })

        $('.fkmarca').focus(function () {
            $(this).parent().addClass('focused');
            current_input = $(this).prop('id');
        })

        $('.marca').focus(function () {
            $(this).parent().addClass('focused');
            current_input = $(this).prop('id');
        })

        $('.fkmodelo').focus(function () {
            $(this).parent().addClass('focused');
            current_input = $(this).prop('id');
        })

        $('.modelo').focus(function () {
            $(this).parent().addClass('focused');
            current_input = $(this).prop('id');
        })


    }

    function get_vehiculos() {
        objeto = []
        objeto_inputs = $('.vehiculo')

        for (i = 0; i < objeto_inputs.length; i += 6) {
            h0 = objeto_inputs[i].value
            h1 = objeto_inputs[i + 1].value
            h2 = objeto_inputs[i + 2].value
            h3 = objeto_inputs[i + 3].value
            h4 = objeto_inputs[i + 4].value
            h5 = objeto_inputs[i + 5].value

            if(h1!=""){
                objeto.push((function add_objeto(h0, h1, h2,h3,h4,h5) {

                if (h0 !=''){
                    return {
                        'placa': h1,
                        'tipo': h2,
                        'color': h3,
                        'fkmarca': h4,
                        'fkmodelo': h5
                        }


                }else{
                    return {
                        'id':h0,
                        'placa': h1,
                        'tipo': h2,
                        'color': h3,
                        'fkmarca': h4,
                        'fkmodelo': h5
                        }
                }

            })(
                h0,
                h1,
                h2,
                h3,
                h4,
                h5))
            }



        }
        return objeto
    }

$('#vehiculos').selectpicker({
size: 10,
liveSearch: true,
liveSearchPlaceholder: 'Buscar vehiculo',
title: 'Seleccione Vehiculo'
})



$('#agregar_vehiculo').click(function () {

    $('#div_agregar_vehiculo').hide()
    $('#div_buscar_vehiculo').show()
    $('#div_cancelar_vehiculo').show()

})

$('#cancelar_vehiculo').click(function () {

    $('#div_buscar_vehiculo').hide()
    $('#div_cancelar_vehiculo').hide()
    $('#div_agregar_vehiculo').show()

})

$('#new').click(function () {
    $('#codigo').val('')
    $('#nombre').val('')
    $('#apellidop').val('')
    $('#apellidom').val('')
    $('#sexo').val('M')
    $('#sexo').selectpicker('refresh')
    $('#ci').val('')
    $('#telefono').val('')
    $('#vehiculo_div').empty()

    verif_inputs('')
    validationInputSelects("form")
     $('#div_nuevo_vehiculo').hide()
    $('#id_div').hide()
    $('#insert').show()
    $('#update').hide()
    $('#form').modal('show')
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

$('#insert').click(function () {
    notvalid = validationInputSelectsWithReturn("form");
    if (notvalid===false) {
        objeto = JSON.stringify({
            'nombre': $('#nombre').val(),
            'apellidop': $('#apellidop').val(),
            'apellidom': $('#apellidom').val(),
            'sexo': $('#sexo').val(),
            'ci': $('#ci').val(),
            'expendido': $('#expendido').val(),
            'telefono': $('#telefono').val(),
            'vehiculos' : get_vehiculos()
        })
        ajax_call('invitado_insert', {
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


$('#insert-importar').on('click',function (e) {
     e.preventDefault();

    var data = new FormData($('#importar-form')[0]);

    ruta = "invitado_importar";
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
                query_render('/invitado');
            });
        }
    })
    $('#form').modal('hide')
})


function editar(elemento){
    obj = JSON.stringify({
        'id': parseInt(JSON.parse($(elemento).attr('data-json')))
    })
    ajax_call_get('invitado_update', {
        _xsrf: getCookie("_xsrf"),
        object: obj
    }, function (response) {
        var self = response;
            $('#id').val(self.id)
            $('#nombre').val(self.nombre)
            $('#apellidop').val(self.apellidop)
            $('#apellidom').val(self.apellidom)
            $('#sexo').val(self.sexo)
            $('#sexo').selectpicker('refresh')
            $('#ci').val(self.ci)
            $('#expendido').val(self.expendido)
            $('#expendido').selectpicker('refresh')
            $('#telefono').val(self.telefono)

            $('#vehiculo_div').empty()

            for (vehi in self.vehiculos) {
                idve = self.vehiculos[vehi]['id']
                placa= self.vehiculos[vehi]['placa']
                tipo = self.vehiculos[vehi]['tipo']
                color = self.vehiculos[vehi]['color']
                fkmarca = self.vehiculos[vehi]['fkmarca']
                nombremarca = self.vehiculos[vehi]['nombremarca']
                fkmodelo = self.vehiculos[vehi]['fkmodelo']
                nombremodelo = self.vehiculos[vehi]['nombremodelo']

                append_input_vehiculos(idve)
                $('#id' + idve).val(idve)
                $('#placa' + idve).val(placa)
                $('#tipo' + idve).val(tipo)
                $('#color' + idve).val(color)
                $('#fkmarca' + idve).val(fkmarca)
                $('#marca' + idve).val(nombremarca)
                $('#fkmodelo' + idve).val(fkmodelo)
                $('#modelo' + idve).val(nombremodelo)
            }


            clean_form()
            verif_inputs('')
            validationInputSelects("form")
            $('#id_div').hide()
            $('#insert').hide()
            $('#update').show()
            $('#div_nuevo_vehiculo').hide()
            $('#form').modal('show')
    })
    }

$('#update').click(function () {
    notvalid = validationInputSelectsWithReturn("form");
    if (notvalid===false) {
        objeto = JSON.stringify({
            'id': parseInt($('#id').val()),
            'nombre': $('#nombre').val(),
            'apellidop': $('#apellidop').val(),
            'apellidom': $('#apellidom').val(),
            'sexo': $('#sexo').val(),
            'ci': $('#ci').val(),
            'expendido': $('#expendido').val(),
            'telefono': $('#telefono').val(),
            'vehiculos' : get_vehiculos()
        })
        ajax_call('invitado_update', {
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
        cb_title = "¿Deshabilitar Invitado?"

    } else {
        cb_title = "¿Habilitar Invitado?"
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
        ajax_call('invitado_delete', {
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

    $('#reporte-xls').click(function () {
        aux = {'datos': ''}
        obj = JSON.stringify(aux)
        ruta = "/invitado_reporte_xls";
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

    ruta = "invitado_importar";
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

validationKeyup("form")
validationSelectChange("form")

