def potencia(base, exponente):
	if exponente > 1:
		return base * potenciaPrueba(base, exponente-1)
	return base

print potencia(input("Ingrese la base "), input("Ingrese el exponente "))