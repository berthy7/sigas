main_route = '/usuarioCondominio'

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

$('#fkrol').selectpicker({
    size: 10,
    liveSearch: true,
    liveSearchPlaceholder: 'Buscar Perfil',
    title: 'Seleccione Perfil'
})

$('#expendido').selectpicker({
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

$('#new').click(function () {
    $('#id').val('')
    $('#nombre_usuario').val('')
    $('#apellidop').val('')
    $('#apellidom').val('')
    $('#telefono').val('')
    $('#username').val('')
    $('#password').val('')
    $('#correo').val('')
    $('#ci').val('')
    $('#expendido').val('')
    $('#expendido').selectpicker('refresh')

    $('#fkrol').val('')
    $('#fkrol').selectpicker('refresh')

    $('#fkcondominio').val($('#idcondominio').val())
    $('#fkcondominio').selectpicker('refresh')
    
    if ($('#sigas').val() == "True"){
        console.log("rol sigas")
        $('#fkcondominio').prop('disabled', false);


    }else{
         console.log("rol condominio")
        $('#fkcondominio').prop('disabled', true);

    }

    verif_inputs('')
    validationInputSelects("form")
    $('#id_div').hide()
    $('#insert').show()
    $('#update').hide()
    $('#div_username').hide()
    $('#form').modal('show')
})

$('#generar').click(function () {

    swal({
        title: "¿Restablecer contraseña?",
        type: "warning",
        showCancelButton: true,
        confirmButtonColor: "#393939",
        cancelButtonColor: "#F44336",
        confirmButtonText: "Aceptar",
        cancelButtonText: "Cancelar"
    }).then(function () {
            objeto = JSON.stringify({
             'idusuario': parseInt($('#id').val()),
             'password': $('#ci').val()

            })
            ajax_call_asincrono('usuario_restablecer_password', {
                _xsrf: getCookie("_xsrf"),
                object: objeto
            }, null, function (response) {
                response = JSON.parse(response);
                if(response.success === true){
                    swal(
                          'Actualizada Correctamente.',
                          '',
                          'success'
                    )
                    $('#password').val($('#ci').val())

                }else{

                    swal(
                        'Datos duplicados',
                        response.message,
                        'error'
                    )
                }

            })



    })



})


$('#insert').click(function () {
    notvalid = validationInputSelectsWithReturn("form");
    if (notvalid===false) {
        objeto = JSON.stringify({
            'nombre': $('#nombre_usuario').val(),
            'apellidop': $('#apellidop').val(),
            'apellidom': $('#apellidom').val(),
            'telefono': $('#telefono').val(),
                
            'username': $('#username').val(),
            'password': $('#password').val(),
            'fkrol': parseInt($('#fkrol').val()),
            'ci': $('#ci').val(),
            'correo': $('#correo').val(),
            'expendido': $('#expendido').val(),
            'fkcondominio': parseInt($('#fkcondominio').val())
            
        })

        objeto_verificar = JSON.stringify({
            'username': $('#correo').val(),

        })
        ajax_call_post("usuario_verificar_username", {
            _xsrf: getCookie("_xsrf"),
            object: objeto_verificar
        }, function (response) {
            console.log(response)
            if(response.success === true){
                ajax_call_asincrono('usuarioCondominio_insert', {
                    object: objeto,
                    _xsrf: getCookie("_xsrf")
                }, null, function (response) {
                    response = JSON.parse(response);
                    var data = [];
                    var id
                    var condominio =""
                    var estado
                    for (var i = 0; i < Object.keys(response.response).length; i++) {
                        id = response['response'][i]['id']

                            if(response['response'][i]['fkcondominio']){
                                condominio = response['response'][i]['condominio']['nombre']
                            }else{
                                condominio  = "------"
                            }
                        estado = response['response'][i]['enabled']
                            if(estado == true){
                                estado = "<input id='" + id + "' onClick='event.preventDefault();eliminar(this)' data-id='" + id + "' type='checkbox' class='chk-col-indigo 'checked disabled/><label for='" + id + "'></label>" +" "+ "Habilitado"

                            }else{
                                estado = "<input id='" + id + "' onClick='event.preventDefault();eliminar(this)'data-id='" + id + "' type='checkbox' class='chk-col-indigo ' disabled/><label for='" + id + "'></label>" + " " + "Deshabilitado"

                            }
                        data.push( [
                            response['response'][i]['id'],
                            response['response'][i]['fullname'],
                            response['response'][i]['username'],
                            response['response'][i]['rol']['nombre'],
                            condominio,
                            estado,
                            "<button id='edit' onClick='editar(this)' data-json='" + id + "' type='button' class='btn bg-indigo waves-effect waves-light edit' title='Editar'><i class='material-icons'>create</i></button>"
                        ]);
                    }

                    cargar_tabla(data)
                })
                showMessage("Insertado Correctamente", "success", "ok")
                $('#form').modal('hide')


            }else{
                swal(
                    'Correo en uso',
                    'El correo ya se encuentra, en uso porfavor, ingrese otro correo electronico',
                    'warning' )
            }
        });

        

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
    ajax_call_get('usuarioCondominio_update', {
        _xsrf: getCookie("_xsrf"),
        object: obj
    }, function (response) {
        var self = response;
        $('#id').val(self.id),
        $('#nombre_usuario').val(self.nombre),
        $('#apellidop').val(self.apellidop),
        $('#apellidom').val(self.apellidom),
        $('#telefono').val(self.telefono),

        $('#username').val(self.username)
        $('#password').val(self.password)
        $('#ci').val(self.ci),
        $('#correo').val(self.correo),
        $('#expendido').val(self.expendido),
        $('#expendido').selectpicker('refresh'),
                            
        $('#fkrol').val(self.fkrol)
        $('#fkrol').selectpicker('render')

        $('#fkcondominio').val(self.fkcondominio)
        $('#fkcondominio').selectpicker('render')

        if ($('#sigas').val() == "True"){
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
            'nombre': $('#nombre_usuario').val(),
            'apellidop': $('#apellidop').val(),
            'apellidom': $('#apellidom').val(),
            'telefono': $('#telefono').val(),
                
            'username': $('#username').val(),
            'password': $('#password').val(),
            'fkrol': parseInt($('#fkrol').val()),
             'ci': $('#ci').val(),
            'correo': $('#correo').val(),
            'expendido': $('#expendido').val(),
            'fkcondominio': parseInt($('#fkcondominio').val())
        })

        objeto_verificar = JSON.stringify({
            'username': $('#username').val(),

        })

        ajax_call_post("usuario_verificar_username", {
            _xsrf: getCookie("_xsrf"),
            object: objeto_verificar
        }, function (response) {
            if(response.success === true){
                ajax_call('usuarioCondominio_update', {
                    object: objeto,
                    _xsrf: getCookie("_xsrf")
                }, null, function (response) {
                    response = JSON.parse(response);
                    var data = [];
                    var id
                    var condominio =""
                    var estado
                    for (var i = 0; i < Object.keys(response.response).length; i++) {
                        id = response['response'][i]['id']

                            if(response['response'][i]['fkcondominio']){
                                condominio = response['response'][i]['condominio']['nombre']
                            }else{
                                condominio  = "------"
                            }
                        estado = response['response'][i]['enabled']
                            if(estado == true){
                                estado = "<input id='" + id + "' onClick='event.preventDefault();eliminar(this)' data-id='" + id + "' type='checkbox' class='chk-col-indigo 'checked disabled/><label for='" + id + "'></label>" +" "+ "Habilitado"

                            }else{
                                estado = "<input id='" + id + "' onClick='event.preventDefault();eliminar(this)'data-id='" + id + "' type='checkbox' class='chk-col-indigo ' disabled/><label for='" + id + "'></label>" + " " + "Deshabilitado"

                            }
                        data.push( [
                            response['response'][i]['id'],
                            response['response'][i]['fullname'],
                            response['response'][i]['username'],
                            response['response'][i]['rol']['nombre'],
                            condominio,
                            estado,
                            "<button id='edit' onClick='editar(this)' data-json='" + id + "' type='button' class='btn bg-indigo waves-effect waves-light edit' title='Editar'><i class='material-icons'>create</i></button>"
                        ]);
                    }

                    cargar_tabla(data)

                })
                showMessage("Modificado Correctamente", "success", "ok")
                $('#form').modal('hide')

            }else{
                swal(
                    'Nombre de usuario en uso',
                    'Por favor ingrese otro nombre de usuario',
                    'warning' )
            }
        });

        
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
        cb_title = "¿Deshabilitar Usuario?"

    } else {
        cb_title = "¿Habilitar Usuario?"
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
        ajax_call('usuarioCondominio_delete', {
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
    ruta = "usuarioCondominio_filtrar";
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

