def longitud(num):
	if num > 0:
		return longitud(num/10) + 1
	return 0
def invertir(num):
    if(num > 1):
        return  invertir(num/10) + (num%10)* pow(10,longitud(num/10))
    return 0

print invertir(input("Ingrese un numero "))


