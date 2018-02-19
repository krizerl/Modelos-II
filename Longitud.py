def longitud(num):
	if num > 9:
		return longitud(num/10) + 1
	return 1
print longitud(input("Ingrese un numero "))
