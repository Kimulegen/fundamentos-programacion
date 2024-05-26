Algoritmo suma_acumulativa
	Definir num, total Como Entero
	
	Escribir "Ingrese un número"
	Leer num
	
	total = 0
	
	Mientras num <> 0 Hacer
		total = total + num
		Escribir "Ingrese otro número"		
		Escribir "La suma de los números es ", total
		Escribir "para salir del programa, presione 0"
		Leer num
	FinMientras
FinAlgoritmo
