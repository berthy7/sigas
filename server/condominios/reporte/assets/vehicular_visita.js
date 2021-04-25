function preparar_datos_vehicular_visita(response){

    var data = [];
    for (var i = 0; i < Object.keys(response.response).length; i++) {

        data.push( [
            response['response'][i].id,
            response['response'][i].fechai,
            response['response'][i].fechaf,
            response['response'][i].documento,
            response['response'][i].ci_invitado,
            response['response'][i].nombre_invitado,
            response['response'][i].nombre_conductor,
            response['response'][i].cantpasajeros,
            response['response'][i].placa,
            response['response'][i].tipo,
            response['response'][i].marca,
            response['response'][i].modelo,
            response['response'][i].color,
            response['response'][i].destino,
            response['response'][i].autorizacion,
            response['response'][i].nropase,
            response['response'][i].tipopase,
            response['response'][i].observacion
        ]);

        console.log(i)
    }

    console.log("cargar tabla vehicular visita")

    cargar_tabla_vehicular_visita(data)
}

// function preparar_datos_vehicular_visita(datos){
//     console.log("preparar datos")
//
//     console.log(datos)
//
//     var data = [];
//     for (var i = 0; i < Object.keys(datos['response']).length; i++) {
//
//         data.push( [
//             datos['response'][i]['id'],
//             datos['response'][i]['fechai'],
//             datos['response'][i]['fechaf'],
//             datos['response'][i]['tipodocumento'],
//             datos['response'][i]['ci_invitado'],
//             datos['response'][i]['nombre_invitado'],
//             datos['response'][i]['nombre_conductor'],
//             datos['response'][i]['cantpasajeros'],
//             datos['response'][i]['placa'],
//             datos['response'][i]['tipo_vehiculo'],
//             datos['response'][i]['marca'],
//             datos['response'][i]['modelo'],
//             datos['response'][i]['color'],
//             datos['response'][i]['destino'],
//             datos['response'][i]['autorizacion'],
//             datos['response'][i]['nropase'],
//             datos['response'][i]['tipopase'],
//             datos['response'][i]['observacion']
//         ]);
//
//         console.log(i)
//     }
//
//     console.log("cargar tabla vehicular visita")
//
//     cargar_tabla_vehicular_visita(data)
// }

// function preparar_datos_vehicular_visita(datos){
//     console.log("preparar datos")
//
//     console.log(datos)
//
//     var data = [];
//     for (var i = 0; i < datos; i++) {
//
//         // data.push( [
//         //     datos['response'][i]['id'],
//         //     datos['response'][i]['fechai'],
//         //     datos['response'][i]['fechaf'],
//         //     datos['response'][i]['tipodocumento'],
//         //     datos['response'][i]['ci_invitado'],
//         //     datos['response'][i]['nombre_invitado'],
//         //     datos['response'][i]['nombre_conductor'],
//         //     datos['response'][i]['cantpasajeros'],
//         //     datos['response'][i]['placa'],
//         //     datos['response'][i]['tipo_vehiculo'],
//         //     datos['response'][i]['marca'],
//         //     datos['response'][i]['modelo'],
//         //     datos['response'][i]['color'],
//         //     datos['response'][i]['destino'],
//         //     datos['response'][i]['autorizacion'],
//         //     datos['response'][i]['nropase'],
//         //     datos['response'][i]['tipopase'],
//         //     datos['response'][i]['observacion']
//         // ]);
//
//         console.log(i)
//     }
//
//     console.log("cargar tabla vehicular visita")
//
//     // cargar_tabla_vehicular_visita(data)
// }


function cargar_tabla_vehicular_visita(data){
    if ( $.fn.DataTable.isDataTable( '#data_vehicular_visita' ) ) {
        var table = $('#data_vehicular_visita').DataTable();
        table.destroy();
    }

    $('#data_vehicular_visita').DataTable({
        data:           data,
        deferRender:    true,
        scrollCollapse: true,
        scroller:       true,

        dom: "Bfrtip" ,
        buttons: [
            {  extend : 'excelHtml5',
               exportOptions : { columns : [0, 1, 2, 3, 4, 5 ,6 ,7,8,9,10,11,12,13,14,15,16,17]},
                sheetName: 'Reporte Control y Registro',
               title: 'Registro Vehicular Visita'  },
            {  extend : 'pdfHtml5',
                orientation: 'landscape',
               customize: function(doc) {
                    doc.styles.tableBodyEven.alignment = 'center';
                    doc.styles.tableBodyOdd.alignment = 'center';
               },
               exportOptions : {
                    columns : [0, 1, 2, 3, 4, 5 ,6 ,7,8,9,10,11,12,13,14,15,16,17]
                },
               title: 'Control y Registro'
            }
        ],
        initComplete: function () {


        },
        "order": [[ 0, "desc" ]],
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
