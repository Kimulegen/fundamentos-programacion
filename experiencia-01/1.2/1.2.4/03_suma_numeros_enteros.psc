Algoritmo suma_numeros_enteros
	Definir n1, n2, suma Como Entero
	Escribir "Ingrese un numero entero positivo"
	Leer n1
	Mientras n1<0 Hacer
		Escribir "porfavor ingresa un numero positivo"
		Leer n1
	FinMientras
	Escribir "Ingrese otro numero entero positivo"
	Leer n2
	Mientras n2<0 Hacer
		Escribir "porfavor ingresa un numero positivo"
		Leer n2
	FinMientras
	suma = n1 + n2
	Escribir "la suma de los dos numero es: ", suma
FinAlgoritmo
