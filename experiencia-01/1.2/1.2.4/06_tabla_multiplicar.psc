Algoritmo tabla_multiplicar
	Definir num, factor, producto Como Entero	
	Escribir "Ingrese un numero entre el 1 y el 10"
	Leer num
	Mientras num<=0 o num>11 Hacer
		Escribir "Ingrese un numero entre el 1 y el 10"
		Leer num
	FinMientras
	Para factor=1 Hasta 10 Con Paso 1 Hacer
		producto = num*factor
		Escribir num " multiplicado por ", factor " = ", producto
	FinPara
FinAlgoritmo


