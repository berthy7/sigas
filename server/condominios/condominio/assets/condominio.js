main_route = '/condominio'

$(document).ready(function () {
    $('#data_table').DataTable();

    
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

//////////////////////////////////////////////////editar///////////////////////////////////////////////////////////////////////
    function append_input_entradas(id_in) {

        $('#entradas_div').append(
            '<div class="row" >\
                 <div class="col-sm-1" hidden>\
                    <div class="input-group">\
                    <input  id="id'+id_in+'" class="form-control condominioentrada readonly">\
                    </div>\
                 </div>\
                 <div class="col-sm-1">\
                    <div class="input-group">\
                    <input  id="fkentrada_'+id_in+'" value="'+id_in+'" class="form-control condominioentrada readonly">\
                    </div>\
                 </div>\
                 <div class="col-sm-5">\
                    <div class="input-group">\
                        <div><input id="nombre_'+id_in+'" type="text" class="form-control" readonly></div>\
                    </div>\
                 </div>\
                 <div id="c_'+id_in+'" class="col-md-2">\
                    <input id="b_'+id_in+'" type="checkbox" class="regular-checkbox big-checkbox condominioentrada" data-id="1" >\
                    <label for="b_'+id_in+'"></label>\
                 </div>\
             </div>'
        )
    }

///////////////////////////////////////////////////////////////////////////////////////////////////////////////

function append_table(id) {
        obj = JSON.stringify({
            'idcondominio': parseInt(id)
        })

        ajax_call_get("usuario_obtener_x_condominio",{
            _xsrf: getCookie("_xsrf"),
            object: obj
        },function(response){

            console.log(response)

        var partaux = "";
        var i = 0;
        var editar= ""
        var estado
        for (a in response) {
            estado = response[i].enabled
            if(estado == true){
                estado ="<div><input id='edits' onClick='event.preventDefault();eliminar_usuarios(this)' type='checkbox'  data-id='" + response[i].id + "' class='chk-col-indigo edit_usuarios2' checked/><label for='" + response[i].id + "'></label>Habilitado</div>"
            }else{
                estado ="<div><input id='edits' onClick='event.preventDefault();eliminar_usuarios(this)' type='checkbox'  data-id='" + response[i].id + "' class='chk-col-indigo edit_usuarios2'/><label for='" + response[i].id + "'></label>Deshabilitado</div>"

            }
            var editar ="<button id='edit' type='button'  data-json='" + response[i].id + "' class='btn bg-indigo waves-effect waves-light edit_usuarios' title='Editar'><i class='material-icons'>create</i></button>"
            
            partaux = partaux + '<tr><td>' + response[i].fullname + '</td><td>' + response[i].telefono + '</td><td>' + response[i].username + '</td><td>' + response[i].rol.nombre + '</td><td>' + estado + '</td><td>' + editar + '</td></tr>';

            i = i + 1;

        }

        $('#table_usuarios').append(
            '<div class="row">\
                <div class="body table-responsive">\
                <table id="data_table" class="table table-bordered table-striped table-hover js-basic-example js-exportable dataTable">\
                <thead>\
                    <tr>\
                    <th class="order_by_th" data-name="names">Nombre Completo  </th>\
                    <th class="order_by_th" data-name="names">Telefono  </th>\
                    <th class="order_by_th" data-name="names">Username </th>\
                    <th class="order_by_th" data-name="names">Perfil </th>\
                    <th class="order_by_th" data-name="names">Estado </th>\
                    <th class="actions_header">Acciones</th>\
                          </tr>\
                          </thead>\
                           <tbody id="table_content">' + partaux + '</tbody>\
        </table>\
        </div>\
        </div>'
        )

        $('.clear_schedule').last().click(function () {
            $(this).parent().parent().remove()
        })
    })

        $('#cerrar').click(function (e) {
         e.preventDefault();

            $('#plan_auditor').modal('hide')

            })

        $('.edit_usuarios').click(function () {
            obj = JSON.stringify({
                'id': parseInt(JSON.parse($(this).attr('data-json')))
            })

            ajax_call_get('usuarioCondominio_update', {
                _xsrf: getCookie("_xsrf"),
                object: obj
            }, function (response) {

                var self = response;

                $('#idusuario').val(self.id),
                $('#fkrol').val(self.fkrol),
                $('#fkrol').selectpicker('refresh'),
                $('#nombre_usuario').val(self.nombre),
                $('#apellidop').val(self.apellidop),
                $('#apellidom').val(self.apellidom),
                $('#telefono').val(self.telefono),
                $('#username').val(self.username),
                $('#password').val(self.password),
                $('#ci').val(self.ci),
                $('#correo').val(self.correo),
                $('#expendido').val(self.expendido),
                $('#expendido').selectpicker('refresh'),

                clean_form(),
                verif_inputs(),

                $('#fkrol').parent().addClass('focused'),
                $('#nombre_usuario').parent().addClass('focused'),
                $('#apellidop').parent().addClass('focused'),
                $('#apellidom').parent().addClass('focused'),
                $('#telefono').parent().addClass('focused'),


                $('#div_agregar_usuario').show()
                $('#div_update_usuario').show()
                $('#div_insert_usuario').hide()
                $('#div_username').show()
                $('#agregar_usuario').hide()
            })
        })

        $('.edit_usuarios2').click(function () {
            console.log("edi2")
            obj = JSON.stringify({
                'id': parseInt(JSON.parse($(this).attr('data-json')))
            })

            ajax_call_get('usuarioCondominio_update', {
                _xsrf: getCookie("_xsrf"),
                object: obj
            }, function (response) {

                var self = response;

                $('#idusuario').val(self.id),
                $('#fkrol').val(self.fkrol),
                $('#fkrol').selectpicker('refresh'),
                $('#nombre_usuario').val(self.nombre),
                $('#apellidop').val(self.apellidop),
                $('#apellidom').val(self.apellidom),
                $('#telefono').val(self.telefono),
                $('#username').val(self.username),
                $('#password').val(self.password),
                $('#ci').val(self.ci),
                $('#correo').val(self.correo),
                $('#expendido').val(self.expendido),
                $('#expendido').selectpicker('refresh'),

                clean_form(),
                verif_inputs(),

                $('#fkrol').parent().addClass('focused'),
                $('#nombre_usuario').parent().addClass('focused'),
                $('#apellidop').parent().addClass('focused'),
                $('#apellidom').parent().addClass('focused'),
                $('#telefono').parent().addClass('focused'),


                $('#div_agregar_usuario').show()
                $('#div_update_usuario').show()
                $('#div_insert_usuario').hide()
                $('#div_username').show()
                $('#agregar_usuario').hide()
            })
        })

        function eliminar_usuarios(elemento){
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

    }

function cargar_entradas() {
    obj = JSON.stringify({
        '_xsrf': getCookie("_xsrf")
    })
    ruta = "condominio_entrada";
    $.ajax({
        method: "POST",
        url: ruta,
        data: {_xsrf: getCookie("_xsrf"), object: obj},
        async: true
    }).done(function (response) {
        response = JSON.parse(response)
        var self = response;
        console.log(self)

        $('#entradas_div').empty()

        for(i in self.response){
            aux0 = self.response[i]['id']
            aux1 = self.response[i]['nombre']

            append_input_entradas(aux0)
            $('#fkentrada_' + aux0).val(aux0)
            $('#nombre_' + aux0).val(aux1)
        }

    })
    
}

function obtener_entradas() {
        objeto = []
        objeto_inputs = $('.condominioentrada')

        for(i=0;i<objeto_inputs.length;i+=3){
            h0 = objeto_inputs[i].value
            h1 = objeto_inputs[i+1].value
            h2 = objeto_inputs[i+2].checked

            //if (!(h0 < h1 && h1 < h2 && h2 < h3 && h3 < h4 && h4 < h5)){


            objeto.push((function add_hours(h0,h1,h2) {

                if (h0 ==''){
                    return {
                    'fkentrada': h1,
                    'estado': h2

                    }

                }else{
                    return {
                    'id':h0,
                    'fkentrada': h1,
                    'estado': h2
                    }
                }

            })(
                    objeto_inputs[i].value,
                    objeto_inputs[i+1].value,
                    objeto_inputs[i+2].checked))
        }
        return objeto
    }

$('#agregar_usuario').click(function () {

    $('#fkrol').val(''),
    $('#fkrol').selectpicker('refresh'),
    $('#nombre_usuario').val(''),
    $('#apellidop').val(''),
    $('#apellidom').val(''),
    $('#telefono').val(''),
    $('#username').val(''),
    $('#password').val(''),
    $('#correo').val('')
    $('#ci').val('')
    $('#expendido').val('')
    $('#expendido').selectpicker('refresh')

    $('#div_agregar_usuario').show(),
    $('#div_update_usuario').hide(),
    $('#div_insert_usuario').show(),
    $('#agregar_usuario').hide(),
    $('#div_username').hide(),
    validationInputSelects("form_usuarios")

})

$('#insert_usuario').click(function () {
    if(!validationInputSelects("form_usuarios")){
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
        'fkcondominio': parseInt($('#idcondominio').val())
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
                    _xsrf: getCookie("_xsrf"),
                    object: objeto
                }, null, function (response) {
                    response = JSON.parse(response);
                    if(response.success === true){
    
                            $('#table_usuarios').empty();
                             append_table($('#idcondominio').val())
                    }else{
    
                        swal(
                            'Datos duplicados',
                            response.message,
                            'error'
                        )
                    }
    
                })
                showMessage("Insertado Correctamente", "success", "ok")
                $('#div_agregar_usuario').hide()
                 $('#agregar_usuario').show()
    
            }else{
                swal(
                    'Correo en uso',
                    'El correo ya se encuentra, en uso porfavor, ingrese otro correo electronico',
                    'warning' )
            }
        });
        
    }else{
        swal(
            'Error de datos.',
            'Hay campos vacíos por favor verifique sus datos.',
            'error'
        )
    }

})

$('#update_usuario').click(function () {
    objeto = JSON.stringify({
        'id': parseInt($('#idusuario').val()),
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
        'fkcondominio': parseInt($('#idcondominio').val())
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
                _xsrf: getCookie("_xsrf"),
                object: objeto
            }, null, function (response) {
                response = JSON.parse(response);
                if(response.success === true){


                    $('#div_agregar_usuario').hide()
                     $('#agregar_usuario').show()
                    $('#table_usuarios').empty();
                     append_table($('#idcondominio').val())

                }else{

                    swal(
                        'Datos duplicados',
                        response.message,
                        'error'
                    )
                }

            })
            $('#form').modal('hide')

        }else{
            swal(
                'Nombre de usuario en uso',
                'Por favor ingrese otro nombre de usuario',
                'warning' )
        }
    });


})

$('#cerrar_usuario').click(function () {
    $('#div_agregar_usuario').hide()
     $('#agregar_usuario').show()
})

$('#new').click(function () {
    cargar_entradas()
    $('#contrato').val('')
    $('#fechai').val('')
    $('#fechaf').val('')
    $('#codigo').val('')
    $('#nombre').val('')
    $('#cant_casas').val('')
    $('#cant_departamentos').val('')
    $('#cant_residentes').val('')
    $('#cant_vehiculos').val('')
    $('#cant_tarjetas').val('')
    $('#ip_publica').val('')
    $('#ip_privada').val('')
    $('#puerto').val('')
    document.getElementById('singuardia').checked=false
    document.getElementById('invitacionpaselibre').checked=false
    document.getElementById('invitacionmultiple').checked=false
    
    verif_inputs('')
    validationInputSelects("form")
    $('#id_div').hide()
    $('#insert').show()
    $('#update').hide()
    $('#form').modal('show')
})

$('.new_usuarios').click(function () {
    $('#nombrecondominio').val($(this).attr('data-nombre'))
    $('#idcondominio').val($(this).attr('data-id'))
    $('#fkrol').val('')
    $('#fkrol').selectpicker('refresh')
    $('#nombre').val('')
    $('#apellidop').val('')
    $('#apellidom').val('')
    $('#telefono').val('')
    $('#username').val('')
    $('#password').val('')
    $('#correo').val('')
    $('#ci').val('')
    $('#expendido').val('')
    $('#expendido').selectpicker('refresh')


    $('#table_usuarios').empty();
    append_table($(this).attr('data-id'))

    verif_inputs('')
    validationInputSelects("form_usuarios")
    $('#id_div').hide()
    $('#div_agregar_usuario').hide()
    $('#agregar_usuario').show()
    $('#insert').show()
    $('#update').hide()
    $('#form_usuarios').modal('show')
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
             'idusuario': parseInt($('#idusuario').val()),
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
            'contrato': $('#contrato').val(),
            'fechai': $('#fechai').val(),
            'fechaf': $('#fechaf').val(),
            'codigo': $('#codigo').val(),
            'nombre': $('#nombre').val(),
            'cant_casas': $('#cant_casas').val(),
            'cant_departamentos': $('#cant_departamentos').val(),
            'cant_residentes': $('#cant_residentes').val(),
            'cant_vehiculos': $('#cant_vehiculos').val(),
            'cant_tarjetas': $('#cant_tarjetas').val(),
            'ip_publica': $('#ip_publica').val(),
            'ip_privada': $('#ip_privada').val(),
            'puerto': $('#puerto').val(),
            'entradas': obtener_entradas(),
            'singuardia':document.getElementById('singuardia').checked,
            'invitacionpaselibre':document.getElementById('invitacionpaselibre').checked,
            'invitacionmultiple':document.getElementById('invitacionmultiple').checked

        })
        ajax_call('condominio_insert', {
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

function attach_edit() {
    $('.edit').click(function () {
        obj = JSON.stringify({
            'id': parseInt(JSON.parse($(this).attr('data-json')))
        })
        ajax_call_get('condominio_update', {
            _xsrf: getCookie("_xsrf"),
            object: obj
        }, function (response) {
            var self = response;
            $('#id').val(self.id)
            $('#contrato').val(self.contrato)
            $('#fechai').val(self.fechai)
            $('#fechaf').val(self.fechaf)
            $('#codigo').val(self.codigo)
            $('#nombre').val(self.nombre)
            $('#cant_casas').val(self.cant_casas)
            $('#cant_departamentos').val(self.cant_departamentos)
            $('#cant_residentes').val(self.cant_residentes)
            $('#cant_vehiculos').val(self.cant_vehiculos)
            $('#cant_tarjetas').val(self.cant_tarjetas)
            $('#ip_publica').val(self.ip_publica)
            $('#ip_privada').val(self.ip_privada)
            $('#puerto').val(self.puerto)
            document.getElementById('singuardia').checked=self.singuardia
             document.getElementById('invitacionpaselibre').checked=self.invitacionpaselibre
             document.getElementById('invitacionmultiple').checked=self.invitacionmultiple
            
            $('#entradas_div').empty()
            for(i in self.entradas){
                aux0 = self.entradas[i]['id']
                aux1 = self.entradas[i]['fkentrada']
                aux2 = self.entradas[i]['entrada'].nombre
                aux3 = self.entradas[i]['estado']

                append_input_entradas(aux0)
                $('#id' + aux0).val(aux0)
                $('#fkentrada_' + aux0).val(aux1)
                $('#nombre_' + aux0).val(aux2)
                $('#b_' + aux0).prop('checked', aux3)
            }

            validationInputSelects("form")
            verif_inputs('')
            $('#id_div').hide()
            $('#insert').hide()
            $('#update').show()
            $('#form').modal('show')
        })
    })
}
attach_edit()

$('#update').click(function () {
    notvalid = validationInputSelectsWithReturn("form");
    if (notvalid===false) {
        objeto = JSON.stringify({
            'id': parseInt($('#id').val()),
            'contrato': $('#contrato').val(),
            'fechai': $('#fechai').val(),
            'fechaf': $('#fechaf').val(),
            'codigo': $('#codigo').val(),
            'nombre': $('#nombre').val(),
            'cant_casas': $('#cant_casas').val(),
            'cant_departamentos': $('#cant_departamentos').val(),
            'cant_residentes': $('#cant_residentes').val(),
            'cant_vehiculos': $('#cant_vehiculos').val(),
            'cant_tarjetas': $('#cant_tarjetas').val(),
            'ip_publica': $('#ip_publica').val(),
            'ip_privada': $('#ip_privada').val(),
            'puerto': $('#puerto').val(),
            'entradas': obtener_entradas(),
            'singuardia':document.getElementById('singuardia').checked,
            'invitacionpaselibre':document.getElementById('invitacionpaselibre').checked,
            'invitacionmultiple':document.getElementById('invitacionmultiple').checked

        })
        ajax_call('condominio_update', {
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

$('.delete').click(function () {
    id = parseInt(JSON.parse($(this).attr('data-json')))
    enabled = false
    swal({
        title: "¿Eliminar Condominio?",
        type: "warning",
        showCancelButton: true,
        confirmButtonColor: "#393939",
        cancelButtonColor: "#F44336",
        confirmButtonText: "Aceptar",
        cancelButtonText: "Cancelar"
    }).then(function () {
        ajax_call('condominio_delete', {
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

function eliminar(elemento){
    console.log("s")
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

validationKeyup("form")
validationSelectChange("form")
validationKeyup("form_usuarios")
validationSelectChange("form_usuarios")