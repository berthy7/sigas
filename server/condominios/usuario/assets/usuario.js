main_route = '/usuarioCondominio'
var data_privilegios_js = [];

$(document).ready(function () {
    if ($('#sigas').val() == "True"){
        console.log("rol sigas")
        $('#div_filtro').show()


    }else{
         console.log("rol condominio")
        $('#div_filtro').hide()

    }
});

$('.show-tick').selectpicker()

$('.dd').nestable({
    group:'categories',
    maxDepth:0,
    reject: [{
        rule: function () {
            // The this object refers to dragRootEl i.e. the dragged element.
            // The drag action is cancelled if this function returns true
            var ils = $(this).find('>ol.dd-list > li.dd-item');
            for (var i = 0; i < ils.length; i++) {
                var datatype = $(ils[i]).data('type');
                if (datatype === 'child')
                    return true;
            }
            return false;
        },
        action: function (nestable) {
            // This optional function defines what to do when such a rule applies. The this object still refers to the dragged element,
            // and nestable is, well, the nestable root element
            alert('Can not move this item to the root');
        }
    }]
});

$('.module').click(function () {
    var checked = $(this).prop('checked')
    //$('.module').prop('checked', false)
    empresa_id = null
    sucursal_id = null
    gerencia_id = null
    grupo_id = null
    emp_id = null
    if ($(this).hasClass('employee')){
        emp_id = parseInt($(this).attr('data-id'))
    } else {
        if ($(this).hasClass('grupo')){
            grupo_id = parseInt($(this).attr('data-id'))
            gerencia_id = parseInt($(this).attr('data-ger'))
            sucursal_id = parseInt($(this).attr('data-suc'))
            empresa_id = parseInt($(this).attr('data-empr'))
        } else {
            if ($(this).hasClass('gerencia')){
                gerencia_id = parseInt($(this).attr('data-id'))
                sucursal_id = parseInt($(this).attr('data-suc'))
                empresa_id = parseInt($(this).attr('data-empr'))
            }else {
                if($(this).hasClass('sucursal')){
                    sucursal_id = parseInt($(this).attr('data-id'))
                    empresa_id = parseInt($(this).attr('data-empr'))
                }else {
                    if($(this).hasClass('empresa')){
                        empresa_id_id = parseInt($(this).attr('data-id'))
                    }
                }
            }
        }
    }
    $(this).prop('checked', checked)
    $(this).parent().next().find('.module').prop('checked', $(this).prop('checked'))
    analizar($(this).parent().parent().closest('.dd-list').prev().find('.module'))
})

function analizar(parent) {
    children = $(parent).parent().next().find('.module:checked')
    //console.log(children.length)
    $(parent).prop('checked', (children.length > 0))
    grand_parent = $(parent).parent().parent().closest('.dd-list').prev().find('.module')
    //console.log(grand_parent.length)
    if (grand_parent.length > 0){
        analizar(grand_parent)
    }
}

function obtener_usuarios_id() {
    aux = []
    $('.employee').each(function () {

        var a = parseInt($(this).attr('data-id'))
        var check = $(this).prop('checked')

        console.log("usuario id : "+ a)
        console.log("usuario estado : "+check)

        aux.push((function add(a,check) {

            return {
                'id': a,
                'estado': check
            }


        })(a,check))

    })
    return aux
}


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



function cargar_tabla2(data){

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

function cargar_tabla(data,data_privilegios){
    
    for (dat in data_privilegios) {
            data_privilegios_js.push( data_privilegios[dat]);
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
        "order": [[ 0, "asc" ]],
        language : {
            'url': '/resources/js/spanish.json',
        },
        "pageLength": 50
    });
}

function actualizar_data(response){

    var data = [];
    var id
    var condominio =""
    
    for (var i = 0; i < Object.keys(response.response).length; i++) {
        var estado = ""
        var login = ""
        var acciones = ""
        id = response['response'][i]['id']


        if(data_privilegios_js.includes('usuarioCondominio_state')){
            if(response['response'][i]['estado']){
                estado = "<input id='" + id + "' onClick='event.preventDefault();estado(this)' data-id='" + id + "' type='checkbox' class='chk-col-indigo' checked /><label for='" + id + "'></label>"
            }else{
               estado = "<input id='" + id + "' onClick='event.preventDefault();estado(this)' data-id='" + id + "' type='checkbox' class='chk-col-indigo' /><label for='" + id + "'></label>"
            }
        }else{
            if(response['response'][i]['estado']){
                estado = "<input id='" + id + "' onClick='event.preventDefault();estado(this)' data-id='" + id + "' type='checkbox' class='chk-col-indigo' checked disabled/><label for='" + id + "'></label>"
            }else{
               estado = "<input id='" + id + "' onClick='event.preventDefault();estado(this)' data-id='" + id + "' type='checkbox' class='chk-col-indigo' disabled/><label for='" + id + "'></label>"
            }

        }

        if(data_privilegios_js.includes('usuarioCondominio_sesion')){
            if(response['response'][i]['login']){
                login = "<input id='se-" + id + "' onClick='event.preventDefault();sesion(this)' data-id='" + id + "' type='checkbox' class='chk-col-indigo' checked /><label for='se-" + id + "'></label>"
            }else{
               login = "<input id='se-" + id + "' onClick='event.preventDefault();sesion(this)' data-id='" + id + "' type='checkbox' class='chk-col-indigo' /><label for='se-" + id + "'></label>"
            }
        }else{
            if(response['response'][i]['login']){
                login = "<input id='" + id + "' onClick='event.preventDefault();sesion(this)' data-id='" + id + "' type='checkbox' class='chk-col-indigo' checked disabled/><label for='" + id + "'></label>"
            }else{
               login = "<input id='" + id + "' onClick='event.preventDefault();sesion(this)' data-id='" + id + "' type='checkbox' class='chk-col-indigo' disabled/><label for='" + id + "'></label>"
            }

        }

        if(data_privilegios_js.includes('usuarioCondominio_update')){
            acciones += "<button id='edit' onClick='editar(this)' data-json='" + id + "' type='button' class='btn bg-indigo waves-effect waves-light white-own' title='Editar'><i class='material-icons'>create</i></button> "
        }

        if(data_privilegios_js.includes('usuarioCondominio_delete')){
            acciones += "<button id='delete' onClick='eliminar(this)' data-json='" + id + "' type='button' class='btn bg-indigo waves-effect waves-light white-own' title='Eliminar'><i class='material-icons'>delete</i></button> "
        }
        
        
        if(response['response'][i]['fkcondominio']){
            condominio = response['response'][i]['condominio']['nombre']
        }else{
            condominio  = "------"
        }


        data.push( [
            response['response'][i]['id'],
            response['response'][i]['codigo'],
            response['response'][i]['fullname'],
            response['response'][i]['username'],
            response['response'][i]['rol']['nombre'],
            condominio,
            estado,
            login,
            acciones
        ]);
    }
    return data
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
                console.log(response)
                if(response.success === true){

                    swal(
                          'Actualizada Correctamente.',
                          '',
                          'success'
                    )
                    $('#password').val(response.response.response)

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

    if (parseInt($('#fkrol').val())===7) {
        swal(
            'El registro de usuarios para residentes, se debe realizar en el menu de Residentes',
             '',
            'warning'
        )

    }else{
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
                    
                    ajax_call('usuarioCondominio_insert', {
                        object: objeto,
                        _xsrf: getCookie("_xsrf")
                    }, null, function (response) {
                        response = JSON.parse(response);
                        
                        var data = actualizar_data(response);

                        cargar_tabla(data)
                    })
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
        $('#password').val(self.default)
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
        $('#div_username').show()
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
                    
                    var data = actualizar_data(response);

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

function estado(elemento){
    console.log("estado")
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
        ajax_call('usuarioCondominio_state', {
            object: objeto,
            _xsrf: getCookie("_xsrf")
        }, null, function (response) {
            
            response = JSON.parse(response);
            
            var data = actualizar_data(response);

            cargar_tabla(data)
            
        })
        $('#form').modal('hide')
    })
}

function eliminar(elemento){

    cb_title = "¿Eliminar Usuario?"
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
            id: parseInt(JSON.parse($(elemento).attr('data-json')))
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

function sesion(elemento){
    console.log("Sesion")
    cb_delete = elemento
    b = $(elemento).prop('checked')
    if (!b) {
        cb_title = "¿Cerrar Session del Usuario?"

    } else {
        cb_title = "¿Iniciar Session del Usuario?"
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
        ajax_call('usuarioCondominio_sesion', {
            object: objeto,
            _xsrf: getCookie("_xsrf")
        }, null, function (response) {

            response = JSON.parse(response);

            var data = actualizar_data(response);

            cargar_tabla(data)

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

$('#sincronizar').click(function () {
    console.log("sincronizar")
    $('.module').prop('checked', false)
    $('#desplegable').show()
    $('#form-sincro').modal('show')

    obj = JSON.stringify({

    })
    ajax_call_get('usuarioCondominio_listar_todo', {
        _xsrf: getCookie("_xsrf"),
        object: obj
    }, function (response) {
        var self = response;

        for(i in self){

            employe_cb = $('.employee[data-id="'+self[i].id+'"]')
            employe_cb.prop('checked', self[i].estado)
            analizar(employe_cb.parent().parent().closest('.dd-list').prev().find('.module'))
        }
    })

})

$('#guardar_sincro').click(function () {
    obj = JSON.stringify({
        'usuarios': obtener_usuarios_id()
    })
    ajax_call('usuarioCondominio_insert_sincro', {
        _xsrf: getCookie("_xsrf"),
        object: obj
    },null, function () {
        setTimeout(function () {
            window.location = main_route
        }, 2000);
    })

    $('#desplegable').hide()
    $('#form-sincro').modal('hide')

})

validationKeyup("form")
validationSelectChange("form")

