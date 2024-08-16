Algoritmo estacion_servicio
	Definir nivel_bencina, tipo_bencina como Entero
	Escribir "Bienvenido a la estación de servicio"
	Escribir "¿Cuantos litros de bencina tiene tu auto?"
	Leer nivel_bencina
	
	Si nivel_bencina < 10 Entonces
		Escribir "Es recomendado cargar mas bencina"
		Escribir "Elige el tipo de bencina que quieres cargar (93/95/97)"
		Leer tipo_bencina
		
		Si tipo_bencina == 93 Entonces
			Escribir "Cargando bencina regular..."
			Esperar 1 Segundos
			Escribir "Carga realizada con éxito"
		SiNo Si tipo_bencina == 95 Entonces
				Escribir "Cargando bencina plus..."
				Esperar 1 Segundos
				Escribir "Carga realizada con éxito"
			SiNo Si tipo_bencina == 97 Entonces
					Escribir "Cargando bencina premium..."
					Esperar 1 Segundos
					Escribir "Carga realizada con éxito"
				SiNo
					Escribir "Error tipo de bencina especificada no es válida, cancelando carga"
				FinSi
			FinSi
		FinSi
	SiNo 
		Escribir "No es necesario cargar más bencina"
	FinSi
	
FinAlgoritmo
