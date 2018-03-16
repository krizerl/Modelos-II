import random

'''Funcion que retorna el valor de una carta teniendo en cuenta el puntaje acumulado'''
def valorCarta(carta, acumulado):
    if(carta[0]=="J" or carta[0]=="Q" or carta[0]=="K"):
        return 10
    if carta[0]=="A" and acumulado+11>21:
        return 1
    elif carta[0]=="A" and acumulado+11<=21:
        return 11
    else:
        return int(carta[0])

'''Funcion que retorna el valor de una mano de cartas'''
def contarMano(listaDeCartas, acumulado):
    if len(listaDeCartas)==1:
        return valorCarta(listaDeCartas[0], acumulado)
    else:
        return valorCarta(listaDeCartas[0], acumulado)+contarMano(listaDeCartas[1:],acumulado+valorCarta(listaDeCartas[0],acumulado))

'''Funcion que retorna una baraja de cartas desordenada'''
def retornarCartas():
    return random.sample([(x,y) for x in [2,3,4,5,6,7,8,9,10,"J","Q","K","A"] for y in ["Diamantes","Corazones","Picas","Treboles"]],52)

'''Funcion principal que maneja el juego'''
def juego(cartasJugador, cartasCasa, contador):
    if(contador==1):
        print "JUGADOR________________________________________"
        print "\nCartas Casa: Carta Oculta "+str(cartasCasa[1])
        print "\nSus cartas son "+str(cartasJugador)
        print "\nPuntaje: "+str(contarMano(cartasJugador,0))
        if(contarMano(cartasJugador,0)<21):
            if(input("Desea otra carta? 1.Tomar otra carta 2.Plantar")==1):
                juego(cartasJugador+retornarCartas()[:1],cartasCasa,contador)
            else:
                juego(cartasJugador,cartasCasa,2)
        elif(contarMano(cartasJugador,0)==21):
            juego(cartasJugador,cartasCasa,2)
        else:
            print "La casa gana"
    elif(contador==2):
        print "CASA___________________________________________"
        print "\nSus cartas son: "+str(cartasJugador)
        print "\nPuntaje: "+str(contarMano(cartasJugador,0))
        print "\nCartas Casa: "+str(cartasCasa)
        print "\nPuntaje: "+str(contarMano(cartasCasa,0))
        if(contarMano(cartasCasa,0)<21):
            if(contarMano(cartasCasa,0)<contarMano(cartasJugador,0)):
                juego(cartasJugador,cartasCasa+retornarCartas()[:1],contador)
            else:
                juego(cartasJugador,cartasCasa,3)
        elif(contarMano(cartasCasa,0)==21):
            print "La casa gana"
        else:
            print "El jugador gana"
    else:
        print "_______________________________________________"
        if(contarMano(cartasCasa,0)<contarMano(cartasJugador,0)):
            print "El jugador gana"
        elif(contarMano(cartasCasa,0)>=contarMano(cartasJugador,0)):
            print "La casa gana"

juego(retornarCartas()[:2], retornarCartas()[:2],1)
