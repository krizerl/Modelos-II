class Arbol:
    def __init__ (self,val,izq=None,der=None):
        self.valor=val
        self.izquierda=izq
        self.derecha=der

def buscar( valor, arbol):
    if arbol.valor==None:
        return False
    if arbol.valor==valor:
        return True
    
    if  valor>arbol.valor:
        return buscar(valor,arbol.derecha)
    return buscar(valor,arbol.izquierda)

def printArbo(arbol):
    if(arbol==None):
        return []
    else:
        return printArbo(arbol.izquierda)+[arbol.valor]+ printArbo(arbol.derecha)

def insertarArbol(val,arbol):
    if arbol==None:
        return Arbol(val)
    if arbol.valor>val:
        return Arbol(arbol.valor,insertarArbol(val,arbol.izquierda),arbol.derecha)
    if arbol.valor<val:
        return Arbol(arbol.valor,arbol.izquierda,insertarArbol(val,arbol.derecha))

def insetrarALista(lista,arbol):
    if lista==[]:
        return arbol
    else:
        return insetrarALista(lista[1:],insertarArbol(lista[0],arbol))

    
arbolS=Arbol(10,Arbol(5),Arbol(50,Arbol(30,Arbol(20),Arbol(49))))

print(printArbo(insetrarALista([1,200,3,51],arbolS)))

