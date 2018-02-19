def longitud(num):
	if num > 0:
		return longitud(num/10) + 1
	return 0

def invertir(num):
    if(num > 1):
        return  invertir(num/10) + (num%10)* pow(10,longitud(num/10))
    return 0

def palindromo (num):
    if num == invertir(num):
        return "el numero es palindromo"
    return "el numero no es palindromo"
   

print palindromo(input("Ingrese un numero "))


