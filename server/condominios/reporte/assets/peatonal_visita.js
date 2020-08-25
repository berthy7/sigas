function preparar_datos_peatonal_visita(datos){
    
    var data = [];
    for (var i = 0; i < Object.keys(datos).length; i++) {
        var id
        var fechai
        var fechaf

    
        var domicilio
        var autorizacion
        var nropase

        
        id = datos[i].id
        if (datos[i].fechai !="None"){
            fechai = datos[i]['fechai']
        }else{
            fechai= '-----'
        }

        if (datos[i].fechaf !="None"){
            fechaf = datos[i]['fechaf']

        }else{
            fechaf= '-----'
        }
        
        if (datos[i].fkdomicilio !="None"){
            domicilio = datos[i]['domicilio'].ubicacion + ' ' +datos[i]['domicilio'].numero
        }else if (datos[i].fkareasocial !="None"){
            domicilio= datos[i]['areasocial'].nombre
        }else{
            domicilio= '-----'
        }
        
        if (datos[i].fkautorizacion !="None"){
            autorizacion = datos[i]['autorizacion'].nombre
        }else{
            autorizacion= '-----'
        }

        if (datos[i].fknropase !="None"){
            nropase = datos[i]['nropase'].numero
        }else{
            nropase= '-----'
        }
        

        data.push( [
            id,
            fechai,
            fechaf,
            datos[i]['tipodocumento'].nombre,
            datos[i]['invitado'].ci,
            datos[i]['invitado'].apellidop + ' ' + datos[i]['invitado'].apellidom + ' '+datos[i]['invitado'].nombre,
            domicilio,
            autorizacion,
            nropase,
            datos[i]['tipopase'].nombre,
            datos[i].observacion
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