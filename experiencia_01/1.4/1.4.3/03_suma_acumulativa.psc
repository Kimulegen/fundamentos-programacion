Algoritmo suma_acumulativa
	Definir num, total Como Entero
	
	Escribir "Ingrese un n�mero"
	Leer num
	
	total = 0
	
	Mientras num <> 0 Hacer
		total = total + num
		Escribir "Ingrese otro n�mero"		
		Escribir "La suma de los n�meros es ", total
		Escribir "para salir del programa, presione 0"
		Leer num
	FinMientras
FinAlgoritmo
