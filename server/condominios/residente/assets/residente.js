main_route = '/residente'

$(document).ready(function () {

});


$(function () {
    $('#sign_in').validate({
        highlight: function (input) {
            $(input).parents('.form-line').addClass('error');
        },
        unhighlight: function (input) {
            $(input).parents('.form-line').removeClass('error');
        },
        errorPlacement: function (error, element) {
            $(element).parents('.input-group').append(error);
        }
    });
});

$('#see-pass').mousedown(function(){
    $("#ic-pass").css("color", "lightgrey");
    $("#password").prop("type", "text");
    $("#ic-pass").html("visibility");
});

$("#see-pass").mouseup(function(){
    $("#ic-pass").css("color", "grey");
    $("#password").prop("type", "password");
    $("#ic-pass").html("visibility_off");
});

$('#sign_in').submit(function(){
    if(!$('#username').val() == '' && $(!'#password').val() == ''){
        $('#btn-login').html('Espere...')
        $('#msg-data').fadeOut('slow')
    }else{
        $('#msg-data').fadeIn('slow')
    }
});

id_gv = 0
sw = false
accion = "nuevo"
actual_fknropase = ""

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

$('#fkcolor').selectpicker({
    size: 10,
    liveSearch: true,
    liveSearchPlaceholder: 'Buscar',
    title: 'Seleccione'
})

$('#fktipovehiculo').selectpicker({
    size: 10,
    liveSearch: true,
    liveSearchPlaceholder: 'Buscar',
    title: 'Seleccione'
})

$('#fknropase').selectpicker({
    size: 10,
    liveSearch: true,
    liveSearchPlaceholder: 'Buscar',
    title: 'Seleccione'
})

$('#b_fknropase').selectpicker({
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

    function cargar_modelos (idmarca) {
        obj = JSON.stringify({
            'idmarca': idmarca,
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
            console.log(response)
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


    };

$('#b_fknropase').change(function () {
    
    if($('#b_fknropase').val() == "0"){

        $('#fknropase_tarjeta').val("")
        $('#fknropase_tarjeta').parent().addClass('focused')

        
    }else{
        $('#fknropase_peatonal').val($('#b_fknropase').val())
        $('#fknropase_peatonal').parent().addClass('focused')
        $('#fknropase_tarjeta').val($( "#b_fknropase option:selected" ).text())
        $('#fknropase_tarjeta').parent().addClass('focused')
    
    
        $('#b_fknropase').val('')
        $('#b_fknropase').selectpicker('refresh')
        
    }

    

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
        "order": [[ 2, "asc" ]],
        language : {
            'url': '/resources/js/spanish.json',
        },
        "pageLength": 50
    });
}

document.getElementById("tab-residente").click();

    $('#tab-residente').click(function () {
        $('#body-residente').css("display", "block")
        $('#body-vivienda').css("display", "none")
        $('#body-vehiculo').css("display", "none")
        $('#body-usuario').css("display", "none")

        if (accion == "nuevo"){
            $('#siguiente1').show()
            $('#siguiente2').hide()
            $('#siguiente3').hide()
        }else{
            $('#siguiente1').hide()
            $('#siguiente2').hide()
            $('#siguiente3').hide()
        }
    })
    $('#tab-vivienda').click(function () {
        $('#body-residente').css("display", "none")
        $('#body-vivienda').css("display", "block")
        $('#body-vehiculo').css("display", "none")
        $('#body-usuario').css("display", "none")

        $('#div_buscar_vivienda').hide()
        $('#div_cancelar_vivienda').hide()
        $('#div_agregar_vivienda').show()

        if (accion == "nuevo"){
            $('#siguiente1').hide()
            $('#siguiente2').show()
            $('#siguiente3').hide()
        }else{
            $('#siguiente1').hide()
            $('#siguiente2').hide()
            $('#siguiente3').hide()
        }
    })
    $('#tab-vehiculo').click(function () {
        $('#body-residente').css("display", "none")
        $('#body-vivienda').css("display", "none")
        $('#body-vehiculo').css("display", "block")
        $('#body-usuario').css("display", "none")

        $('#div_buscar_vehiculo').hide()
        $('#div_cancelar_vehiculo').hide()
        $('#div_agregar_vehiculo').show()

        if (accion == "nuevo"){
            $('#siguiente1').hide()
            $('#siguiente2').hide()
            $('#siguiente3').show()
        }else{
            $('#siguiente1').hide()
            $('#siguiente2').hide()
            $('#siguiente3').hide()
        }

    })
    $('#tab-usuario').click(function () {
        $('#body-residente').css("display", "none")
        $('#body-vivienda').css("display", "none")
        $('#body-vehiculo').css("display", "none")
        $('#body-usuario').css("display", "block")



        if (accion == "nuevo"){
            $('#insert').show()
            $('#siguiente1').hide()
            $('#siguiente2').hide()
            $('#siguiente3').hide()
        }else{
            $('#update').show()
            $('#siguiente1').hide()
            $('#siguiente2').hide()
            $('#siguiente3').hide()
        }

    })

    $('#switch').change(function() {
       sw = $(this).prop('checked')

   })

    $('#viviendas').change(function () {
        obj = JSON.stringify({
            'id': parseInt(JSON.parse($('#viviendas').val())),
            '_xsrf': getCookie("_xsrf")
        })

        ruta = "domicilio_obtener";

        $.ajax({
            method: "POST",
            url: ruta,
            data: {_xsrf: getCookie("_xsrf"), object: obj},
            async: false
        }).done(function (response) {
            response = JSON.parse(response)
            console.log(response)
            append_input_vivienda('')

            var id_codigo = ''
            $("input.codigo").each(function() {
                id_codigo  = $(this).prop('id');
            });


            var id_ubicacion = ''
            $("input.ubicacion").each(function() {
                id_ubicacion  = $(this).prop('id');
            });

            var id_vivienda = ''
            $("input.fkvivienda").each(function() {
                id_vivienda = $(this).prop('id');
            });

            $('#' + id_vivienda).val(response.response.id)
            $('#' + id_vivienda).parent().addClass('focused')
            $('#' + id_codigo).val(response.response.codigo)
            $('#' + id_codigo).parent().addClass('focused')
            $('#' + id_ubicacion).val(response.response.ubicacion + " " + response.response.numero)
            $('#' + id_ubicacion).parent().addClass('focused')


        })

        $('#viviendas').val('')
        $('#viviendas').selectpicker('refresh')

    });

    function append_input_vivienda(id_in) {
        if(id_in === ''){
            id_gv++;
            id_in = id_gv;
        }

        $('#vivienda_div').append(
        '<div class="row">\
            <div class="col-sm-1 hidden">\
                <div class="input-group">\
                <input  id="idv'+id_in+'" class="form-control idvivienda vivienda readonly txta-own">\
                </div>\
            </div>\
            <div class="col-sm-1 hidden">\
                <div class="input-group">\
                <input  id="fkvivienda'+id_in+'" class="form-control fkvivienda vivienda txta-own">\
                </div>\
            </div>\
            <div class="col-sm-2">\
                <div class="form-line">\
                    <input id="codigo'+id_in+'" data-id="'+id_in+'" class="form-control codigo  txta-own"readonly>\
                </div>\
            </div>\
            <div class="col-sm-6 p-t-own">\
                <div  class="form-line">\
                    <input id="ubicacion'+id_in+'" data-id="'+id_in+'" class="form-control ubicacion  txta-own"readonly>\
                </div>\
            </div>\
            <div class="col-md-2 ">\
                <input id="b_'+id_in+'" type="checkbox" class="module chk-col-deep-purple vivienda" data-id="1" >\
                <label for="b_'+id_in+'"></label>\
            </div>\
            <div class="col-sm-2">\
                <button type="button" class="btn bg-red waves-effect white-own clear_vivienda" title="Eliminar">\
                    <i class="material-icons">clear</i>\
                </button>\
            </div>\
        </div>'
    )

        $('.clear_vivienda').last().click(function () {
            $(this).parent().parent().remove()
        })

        $('.codigo').focus(function () {
            $(this).parent().addClass('focused');
            current_input = $(this).prop('id');
        })

        $('.ubicacion').focus(function () {
            $(this).parent().addClass('focused');
            current_input = $(this).prop('id');
        })

    }

    function get_viviendas() {
        viviendas = []
        viviendas_inputs = $('.vivienda')
        cant_viviendas = 0

        for (i = 0; i < viviendas_inputs.length; i += 3) {
            h0 = viviendas_inputs[i].value
            h1 = viviendas_inputs[i + 1].value
            h2 = viviendas_inputs[i + 2].checked

            if (h2 == true){
                cant_viviendas = cant_viviendas + 1
            }


            viviendas.push((function add_invitado(h0, h1, h2) {

                if (h0 ==''){
                    return {
                        'fkdomicilio': h1,
                        'vivienda': h2

                    }

                }else{
                    return {
                    'id':h0,
                    'fkdomicilio': h1,
                    'vivienda': h2
                    }
                }


            })(
                h0,
                h1,
                h2))
        }

        if (cant_viviendas == 0){
            viviendas = []
        }


        return viviendas
    }

    $('#insertar_vehiculo').click(function () {
        console.log($('#idvehiculo').val())

        if($('#idvehiculo').val() == ""){

            append_input_vehiculos('')

            var id_placa = ''
            $("input.placa").each(function() {
                id_placa  = $(this).prop('id');
            });


            var id_fktipo = ''
            $("input.fktipo").each(function() {
                id_fktipo  = $(this).prop('id');
            });

            var id_tipo = ''
            $("input.tipo").each(function() {
                id_tipo  = $(this).prop('id');
            });
            
            var id_fkcolor = ''
            $("input.fkcolor").each(function() {
                id_fkcolor  = $(this).prop('id');
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

            var id_fknropase = ''
            $("input.fknropase").each(function() {
                id_fknropase  = $(this).prop('id');
            });

            var id_nropase = ''
            $("input.nropase").each(function() {
                id_nropase  = $(this).prop('id');
            });
        
            var id_vehiculo = ''
            $("input.id").each(function() {
                id_vehiculo = $(this).prop('id');
            });

            $('#' + id_vehiculo ).val('')
            $('#' + id_vehiculo ).parent().addClass('focused')
            $('#' + id_placa).val($('#placa').val())
            $('#' + id_placa).parent().addClass('focused')
            $('#' + id_fktipo).val($('#fktipo').val())
            $('#' + id_fktipo).parent().addClass('focused')
            $('#' + id_tipo).val($( "#fktipo option:selected" ).text())
            $('#' + id_tipo).parent().addClass('focused')
            $('#' + id_fkcolor).val($('#fkcolor').val())
            $('#' + id_fkcolor).parent().addClass('focused')
            $('#' + id_color).val($( "#fkcolor option:selected" ).text())
            $('#' + id_color).parent().addClass('focused')
            $('#' + id_fkmarca).val($('#fkmarca').val())
            $('#' + id_fkmarca).parent().addClass('focused')
            $('#' + id_marca).val($( "#fkmarca option:selected" ).text())
            $('#' + id_marca).parent().addClass('focused')
            $('#' + id_fkmodelo).val($('#fkmodelo').val())
            $('#' + id_fkmodelo).parent().addClass('focused')
            $('#' + id_modelo).val($( "#fkmodelo option:selected" ).text())
            $('#' + id_modelo).parent().addClass('focused')
            $('#' + id_fknropase).val($('#fknropase').val())
            $('#' + id_fknropase).parent().addClass('focused')
            $('#' + id_nropase).val($( "#fknropase option:selected" ).text())
            $('#' + id_nropase).parent().addClass('focused')
        
            $('#div_nuevo_vehiculo').hide()

        }else{
            var id = $('#idvehiculo').val()

            $('#id' + id ).val($('#idvehiculo').val())
            $('#id' + id ).parent().addClass('focused')
            $('#placa' + id ).val($('#placa').val())
            $('#placa' + id ).parent().addClass('focused')
            $('#fktipo' + id).val($('#fktipo').val())
            $('#fktipo' + id).parent().addClass('focused')
            $('#tipo' + id).val($("#fktipo option:selected").text())
            $('#tipo' + id).parent().addClass('focused')
            $('#fkcolor' + id).val($('#fkcolor').val())
            $('#fkcolor' + id).parent().addClass('focused')
            $('#color' + id).val($("#fkcolor option:selected").text())
            $('#color' + id).parent().addClass('focused')
            $('#fkmarca' + id).val($('#fkmarca').val())
            $('#fkmarca' + id).parent().addClass('focused')
            $('#marca' + id).val($("#fkmarca option:selected").text())
            $('#marca' + id).parent().addClass('focused')
            $('#fkmodelo' + id).val($('#fkmodelo').val())
            $('#fkmodelo' + id).parent().addClass('focused')
            $('#modelo' + id).val($("#fkmodelo option:selected").text())
            $('#modelo' + id).parent().addClass('focused')
            $('#fknropase' + id).val($('#fknropase').val())
            $('#fknropase' + id).parent().addClass('focused')
            $('#nropase' + id).val($("#fknropase option:selected").text())
            $('#nropase' + id).parent().addClass('focused')

            $('#div_nuevo_vehiculo').hide()

        }


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


                var id_fktipo = ''
                $("input.fktipo").each(function() {
                    id_fktipo  = $(this).prop('id');
                });

                var id_tipo = ''
                $("input.tipo").each(function() {
                    id_tipo  = $(this).prop('id');
                });

                var id_fkcolor = ''
                $("input.fkcolor").each(function() {
                    id_fkcolor  = $(this).prop('id');
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

                var id_fknropase = ''
                $("input.fknropase").each(function() {
                    id_fknropase  = $(this).prop('id');
                });

                var id_nropase = ''
                $("input.nropase").each(function() {
                    id_nropase  = $(this).prop('id');
                });

                var id_vehiculo = ''
                $("input.id").each(function() {
                    id_vehiculo = $(this).prop('id');
                });

                $('#' + id_vehiculo ).val(response.response.id)
                $('#' + id_vehiculo ).parent().addClass('focused')
                $('#' + id_placa).val(response.response.placa)
                $('#' + id_placa).parent().addClass('focused')
                $('#' + id_fktipo).val(response.response.fktipo)
                $('#' + id_fktipo).parent().addClass('focused')
                $('#' + id_tipo).val(response.response.tipo.nombre)
                $('#' + id_tipo).parent().addClass('focused')
                $('#' + id_fkcolor).val(response.response.fkcolor)
                $('#' + id_fkcolor).parent().addClass('focused')
                $('#' + id_color).val(response.response.color.nombre)
                $('#' + id_color).parent().addClass('focused')
                $('#' + id_fkmarca).val(response.response.fkmarca)
                $('#' + id_fkmarca).parent().addClass('focused')
                $('#' + id_marca).val(response.response.marca.nombre)
                $('#' + id_marca).parent().addClass('focused')
                $('#' + id_fkmodelo).val(response.response.fkmodelo)
                $('#' + id_fkmodelo).parent().addClass('focused')
                $('#' + id_modelo).val(response.response.modelo.nombre)
                $('#' + id_modelo).parent().addClass('focused')
                $('#' + id_fknropase).val(response.response.fknropase)
                $('#' + id_fknropase).parent().addClass('focused')
                $('#' + id_nropase).val(response.response.nropase.numero)
                $('#' + id_nropase).parent().addClass('focused')

            })

            $('#div_nuevo_vehiculo').hide()

        }else{
             $('#div_nuevo_vehiculo').show()
            // append_input_vehiculos('')
            $('#idvehiculo').val('')
             $('#fktipovehiculo').val('')
            $('#fktipovehiculo').selectpicker('refresh')
            $('#placa').val('')
            $('#fkcolor').val('')
            $('#fkmarca').val('')
            $('#fkmarca').selectpicker('refresh')
            $('#fkmodelo').val('')
            $('#fkmodelo').selectpicker('refresh')
            $('#fknropase').val('')
            $('#fknropase').selectpicker('refresh')
        }
        $('#vehiculos').val('')
        $('#vehiculos').selectpicker('refresh')

    });

    function get_vehiculos() {
        objeto = []
        objeto_inputs = $('.vehiculo')

        for (i = 0; i < objeto_inputs.length; i += 7) {
            h0 = objeto_inputs[i].value
            h1 = objeto_inputs[i + 1].value
            h2 = objeto_inputs[i + 2].value
            h3 = objeto_inputs[i + 3].value
            h4 = objeto_inputs[i + 4].value
            h5 = objeto_inputs[i + 5].value
            h6 = objeto_inputs[i + 6].value

            if(h1!=""){
                objeto.push((function add_objeto(h0, h1, h2,h3,h4,h5,h6) {

                return {
                    'id':h0,
                    'placa': h1,
                    'fktipo': h2,
                    'fkcolor': h3,
                    'fkmarca': h4,
                    'fkmodelo': h5,
                    'fknropase':h6
                    }

            })(
                h0,
                h1,
                h2,
                h3,
                h4,
                h5,
                h6))
            }



        }
        return objeto
    }

    function get_acceso() {
        objeto_acceso = []
        h0 = $('#fechai').val()
        h1 = $('#fechaf').val()
        h2 = sw

        console.log(h0)
        console.log(h1)
        console.log(h2)


        objeto_acceso.push((function add_objeto(h0, h1, h2) {

            return {
                'fechai':h0,
                'fechaf': h1,
                'estado': h2
                }

        })(
            h0,
            h1,
            h2))
        
        return objeto_acceso
    }


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
$('#expendido').selectpicker({
    size: 10,
    liveSearch: true,
    liveSearchPlaceholder: 'Buscar',
    title: 'Seleccione'
})

$('#fktipo').selectpicker({
    size: 10,
    liveSearch: true,
    liveSearchPlaceholder: 'Buscar',
    title: 'Seleccione'
})

$('#viviendas').selectpicker({
    size: 10,
    liveSearch: true,
    liveSearchPlaceholder: 'Buscar domicilio',
    title: 'Seleccione Domicilio'
})

$('#vehiculos').selectpicker({
    size: 10,
    liveSearch: true,
    liveSearchPlaceholder: 'Buscar vehiculo',
    title: 'Seleccione Vehiculo'
})

$('#agregar_vivienda').click(function () {

    $('#div_agregar_vivienda').hide()
    $('#div_buscar_vivienda').show()
    $('#div_cancelar_vivienda').show()

})

$('#cancelar_vivienda').click(function () {

    $('#div_buscar_vivienda').hide()
    $('#div_cancelar_vivienda').hide()
    $('#div_agregar_vivienda').show()

})

$('#agregar_vehiculo').click(function () {

    $('#div_agregar_vehiculo').hide()
    $('#div_buscar_vehiculo').show()
    $('#div_cancelar_vehiculo').show()

})

$('#cancelar_vehiculo').click(function () {

    $('#div_buscar_vehiculo').hide()
    $('#div_cancelar_vehiculo').hide()
    $('#div_nuevo_vehiculo').hide()
    $('#div_agregar_vehiculo').show()

})

$('#siguiente1').click(function () {
    document.getElementById("tab-vivienda").click();
    $('#body-residente').css("display", "none")
    $('#body-vivienda').css("display", "block")
    $('#body-vehiculo').css("display", "none")
    $('#body-usuario').css("display", "none")

    $('#siguiente1').hide()
    $('#siguiente2').show()
    $('#siguiente3').hide()


})

$('#siguiente2').click(function () {
    document.getElementById("tab-vehiculo").click();
    $('#body-residente').css("display", "none")
    $('#body-vivienda').css("display", "none")
    $('#body-vehiculo').css("display", "block")
    $('#body-usuario').css("display", "none")

    $('#siguiente1').hide()
    $('#siguiente2').hide()
    $('#siguiente3').show()


})

$('#siguiente3').click(function () {
    document.getElementById("tab-usuario").click();
    $('#body-residente').css("display", "none")
    $('#body-vivienda').css("display", "none")
    $('#body-vehiculo').css("display", "none")
    $('#body-usuario').css("display", "block")

    $('#siguiente1').hide()
    $('#siguiente2').hide()
    $('#siguiente3').hide()
    $('#insert').show()

})


$('#new').click(function () {
    accion = "nuevo"

    $('#codigo').val('')
    $('#nombre').val('')
    $('#apellidop').val('')
    $('#apellidom').val('')
    $('#correo').val('')

    $('#sexo').val('M')
    $('#sexo').selectpicker('refresh')
    $('#ci').val('')
    $('#expendido').val('')
    $('#expendido').selectpicker('refresh')
    $('#fechanacimiento').val('')
    $('#telefono').val('')
    $('#fktipo').val('')
    $('#fktipo').selectpicker('refresh')
    $('#fknropase_peatonal').val('')
    $('#b_fknropase').val('')
    $('#b_fknropase').selectpicker('refresh')

    $('#vivienda_div').empty()
    $('#vehiculo_div').empty()

    $('#foto').fileinput('clear');

    verif_inputs('')
    validationInputSelects("form")
    $('#div_foto').hide()
    $('#id_div').hide()
    $('#insert').hide()
    $('#update').hide()
    $('#div_nuevo_vehiculo').hide()
    $('#form').modal('show')
    $('#siguiente1').show()
    $('#siguiente2').hide()
    $('#siguiente3').hide()
    $('#siguiente4').hide()
    $('#div_username').hide()
    document.getElementById("tab-residente").click();
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

$('#insert').on('click',function (e) {
     e.preventDefault();
     notvalid = validationInputSelectsWithReturn("form");
    if (notvalid===false) {
        var data = new FormData($('#form_submit')[0]);
    
        objeto = JSON.stringify({
            'codigo': $('#codigo').val(),
            'nombre': $('#nombre').val(),
            'apellidop': $('#apellidop').val(),
            'apellidom': $('#apellidom').val(),
            'sexo': $('#sexo').val(),
            'ci': $('#ci').val(),
            'correo': $('#correo').val(),
            'expendido': $('#expendido').val(),
            'fechanacimiento': $('#fechanacimiento').val(),
            'telefono': $('#telefono').val(),
            'fktipo': $('#fktipo').val(),
            'fknropase': $('#fknropase_peatonal').val(),
            'b_fknropase': $('#b_fknropase').val(),
            'domicilios' : get_viviendas(),
            'vehiculos' : get_vehiculos(),
            'acceso' : get_acceso()

        })
        if(get_viviendas().length !=0){
            objeto_verificar = JSON.stringify({
                'username': $('#correo').val()

            })
             ajax_call_post("usuario_verificar_username", {
                _xsrf: getCookie("_xsrf"),
                object: objeto_verificar
            }, function (response) {
                if(response.success === true){
                    ruta = "residente_insert";
                    data.append('object', objeto)
                    data.append('_xsrf', getCookie("_xsrf"))

                    $.ajax({
                        url: ruta,
                        type: "post",
                        data: data,
                        contentType: false,
                        processData: false,
                        cache: false,
                        async: true
                    }).done(function (response) {
                        response = JSON.parse(response);
                        var data = [];
                        var id
                        var estadoresidente
                        for (var i = 0; i < Object.keys(response.response).length; i++) {
                            id = response['response'][i]['id']
                            estadoresidente = response['response'][i]['estado']
                            if(estadoresidente == true){
                                estadoresidente = "<input id='" + id + "' onClick='event.preventDefault();eliminar(this)' data-id='" + id + "' type='checkbox' class='chk-col-indigo 'checked disabled/><label for='" + id + "'></label>"
                                console.log(estadoresidente)
                            }else{
                                estadoresidente = "<input id='" + id + "' onClick='event.preventDefault();eliminar(this)' data-id='" + id + "' type='checkbox' class='chk-col-indigo ' disabled/><label for='" + id + "'></label>"
                                console.log(estadoresidente)
                            }

                            data.push( [
                                response['response'][i]['codigo'],
                                response['response'][i]['ci'],
                                response['response'][i]['fullname'],
                                response['response'][i]['telefono'],
                                estadoresidente,
                                "<button id='edit' onClick='editar(this)' data-json='" + id + "' type='button' class='btn bg-indigo waves-effect white-own waves-light edit' title='Editar'><i class='material-icons'>create</i></button>"
                            ]);
                        }

                        cargar_tabla(data)

                    })
                    showMessage("Insertado Correctamente", "success", "ok")
                    $('#form').modal('hide')



                }else{
                    swal(
                        'Correo en uso',
                        response.message,
                        'warning' )
                }
            });

        }else{
            swal(
            'Seleccion de Domicilio.',
            'Se debe seleccionar al menos un domicilio',
            'warning'
        )
        }


    } else {
        swal(
            'Error de datos.',
             notvalid,
            'warning'
        )
    }
})

$('#insert-importar').on('click',function (e) {
     e.preventDefault();

    var data = new FormData($('#importar-form')[0]);

    ruta = "residente_importar";
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


function editar(elemento){
    accion = "editar"
    obj = JSON.stringify({
        'id': parseInt(JSON.parse($(elemento).attr('data-json')))
    })
    ajax_call_get('residente_update', {
        _xsrf: getCookie("_xsrf"),
        object: obj
    }, function (response) {
       
        var self = response;
            $('#id').val(self.id)
            $('#codigo').val(self.codigo)
            $('#nombre').val(self.nombre)
            $('#apellidop').val(self.apellidop)
            $('#apellidom').val(self.apellidom)
            $('#sexo').val(self.sexo)
            $('#sexo').selectpicker('refresh')
            $('#ci').val(self.ci)
            $('#correo').val(self.correo)
            $('#expendido').val(self.expendido)
            $('#expendido').selectpicker('refresh')
            $('#fechanacimiento').val(self.fechanacimiento)
            $('#telefono').val(self.telefono)
            $('#fktipo').val(self.fktipo)
            $('#fktipo').selectpicker('refresh')
            $('#fknropase_peatonal').val(self.fknropase)
            $('#fechai').val(self.fechai)
            $('#fechaf').val(self.fechaf)
            $('#username').val(self.username)
            $('#switch').prop('checked', self.estadoacceso)
            sw = self.estadoacceso
            $('#b_fknropase').val('')
            $('#b_fknropase').selectpicker('refresh')

            console.log(self.fknropase)

        
            $('#fknropase_peatonal').val(self.idtarjeta)
            $('#fknropase_tarjeta').val(self.nrotarjeta)
            actual_fknropase = self.idtarjeta


            if (self.foto != "None" && self.foto != "") {
                document.getElementById("imagen_show_img").src = self.foto;
            } else {
                document.getElementById("imagen_show_img").src = "/resources/images/sinImagen.jpg";
            }


            $('#foto').fileinput('clear');

            $('#vivienda_div').empty()

            for (invi in self.domicilios) {

                append_input_vivienda(self.domicilios[invi]['id'])
                $('#idv' + self.domicilios[invi]['id']).val(self.domicilios[invi]['id'])
                $('#fkvivienda' + self.domicilios[invi]['id']).val(self.domicilios[invi]['fkdomicilio'])
                $('#codigo' + self.domicilios[invi]['id']).val(self.domicilios[invi]['codigo'])
                $('#ubicacion' + self.domicilios[invi]['id']).val(self.domicilios[invi]['nombre'])
                $('#b_' + self.domicilios[invi]['id']).prop('checked', self.domicilios[invi]['vivienda'])
            }

            $('#vehiculo_div').empty()
            console.log(self.vehiculos)
            for (vehi in self.vehiculos) {

                append_input_vehiculos(self.vehiculos[vehi]['id'])
                $('#id' + self.vehiculos[vehi]['id']).val(self.vehiculos[vehi]['id'])
                $('#placa' + self.vehiculos[vehi]['id']).val(self.vehiculos[vehi]['placa'])
                $('#fktipo' + self.vehiculos[vehi]['id']).val(self.vehiculos[vehi]['fktipo'])
                $('#tipo' + self.vehiculos[vehi]['id']).val(self.vehiculos[vehi]['nombretipo'])
                $('#fkcolor' + self.vehiculos[vehi]['id']).val(self.vehiculos[vehi]['fkcolor'])
                $('#color' + self.vehiculos[vehi]['id']).val(self.vehiculos[vehi]['nombrecolor'])
                $('#fkmarca' + self.vehiculos[vehi]['id']).val(self.vehiculos[vehi]['fkmarca'])
                $('#marca' + self.vehiculos[vehi]['id']).val(self.vehiculos[vehi]['nombremarca'])
                $('#fkmodelo' + self.vehiculos[vehi]['id']).val(self.vehiculos[vehi]['fkmodelo'])
                $('#modelo' + self.vehiculos[vehi]['id']).val(self.vehiculos[vehi]['nombremodelo'])
                $('#fknropase' + self.vehiculos[vehi]['id']).val(self.vehiculos[vehi]['fknropase'])
                $('#nropase' + self.vehiculos[vehi]['id']).val(self.vehiculos[vehi]['nropase'])

            }

            clean_form()
            verif_inputs('')
            validationInputSelects("form")
            $('#div_nuevo_vehiculo').hide()
            $('#div_foto').show()
            $('#id_div').hide()
            $('#insert').hide()
            $('#update').show()
            $('#form').modal('show')

            document.getElementById("tab-residente").click();
            $('#siguiente1').hide()
            $('#siguiente2').hide()
            $('#siguiente3').hide()
            $('#siguiente4').hide()


        $('.div_nropase_nombre').show()
        $('#div_username').show()
    })
    }

$('#update').on('click',function (e) {
     e.preventDefault();
      notvalid = validationInputSelectsWithReturn("form");
    if (notvalid===false) {
        var data = new FormData($('#form_submit')[0]);
        objeto = JSON.stringify({
             'id': $('#id').val(),
             'codigo': $('#codigo').val(),
             'nombre': $('#nombre').val(),
             'apellidop': $('#apellidop').val(),
             'apellidom': $('#apellidom').val(),
             'sexo': $('#sexo').val(),
             'ci': $('#ci').val(),
             'correo': $('#correo').val(),
             'expendido': $('#expendido').val(),
             'fechanacimiento': $('#fechanacimiento').val(),
             'telefono': $('#telefono').val(),
             'fktipo': $('#fktipo').val(),
             'fknropase': $('#fknropase_peatonal').val(),
             'b_fknropase': $('#b_fknropase').val(),
             'actual_fknropase': actual_fknropase,
             'domicilios' : get_viviendas(),
             'vehiculos' : get_vehiculos(),
             'acceso' : get_acceso()

        })
        ruta = "residente_update";
        data.append('object', objeto)
        data.append('_xsrf', getCookie("_xsrf"))

        $.ajax({
            url: ruta,
            type: "post",
            data: data,
            contentType: false,
            processData: false,
            cache: false,
            async: true
        }).done(function (response) {
            response = JSON.parse(response);
            var data = [];
            var id
            var estadoresidente
            for (var i = 0; i < Object.keys(response.response).length; i++) {
                id = response['response'][i]['id']
                estadoresidente = response['response'][i]['estado']
                if(estadoresidente == true){
                    estadoresidente = "<input id='" + id + "' data-id='" + id + "' type='checkbox' class='chk-col-indigo 'checked disabled/><label for='" + id + "'></label>" +" "+ "Habilitado"

                }else{
                    estadoresidente = "<input id='" + id + "'data-id='" + id + "' type='checkbox' class='chk-col-indigo ' disabled/><label for='" + id + "'></label>" + " " + "Deshabilitado"

                }

                data.push( [
                    response['response'][i]['codigo'],
                    response['response'][i]['ci'],
                    response['response'][i]['fullname'],
                    response['response'][i]['telefono'],
                    estadoresidente,
                    "<button id='edit' onClick='editar(this)' data-json='" + id + "' type='button' class='btn bg-indigo waves-effect white-own waves-light edit' title='Editar'><i class='material-icons'>create</i></button>"
                ]);
            }

            cargar_tabla(data)
        })
        showMessage("IModificado Correctamente", "success", "ok")
        $('#form').modal('hide')
    } else {
        swal(
            'Error de datos.',
             notvalid,
            'warning'
        )
    }

})
reload_form()

    $('.delete').click(function (e) {
        console.log("delete")
        e.preventDefault()
        cb_delete = this
        b = $(this).prop('checked')
        if (!b) {
            cb_title = "Deshabilitar Residente"

        } else {
            cb_title = "Habilitar Residente"
        }
        swal({
            text: cb_title,
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

            ajax_call("residente_delete", {
                object: objeto,
                _xsrf: getCookie("_xsrf")
            }, null, function () {
                setTimeout(function () {
                    window.location = main_route
                }, 2000);
            })
            $('#form').modal('hide')
        })
    })

function eliminar(elemento){
    cb_delete = elemento
    b = $(elemento).prop('checked')
    if (!b) {
        cb_title = "¿Deshabilitar Residente?"

    } else {
        cb_title = "¿Habilitar Residente?"
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
        ajax_call('residente_delete', {
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