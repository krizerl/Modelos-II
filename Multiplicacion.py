def multiplicacion(adicion, variable):
	if variable > 1:
		return adicion + multiplicacion(adicion, variable-1)
	return adicion
print multiplicacion(input("Ingrese un numero "), input("Ingrese un numero "))
