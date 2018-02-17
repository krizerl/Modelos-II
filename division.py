def division(dividendo, divisor, contador):
	if dividendo >= divisor:
		return division(dividendo - divisor, divisor, contador + 1)
	return contador

print division(input("Ingrese el dividendo "), input("Ingrese el divisor "), 0)