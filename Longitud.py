def longitud(num, contador):
	if num > 9:
		return longitud(num/10, contador+1)
	return contador

print longitud(input("Ingrese un numero"), 1)