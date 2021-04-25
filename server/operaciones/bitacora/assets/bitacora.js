main_route = '/bitacora'

$(document).ready( function () {

    var fechahoy = new Date();
    var hoy = fechahoy.getDate()+"/"+(fechahoy.getMonth()+1) +"/"+fechahoy.getFullYear()

    document.getElementById("fechai").value=hoy
    document.getElementById("fechaf").value=hoy

    $('#idusuario').val(0)
    $('#idusuario').selectpicker('refresh')

});

$('#idusuario').selectpicker({
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
            {  extend : 'excelHtml5',
               exportOptions : { columns : [0, 1, 2, 3, 4]},
                sheetName: 'Reporte Bitacora',
               title: 'Bitacora'  },
            {  extend : 'pdfHtml5',
                orientation: 'landscape',
               customize: function(doc) {
                    doc.styles.tableBodyEven.alignment = 'center';
                    doc.styles.tableBodyOdd.alignment = 'center';
               },
               exportOptions : {
                    columns : [0, 1, 2, 3, 4]
                },
               title: 'Bitacora'
            }
        ],
        initComplete: function () {


        },
        "order": [[ 0, "desc" ]],
        language : {
            'url': '/resources/js/spanish.json',
        },
        "pageLength": 20,
        fixedHeader: {
            header: true,
            headerOffset: $('.navbar-header').outerHeight()
        },
        paging: true,
        select: true
    });


}

function actualizar_tabla(response){

    var data = [];
    var usuario;


    for (var i = 0; i < Object.keys(response.response).length; i++) {

            if(response['response'][i].fkusuario != "None"){
                usuario = response['response'][i].usuario.fullname
            }else{
                usuario = '-----'
            }

            data.push( [
                response['response'][i].id,
                usuario,
                response['response'][i].accion,
                response['response'][i].ip,
                response['response'][i].tabla,
                response['response'][i].identificador,
                response['response'][i].fecha

            ]);
    }

    cargar_tabla(data)

}

$('#filtrar').click(function () {
    $("#rgm-loader").show();
    //document.getElementById("filtrar").disabled = true
    obj = JSON.stringify({
        'fechainicio': $('#fechai').val(),
        'fechafin': $('#fechaf').val(),
        'idusuario': $('#idusuario').val(),
        '_xsrf': getCookie("_xsrf")
    })
    ruta = "bitacora_filtrar";
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
        actualizar_tabla(response)

    })
});
