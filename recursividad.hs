module Recursividad where

--producto de dos numeros
multiplicacion::Int->Int->Int
multiplicacion a 0 = 0
multiplicacion a b = a + multiplicacion a (b-1)

--potencia de dos numeros
potencia::Int->Int->Int
potencia a 0 = 1
potencia a b = a * potencia a (b-1)

--suma de los digitos
sumaDigitos::Int->Int
sumaDigitos 0 = 0
sumaDigitos a = mod a 10 + sumaDigitos (div a 10)

--conteo de digitos
conteoDigitos::Int->Int
conteoDigitos 0 = 0
conteoDigitos a = 1 + conteoDigitos (div a 10)

--division de dos numeros
division::Int->Int->Int
division a b
 | b == 0 = 0
 | b-a == 0 = 1
 | b>a = 0
 | otherwise = 1 + division (a-b) b

--serie de fibonacci
fibonacci::Int->Int
fibonacci 0 = 1
fibonacci 1 = 1
fibonacci a = fibonacci(a-1) + fibonacci(a-2)

--invertir un numero
invertir::Int->Int
invertir a
 | a < 10 = a
 | otherwise = (mod a 10) * (10 ^ (conteoDigitos(a)-1)) + invertir (div a 10)

--digito mayor de un numero
mayor::Int->Int
mayor n
 | n == 0 = 0
 | mod n 10 > mayor(div n 10) = mod n 10
 | otherwise = mayor(div n 10)

 --invertir una lista
invertirLista::[Int]->[Int]
invertirLista lista = case lista of
 [] -> []
 [x] -> [x]
 x:xs -> invertirLista xs ++ [x]

--sumar pares de una lista recursivamente
sumaParesRecursiva::[Int]->Int
sumaParesRecursiva[] = 0
sumaParesRecursiva (x:xs)
 | mod x 2 == 1 = 0 + sumaParesRecursiva(xs)
 | otherwise = x + sumaParesRecursiva(xs)

--sumar pares de una lista con funciones de Haskell
sumaParesFunciones::[Int]->Int
sumaParesFunciones(x:xi) = sum (filter even (x:xi))

--contar numeros inpares de una lista recursivo
listaImpar::[Int]->Int
listaImpar[] = 0
listaImpar(x:xs)
 | mod x 2 == 1 = 1 + listaImpar(xs)
 | otherwise = listaImpar(xs)

--contar numeros impares con funciones de Haskell
listaImparFunciones::[Int]->Int
listaImparFunciones(x:xi) = length (filter odd (x:xi))

--encontrar numero mayor de una lista recursivamente
mayorLista::[Int]->Int
mayorLista[] = 0
mayorLista(x:[]) = x
mayorLista(x:xs)
 | x>mayorLista(xs) = x
 | otherwise = mayorLista(xs)