main_route = '/registros_c'
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
            // console.log(refrescar)
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


reload_form()


$('#filtrar').click(function () {
    //document.getElementById("filtrar").disabled = true
    obj = JSON.stringify({
        'fechainicio': $('#fechai').val(),
        'fechafin': $('#fechaf').val(),
        '_xsrf': getCookie("_xsrf")
    })
    ruta = "registros_c_filtrar";
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