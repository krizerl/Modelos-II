def fibonacci(variable):
    if variable == 0 or variable == 1:
        return variable
    else:
        return fibonacci(variable - 1) + fibonacci(variable - 2)
print fibonacci(int(input("Ingrese el numero ")))
