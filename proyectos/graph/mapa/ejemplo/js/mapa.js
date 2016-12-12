$(document).ready( function() 
{	
    $( "#calendario" ).datepicker(
    {  
    	minDate: new Date(2014, 0, 1),
        maxDate: -1,

		onSelect: function()
			{
				var date = $(this).datepicker('getDate'),
		            day  = date.getDate(),  
		            month = date.getMonth() + 1,              
		            year =  date.getFullYear();
		        if (day < 10)
		        	day = '0'+day;
		        if (month<10)
		        	month = '0'+month;
			    $("#calendario_fecha").text('Fecha: '+year + '-' + month + '-' + day);
			    //console.log("hey!");
			    testConsola(year);
			    $( "svg" ).remove();
			    cargarMapa('data/conexiones'+year + '-' + month + '-' + day+'.csv');
			}
    }
    );        
}
);

function testConsola(texto)
{
	console.log("El texto es: "+texto)
};

function cargarMapa(fichero_externo)
{
	var width = 960,
    height = 500;

	var projection = d3.geo.mercator()
    //España
    /*
    .center([-5,40])
    .scale(17000)
    .rotate([0,0]);
    */
    //mundo
    
    .center([-2, 40 ])
    .scale(4700)
    .rotate([0,0]);
    

console.log(fichero_externo);
//if (fichero_externo!='')
fichero=fichero_externo;

var svg = d3.select("#mapa").append("svg").attr("width", width).attr("height", height);

var path = d3.geo.path()
    .projection(projection);

var g = svg.append("g");

//Cargo en el array dataConexiones los datos del fichero con el nombre de los sitios y sus coordenadas
var dataConexiones = [];
d3.csv("sitios.csv", function(error, data) 
{
  dataConexiones = data.map(function(d) { return [ d.Nombre, d.Lat, d.Lon ]; });    
});

// Cargo el fichero con la topologia de todo el mundo y la muestro en SVG
d3.json("world-110m2.json", function(error, topology) {
    g.selectAll("path")
      .data(topojson.object(topology, topology.objects.countries)
          .geometries)
    .enter()
      .append("path")
      .attr("d", path)

    

    //Ahora miro en el fichero de conexiones cuales son las ciudades que estan enlazadas
    d3.csv(fichero, function(error, data) 
    {

      //Cargo en el array dataset todos los Origen,Destino de manera que:
      //dataset[x][0] <- origen
      //dataset[x][1] <- destino
      var dataset = [];
      for (var i=0; i<data.length; i++) {          
        dataset = data.map(function(d) { return [ d.Origen, d.Destino, d.Total ]; });          
      }

      //Recorro la tabla con todos los datos Origen,Destino, y busco el nombre del origen y destino en el array de coordenadas de sitios
      //a traves de la funcion buscarCoordenadas
      for (var j=0; j< dataset.length; j++)
      {
        //console.log(dataset[j][0],dataset[j][1]);
        var coorOrigen = buscarCoordenada(dataset[j][0]);
        var coorDestino = buscarCoordenada(dataset[j][1]);
        //console.log(coorOrigen[0],coorOrigen[1],coorDestino[0],coorDestino[1]);
         
        g.append("path")          
          // A datum hay que pasarle el extremo origen y destino para que lo pinte
          .datum({
                  type: "LineString", 
                  coordinates: [[coorOrigen[0], coorOrigen[1]], [coorDestino[0], coorDestino[1]]]
                })
          
          .attr("class", "arc")
          .attr("id", function(d) 
          {
                var oridest = dataset[j][2] + "  -  " + dataset[j][0] + "  -  " + dataset[j][1];
                //console.log(d.Nombre);
                 return oridest;
          })
          .attr("d", path)
          //Metodo para poner el nombre del Origen->Destino y numero de conex ciudades sobre el DIV correspondiente
          .on('mouseover', function(d)
          {
            var origendestino = d3.select(this);
            //nodeSelection.select("r").style({opacity:'1.0'});
            console.log(origendestino.attr("id"));
            $("#orides_info").text(origendestino.attr("id"));
            d3.select(this).attr("class", "arc2");
            
          })
          .on('mouseout', function(d)
          {
            
            //nodeSelection.select("r").style({opacity:'1.0'});
            d3.select(this).attr("class", "arc");
            
          });
          
      } //Fin del for que recorre la tabla Origen,Destino
    

    //Dentro de la propia funcion utilizo el fichero de ciudades para pintarlas sobre el mapa
    for (var j=0; j< dataset.length; j++)
      {
        //console.log(dataset[j][0],dataset[j][1]);
        var coorOrigen = buscarCoordenada(dataset[j][0]);
        var coorDestino = buscarCoordenada(dataset[j][1]);
        //console.log(coorOrigen[0],coorOrigen[1],coorDestino[0],coorDestino[1]);
        g.append("circle")     
          .attr("cx", function(d) {
                   return projection([coorOrigen[0], coorOrigen[1]])[0];
           })
          .attr("cy", function(d) {
                   return projection([coorOrigen[0], coorOrigen[1]])[1];
           })
          .style("fill", "red")        
          .attr("r", 5)
          .attr("id", function(d) {

                  //console.log(d.Nombre);
                   return dataset[j][0];
           })
          //Metodo para poner el nombre de las ciudades sobre el DIV correspondiente
          .on('mouseover', function(d)
          {
            var ciudad = d3.select(this);
            
            console.log(ciudad.attr("id"));

            $("#dominio_info").text(ciudad.attr("id"));
            d3.select(this).attr("r",15);
            d3.select(this).style("fill", "red");
          })
          .on('mouseout', function(d)
            {
              
              //nodeSelection.select("r").style({opacity:'1.0'});
              d3.select(this).attr("r",5);
              d3.select(this).style("fill", "red");
            });
        g.append("circle")     
            .attr("cx", function(d) {
                     return projection([coorDestino[0], coorDestino[1]])[0];
             })
            .attr("cy", function(d) {
                     return projection([coorDestino[0], coorDestino[1]])[1];
             })
            .style("fill", "red")        
            .attr("r", 5)
            .attr("id", function(d) {

                    //console.log(d.Nombre);
                     return dataset[j][1];
             })
            //Metodo para poner el nombre de las ciudades sobre el DIV correspondiente
            .on('mouseover', function(d)
            {
              var ciudad = d3.select(this);
              
              console.log(ciudad.attr("id"));

              $("#dominio_info").text(ciudad.attr("id"));
              d3.select(this).attr("r",15);
              d3.select(this).style("fill", "red");
            })
            .on('mouseout', function(d)
              {
                
                //nodeSelection.select("r").style({opacity:'1.0'});
                d3.select(this).attr("r",5);
                d3.select(this).style("fill", "red");
              });
        
        
      }//fin del for
    
    }); // Fin de la funcion d3 que recorre el fichero CSV "conexiones.csv"
}); //Fin de la funcion d3 que recorre el JSON "world-110m2.json" con los datos de la cuidades


//Funcion auxiliar que se encarga de buscar una CIUDAD en la tabla "dataConexiones" que ya tenemos cargada con los datos de las ciudades
var buscarCoordenada = function (ciudad)
{
  busqueda = [];
  for (var i=0; i<dataConexiones.length; i++)
  {
    if (dataConexiones[i][0] === ciudad)
    {
      //console.log("He encontrado: "+dataConexiones[i][0]+ " en "+ dataConexiones[i][1] +" "+dataConexiones[i][2]);
      busqueda = [dataConexiones[i][2],dataConexiones[i][1]];
    }    
  }
  return busqueda;  
};

var zoom = d3.behavior.zoom()
    .on("zoom",function() 
    {
        g.attr("transform","translate("+ d3.event.translate.join(",")+")scale("+d3.event.scale+")");
        g.selectAll("path")  
            .attr("d", path.projection(projection));         
    });

svg.call(zoom)
}

