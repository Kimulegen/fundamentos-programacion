Algoritmo contador_cuadrados
//	Inicializar variables
	Definir contador, cuadrado, limite Como Entero
	contador = 1
	
//	Solicitar al usuario que ingrese un n�mero
	Escribir "Ingrese un n�mero"
	Leer limite
	
//	Realizar la repetici�n
	Mientras contador <= limite Hacer
//		Calcular el cuadrado
		cuadrado = contador * contador
		
//		Imprimir el cuadrado
		Escribir "El cuadrado de ", contador, " es: ",cuadrado
		
//		Incrementar el contador
		contador = contador + 1
	FinMientras
FinAlgoritmo
