main_route = '/registros'
var refrescar = false;


$(document).ready(function () {
   auxiliar_method()
});

$(document).ajaxStart(function () { });

$(document).ajaxStop(function () {
    $.Toast.hideToast();
});

var fechahoy = new Date();
var hoy = fechahoy.getDate()+"/"+(fechahoy.getMonth()+1) +"/"+fechahoy.getFullYear()


document.getElementById("fechai").value=hoy
document.getElementById("fechaf").value=hoy

function auxiliar_method() {
    //main_method()
    //setTimeout(auxiliar_method, 10000)
    setInterval(function(){
        if($("#form").is(":visible")){
            console.log("actualizar desactivado")
        }else{
            console.log(refrescar)
            if(refrescar == false){
                window.location = main_route
            }
        }
    }, 10000);
}

$('#switch_refrescar').change(function() {
   var sw_refrescar = $(this).prop('checked')

    if(sw_refrescar){
       refrescar = true;

    }else{
        refrescar = false;
    }

})

function activar_alarma(id_registro) {
    console.log("activar alarma")
    refrescar = true;
    //main_method()
    var sw_alarma = 0;
        setInterval(function(){
        if(sw_alarma == 0){
            document.getElementById("imagen_alarma").src = '/resources/images/imagen_alarma.jpg';
            sw_alarma = 1;
        }else{
            document.getElementById("imagen_alarma").src = '/resources/images/imagen_alarma_blanco.jpg';
            sw_alarma = 0;
        }

    }, 700);

    setTimeout(function () {
        document.getElementById("imagen_alarma").src = '';
        console.log("apagar alarma")

        objeto = JSON.stringify({
            'id_registro': id_registro

        })

        ajax_call('registros_alerta', {
            object: objeto,
            _xsrf: getCookie("_xsrf")
        }, null, function () {

        })


        refrescar = false;

    },10000);
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
        createdRow: function( row, data, dataIndex ) {
            // agregar clase con css
            if(data[2] == "Alarma"){
                $(row).addClass('bg-alarm');
            }
            
        },

        dom: "Bfrtip" ,
        buttons: [
            {  extend : 'excelHtml5',
               exportOptions : { columns : [0, 1, 2, 3, 4, 5 ,6 ,7,8]},
                sheetName: 'Reporte registros dispostivos',
               title: 'Registros dispositivos'  },
            {  extend : 'pdfHtml5',
                orientation: 'landscape',
               customize: function(doc) {
                    doc.styles.tableBodyEven.alignment = 'center';
                    doc.styles.tableBodyOdd.alignment = 'center';
               },
               exportOptions : {
                    columns : [0, 1, 2, 3, 4, 5 ,6 ,7,8]
                },
               title: 'Registros dispositivos'
            }
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


$('#new').click(function () {
    $('#nombre').val('')

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
            'nombre': $('#nombre').val()
        })
        ajax_call('registros_insert', {
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
    ajax_call_get('registros_update', {
        _xsrf: getCookie("_xsrf"),
        object: obj
    }, function (response) {
        var self = response;
        $('#id').val(self.id)
        $('#nombre').val(self.nombre)

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
            'nombre': $('#nombre').val()
        })
        ajax_call('registros_update', {
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
        cb_title = "¿Deshabilitar  Marca?"

    } else {
        cb_title = "¿Habilitar  Marca?"
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
        ajax_call('registros_delete', {
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
    // $("#rgm-loader").show();
    //document.getElementById("filtrar").disabled = true
    obj = JSON.stringify({
        'fechainicio': $('#fechai').val(),
        'fechafin': $('#fechaf').val(),
        '_xsrf': getCookie("_xsrf")
    })
    ruta = "registros_filtrar";
    $.ajax({
        method: "POST",
        url: ruta,
        data: {_xsrf: getCookie("_xsrf"), object: obj},
        async: true,
        beforeSend: function () {
           $("#rproc-loader").fadeIn(800);
           $("#new").hide();
        },
        success: function () {
           $("#rproc-loader").fadeOut(800);
           $("#new").show();
        }

    }).done(function (response) {
        response = JSON.parse(response)

        var data = [];
        for (var i = 0; i < Object.keys(response.response).length; i++) {

            data.push( [
                response['response'][i]["id"],
                response['response'][i]["tarjeta"],
                response['response'][i]["codigo"],
                response['response'][i]["dia"],
                response['response'][i]["mes"],
                response['response'][i]["año"],
                response['response'][i]["hora"],
                response['response'][i]['dispositivo'],
                response['response'][i]["cerradura"],
            ]);
        }

        cargar_tabla(data)
    })
});

validationKeyup("form")
validationSelectChange("form")