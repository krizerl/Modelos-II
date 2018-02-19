def longitud(num):
	if num > 0:
		return longitud(num/10) + 1
	return 0

def invertir(num):
    if(num > 1):
        return  invertir(num/10) + (num%10)* pow(10,longitud(num/10))
    return 0

def mayor(num):
    if num>9:
        if num%10 < (num/10)%10:
            return mayor(num/10)
        else:
            return mayor(invertir(num)/10)
    return num

print mayor(input("Ingrese un numero "))
