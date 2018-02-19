def division(dividendo, divisor):
	if dividendo >= divisor:
		return division(dividendo - divisor, divisor)+1
	return 0


print division(input("Ingrese el dividendo "), input("Ingrese el divisor "))
