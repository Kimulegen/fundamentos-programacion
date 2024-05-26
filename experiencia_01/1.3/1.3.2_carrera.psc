Algoritmo carrera
	Definir encuentro_valla, encuentro_tunel, encuentro_laguna Como Caracter
	Escribir "¡Comienza la carrera!"
	Escribir "¿Te encuentras con una valla?"
	Leer encuentro_valla
	
	Si encuentro_valla == "si" Entonces
		Escribir "¡salta la valla!"
	SiNo
		Escribir "¡continua corriendo!"
	FinSi
	Esperar 1 Segundos
	Escribir "¿Te encuentras con un tunel?"
	Leer encuentro_tunel
	Si encuentro_tunel == "si" Entonces
		Escribir "¡atraviesa el tunel!"
	SiNo
		Escribir "¡continua corriendo!"
	FinSi
	Esperar 1 Segundos
	Escribir "¿Te encuentras con una laguna?"
	Leer encuentro_laguna
	Si encuentro_laguna == "si" Entonces
		Escribir "¡nada!"
		Esperar 2 Segundos
		Escribir "oh no! perdiste la carrera por devolverte!"
	SiNo
		Escribir "¡felicitaciones por llegar a la meta!"
	FinSi
FinAlgoritmo
