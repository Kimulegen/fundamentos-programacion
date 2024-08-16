Algoritmo repeticion_con_contador
//	Inicializar las variables
	Definir contador como Entero
	contador = 1
	
//	Solicitar al usuario que ingrese un número
	Escribir "Ingrese un número"
	Definir limite Como Entero
	Leer limite
	
//	Realizar la repetición mientras el contador sea menor o igual que el número ingresado
	Mientras (contador <= limite) Hacer
		Escribir "Contador: ", contador
//		Incrementar el contador en cada iteración
		contador = contador + 1
	FinMientras
FinAlgoritmo
