function aleatorio(piso,techo){
	return Math.floor(Math.random() * (techo - piso + 1)) + piso;
}

function ProfesorMalo(x,y){
	this.img = $("#profesor-malo")[0];		
	this.x = aleatorio(0,620);
	this.y = aleatorio(100,330);
	this.velocidad = 0;
	this.velocidad2 = 0;
	while(this.velocidad == 0 && this.velocidad2 == 0){
		this.velocidad=aleatorio(-5,5);
		this.velocidad2=aleatorio(-3,3);
	}
			
	this.dibujar = function(ctx){
		var img = this.img;
		ctx.drawImage(img,this.x,this.y);
	}
	
	this.actualizar = function(){
		this.x += this.velocidad;
		this.y += this.velocidad2;
		this.x = (640 + this.x)%640;
		this.y = (480 + this.y)%480;
	}
}
