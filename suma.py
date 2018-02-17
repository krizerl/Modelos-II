def suma(num):
	if num > 10:
		return num%10 + suma(num/10)
	return num%10

print suma(input("Ingrese un número"))