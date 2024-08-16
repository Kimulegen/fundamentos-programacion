Algoritmo Receta_Robot
	Escribir 'En Stand-By'
	Escribir 'Verificar la hora'
	// generar registro de la hora en la variable "hora"
	Definir hora Como Entero
	Leer hora
	Mientras hora<6 Y hora>=0 Hacer
		Escribir 'Verificar la hora'
		// generar registro de la hora en variable "hora"
		Leer hora
	FinMientras
	Escribir '...saliendo del modo Stand-By...'
	Esperar 3 Segundos
	Limpiar Pantalla
	Escribir 'Prenderse'
	Escribir 'Activar sensores'
	Escribir 'Realizar Autodiagnostico'
	Escribir '¿Problema detectado?: Si, No'
	// generar internamente una respuesta a la pregunta y guardar en la variable "prom_detect"
	Leer prom_detect
	Si prom_detect='Si' Entonces
		Escribir 'Arreglar Problema'
	SiNo
		Escribir 'Continuar con Rutina'
	FinSi
	Esperar 3 Segundos
	Limpiar Pantalla
	Escribir 'Revision del estatus de la casa'
	Escribir 'Algo fuera de lugar?: Si, No'
	// responder a la pregunta anterior en la variable "alg_fuer_lug"
	Leer alg_fuer_lug
	Si alg_fuer_lug='Si' Entonces
		Escribir 'Poner cosas en su lugar'
	SiNo
		Escribir 'Continuar con rutina'
	FinSi
	Esperar 3 Segundos
	Limpiar Pantalla
	Escribir 'Revisionde estatus de habitantes'
	Escribir 'Estan dormidos?: Si, No'
	// generar respuesta interna en la variable "dormid"
	Leer dormid
	Si dormid='Si' Entonces
		Escribir 'Despertar a los habitantes'
	SiNo
		Escribir 'Continuar con rutina'
	FinSi
	Esperar 3 Segundos
	Limpiar Pantalla
	Escribir 'Revision del estado del agua en casa'
	Escribir 'Hay agua caliente?: Si, No'
	// generar respuesta interna en la variable "agu_cal"
	Leer agu_cal
	Si agu_cal='Si' Entonces
		Escribir 'Preparar baño y utensilios de baño'
		Escribir 'Continuar con la rutina'
	SiNo
		Escribir 'Diagnosticar Problema'
		Escribir 'Es la cañeria?: Si, No'
		// generar respuesta en variable "cañeria"
		Leer caneria
		Si caneria='Si' Entonces
			Escribir 'Reunir herramientas de reparacion'
			Escribir 'Reparar'
			Escribir 'Comprobar estado del agua'
			Escribir 'Continuar con la rutina'
		SiNo
			Escribir 'Es el calefont?: Si, No'
			// generar respuesta en la variable "calefont"
			Leer calefont
			Si calefont='No' Entonces
				Escribir 'Son las baterias?: Si, No'
				// generar resouesta en la variable "baterias"
				Leer baterias
				Si baterias='Si' Entonces
					Escribir 'Hay baterias de repuesto?: Si, No'
					// generar respuesta en la variable "bat_rep"
					Leer bat_rep
					Si bat_rep='Si' Entonces
						Escribir 'Reemplazar baterias'
						Escribir 'Comprobar Estado del agua'
						Escribir 'Continuar con rutina'
					SiNo
						Escribir 'Solicitar baterias nuevas'
						Escribir 'Reemplazarlas'
						Escribir 'Comprobar estado del agua'
						Escribir 'Continuar con rutina'
					FinSi
				SiNo
					Escribir 'Esta cortado el gas?: Si, No'
					Leer gas
					Si gas='Si' Entonces
						Escribir 'Dar gas'
						Escribir 'Verificar agua caliente'
						Escribir 'Continuar con rutina'
					SiNo
						Escribir 'Comprobar que haya gas en el balon o cañerias'
						Escribir 'Agendar hora con gasfiter'
						Escribir 'Sugerir usar solo agua helada'
						Escribir 'Continuar con rutina'
					FinSi
				FinSi
			SiNo
				Escribir 'Comprobar estado interno del calefont'
				Escribir 'Problema es reparable?: Si, No'
				// generar respuesta en variable "prom_reparab"
				Leer prom_reparab
				Si prom_reparab='Si' Entonces
					Escribir 'Reunir herramientas'
					Escribir 'Reparar calefont'
					Escribir 'Comprobar estado del agua'
					Escribir 'Continuar con rutina'
				SiNo
					Escribir 'Sugerir ducha solo con agua helada mencionando los beneficios de la misma'
					Escribir 'Agendar hora con gasfiter'
					Escribir 'Continuar con rutina'
				FinSi
			FinSi
		FinSi
	FinSi
	Esperar 3 Segundos
	Limpiar Pantalla
	Escribir 'Preparar desayuno'
	Escribir 'Estan todos los ingredientes?: Si, No'
	// generar respuesta en variable "ingred_desay"
	Leer ingred_desay
	Si ingred_desay='Si' Entonces
		Escribir 'Preparar Desayuno'
	SiNo
		Escribir 'Revisar dinero'
		Escribir 'Hay dinero?: Si, No'
		// generar respuesta en variable dinero_desay
		Leer dinero_desay
		Si dinero_desay='Si' Entonces
			Escribir 'Ir a comprar ingredientes'
		SiNo
			Escribir 'Pedir dinero a dueños'
			Escribir 'Dieron dinero?: Si, No'
			// generar respuesta en variable dar_dinero
			Leer dar_dinero
			Si dar_dinero='Si' Entonces
				Escribir 'Comprar'
				Escribir 'Seguir con Rutina'
			SiNo
				Escribir 'Pedir Fiado'
				Escribir 'Seguir con rutina'
			FinSi
		FinSi
	FinSi
	Esperar 3 Segundos
	Limpiar Pantalla
	Escribir 'Preparar desayuno, disponer de utensilios y servir desayuno'
	Repetir
		Esperar 5 Segundos
		Escribir 'Terminaron de comer?: Si, No'
		// generar respuesta en variable "desay_listo"
		Leer desay_listo
	Hasta Que desay_listo='Si'
	Esperar 3 Segundos
	Escribir 'Excelente'
	Limpiar Pantalla
	Escribir 'Retirar cosas de la mesa'
	Escribir 'Despedir dueños'
	Escribir 'Ordenar casa'
	Esperar 3 Segundos
	Limpiar Pantalla
	Escribir 'Preparar almuerzo/cena'
	Escribir 'Estan todos los ingredientes?: Si, No'
	// generar respuesta en variable ingred_alm
	Leer ingred_alm
	Si ingred_alm='Si' Entonces
		Escribir 'Cocinar'
	SiNo
		Escribir 'Ir a Comprar'
		Escribir 'Me encontré con la vecina?: Si, No'
		// generar respuesta en variable "copucha"
		Leer copucha
		Si copucha='Si' Entonces
			Escribir 'Arreglar el mundo en base a la copucha por una media hora'
			Escribir 'Continuar con rutina'
		SiNo
			Escribir 'Continuar con rutina'
		FinSi
	FinSi
	Esperar 3 Segundos
	Limpiar Pantalla
	Escribir 'Recibir a los niños del colegio'
	Escribir 'Pedirles que se cambien de ropa y se laven las manos'
	Escribir 'Servirles comida'
	Repetir
		Esperar 5 Segundos
		Escribir 'Terminaron de comer?: Si, No'
		// generar respuesta en variable ninos_comer
		Leer ninos_comer
	Hasta Que ninos_comer='Si'
	Escribir 'Excelente'
	Esperar 3 Segundos
	Limpiar Pantalla
	Escribir 'Ordenar a los niños hacer sus labores'
	Escribir 'Los niños quieren hacer sus labores?: Si, No'
	// generar respuesta en variable "ninos_no_tarea"
	Leer ninos_no_tarea
	Si ninos_no_tarea='No' Entonces
		Escribir 'Acusarlos con sus padres'
		Escribir 'Seguir con la rutina'
	SiNo
		Escribir 'Darles un premio aunque hacer las tareas sea solo parte de sus obligaciones y ello no implique una conducta loable por su excepcionalidad'
		Escribir 'Seguir con la rutina'
	FinSi
	Esperar 3 Segundos
	Limpiar Pantalla
	Escribir 'Recibir a los dueños'
	Escribir 'Pedirles que se laven las manos y se preparen para la cena'
	Escribir 'Servir comida'
	Repetir
		Escribir 'Pasear al perro'
		Escribir 'Terminaron de comer?: Si, No'
		// generar respuesta en variable "duenos_comer"
		Leer duenos_comer
	Hasta Que duenos_comer='Si'
	Escribir 'Volver a casa'
	Escribir 'Alimentar mascota'
	Esperar 3 Segundos
	Limpiar Pantalla
	Escribir 'Prepara habitaciones para el descanso'
	Escribir 'Reportar a dueños lo acontecido del dia'
	Escribir 'Tarea especial o extra para mañana?: Si, No'
	// generar respuesta en variable tar_extra
	Leer tar_extra
	Si tar_extra='Si' Entonces
		Escribir 'Sincronizar en la nube. Registrar cambios'
	SiNo
		Escribir 'No realizar ajustes'
	FinSi
	Esperar 3 Segundos
	Limpiar Pantalla
	Escribir 'Cerrar accesos, ventanas y llaves de paso'
	Escribir 'Apagar dispositivos electricos y electronicos'
	Escribir 'Activar alarmas'
	Escribir 'Tomar posicion en estacion de carga'
	Escribir 'Recargar baterias'
	Escribir 'Crear copia de seguridad de la base de datos'
	Escribir 'Buscar actualizaciones de software'
	Escribir 'Hay actualizaciones disponibles?: Si, No'
	// generar respuesta en variable act_soft
	Leer act_soft
	Si act_soft='Si' Entonces
		Escribir 'Descargar actualizacion, aplicar, reiniciar sistema, generar registros'
	SiNo
		Escribir 'Continuar con rutina'
	FinSi
	Esperar 3 Segundos
	Limpiar Pantalla
	Escribir "Iniciar el demonio de lectura horaria"
	Escribir 'Activa modo de bajo consumo'
	Escribir 'Activar parpadeo de led indicador de Stand-By'
	Escribir '...en modo Stand-By...'
FinAlgoritmo
