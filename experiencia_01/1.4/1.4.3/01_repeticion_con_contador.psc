Algoritmo repeticion_con_contador
//	Inicializar las variables
	Definir contador como Entero
	contador = 1
	
//	Solicitar al usuario que ingrese un n�mero
	Escribir "Ingrese un n�mero"
	Definir limite Como Entero
	Leer limite
	
//	Realizar la repetici�n mientras el contador sea menor o igual que el n�mero ingresado
	Mientras (contador <= limite) Hacer
		Escribir "Contador: ", contador
//		Incrementar el contador en cada iteraci�n
		contador = contador + 1
	FinMientras
FinAlgoritmo
