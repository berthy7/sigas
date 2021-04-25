function preparar_datos_peatonal_visita(response){
    
    var data = [];
    for (var i = 0; i < Object.keys(response.response).length; i++) {


        data.push( [
            response['response'][i].id,
            response['response'][i].fechai,
            response['response'][i].fechaf,
            response['response'][i].documento,
            response['response'][i].ci_invitado,
            response['response'][i].nombre_invitado,
            response['response'][i].destino,
            response['response'][i].autorizacion,
            response['response'][i].nropase,
            response['response'][i].tipopase,
            response['response'][i].observacion
        ]);
    }

    cargar_tabla_peatonal_visita(data)
}


function cargar_tabla_peatonal_visita(data){
    if ( $.fn.DataTable.isDataTable( '#data_peatonal_visita' ) ) {
        var table = $('#data_peatonal_visita').DataTable();
        table.destroy();
    }

    $('#data_peatonal_visita').DataTable({
        data:           data,
        deferRender:    true,
        scrollCollapse: true,
        scroller:       true,

        dom: "Bfrtip" ,
        buttons: [
            {  extend : 'excelHtml5',
               exportOptions : { columns : [0, 1, 2, 3, 4, 5 ,6 ,7,8,9,10]},
                sheetName: 'Reporte Control y Registro',
               title: 'Control y Registro Peatonal Visita'  },
            {  extend : 'pdfHtml5',
                orientation: 'landscape',
               customize: function(doc) {
                    doc.styles.tableBodyEven.alignment = 'center';
                    doc.styles.tableBodyOdd.alignment = 'center';
               },
               exportOptions : {
                    columns : [0, 1, 2, 3, 4, 5 ,6 ,7,8,9,10]
                },
               title: 'Control y Registro'
            }
        ],
        initComplete: function () {


        },
        "order": [[ 1, "desc" ]],
        language : {
            'url': '/resources/js/spanish.json',
        },
        "pageLength": 5,
        fixedHeader: {
            header: true,
            headerOffset: $('.navbar-header').outerHeight()
        },
        paging: true,
        select: true
    });


}