var jugando;

$(document).ready(inicio);
$(document).keydown(capturaTeclado);

function inicio(){
	jugando = true;
	miCanvas = $("#mi_canvas")[0];
	contexto = miCanvas.getContext("2d");
	buffer = document.createElement("canvas");
	est = new Estudiante();
	pm = [new ProfesorMalo(), new ProfesorMalo(),
			new ProfesorMalo(), new ProfesorMalo(),
			new ProfesorMalo()];

	pb = [new ProfesorBueno(), new ProfesorBueno(), 
			new ProfesorBueno(), new ProfesorBueno(), 
			new ProfesorBueno()];
	run();	
	
	$('#instrucciones').click(function(){
        $('#popup').fadeIn('slow');
        $('.popup-overlay').fadeIn('slow');
        $('.popup-overlay').height($(window).height());
        return false;
    });
    
    $('#close').click(function(){
        $('#popup').fadeOut('slow');
        $('.popup-overlay').fadeOut('slow');
        return false;
    });
    
    $("#iniciar").click(function(){	
		if(jugando==false)
			inicio();	
	});
}

function capturaTeclado(event){
	if(event.which==38 || event.which==87)
		est.actualizar('arriba');
	if(event.which==40 || event.which==83)
		est.actualizar('abajo');
	if(event.which==39 || event.which==68)
		est.actualizar('derecha');
	if(event.which==37 || event.which==65)
		est.actualizar('izquierda');
	
}

function run(){ 
	buffer.width = miCanvas.width;
	buffer.height = miCanvas.height;
	contextoBuffer = buffer.getContext("2d");
		 
	if(jugando){  
		contextoBuffer.clearRect(0,0,buffer.width,buffer.height);

		est.dibujar(contextoBuffer);
		for(i=0;i<pm.length;i++){
			pm[i].dibujar(contextoBuffer);
			pm[i].actualizar();
			if(est.colision(pm[i].x,pm[i].y)){
				est.sprite = 2;
				est.vida--;
				est.puntos--;
			}
		}
		for(i=0;i<pb.length;i++){
			pb[i].dibujar(contextoBuffer);
			pb[i].actualizar();
			if(est.colision(pb[i].x, pb[i].y)){
				est.sprite = 2;
				est.puntos++;
			}
		}
		
		if(est.vida <= 0)
			jugando = false;
		
		contexto.clearRect(0,0,miCanvas.width,miCanvas.height);
		contexto.drawImage(buffer, 0, 0);
		setTimeout("run()",20);
		
	}
	else{
		contextoBuffer.clearRect(0,0,buffer.width,buffer.height);
		contextoBuffer.fillStyle = "#ffffff";
		est.sprite = 3;
		est.vida = 0;
		est.dibujar(contextoBuffer);
		contextoBuffer.font = "50px sans-serif";
		contextoBuffer.fillText("GAMEOVER", 300, 440);
		contextoBuffer.fillStyle = "#ff0000";
		contextoBuffer.font = "15px sans-serif";
		contextoBuffer.fillText("try again", 550, 460);
		contexto.clearRect(0,0,miCanvas.width,miCanvas.height);
		contexto.drawImage(buffer, 0, 0);
	}
	
}


