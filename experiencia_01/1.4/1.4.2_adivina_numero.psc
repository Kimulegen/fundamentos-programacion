Algoritmo adivina_numero
	Definir numero_adivinar, intentos, intento_usuario como Entero;
	Definir acertado Como Logico
	numero_adivinar = Aleatorio(1,100);
	
	Escribir "Ingrese el numero de intentos que desea tener"
	Leer intentos
	
	Mientras intentos > 0 y acertado == Falso Hacer
		Escribir "Ingrese un numero"
		Leer intento_usuario
		Si intento_usuario == numero_adivinar Entonces
			Escribir "¡felicitaciones, acertaste el numero!"
			acertado = Verdadero
		SiNo
			Escribir "numero incorrecto, ¡intenta de nuevo!"
			intentos = intentos - 1
		FinSi
	FinMientras
	
	Si numero_adivinar <> intento_usuario Entonces
		Escribir "El numero a adivinar era: ", numero_adivinar
	FinSi
	
FinAlgoritmo
