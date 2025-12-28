$(window).load(function ()
{

	$("#mapa").svg({onClick: doFer});
	//var svg = $('#arc').svg('get'); 
	//svg.circle(130, 75, 50, {fill: 'none', stroke: 'red', strokeWidth: 3});
	function doFer(svg) 
	{ 
	    svg.circle(75, 75, 50, 
	        {fill: 'none', stroke: 'red', strokeWidth: 3}); 
	    var g = svg.group({stroke: 'black', strokeWidth: 2}); 
	    svg.line(g, 15, 75, 135, 75); 
	    svg.line(g, 75, 15, 75, 135); 
	    console.log("ejecuto funcion");
	    var g = svg.getElementById('circle');
	    svg.change(g, {fill:'blue'})
	}

	$("circle").click(function()
	{
		console.log("Estoy encima de un circulo");
	}
	);
	$("#arc").click(function()
	{
		console.log("Estoy encima de un path");
	}
	);
	
	
}
);