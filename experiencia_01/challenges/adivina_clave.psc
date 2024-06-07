Algoritmo sin_titulo
	Definir clave, i, clave_lon  como Entero
	Definir u,d,c,u_m,d_m Como Logico
	Definir clave_mostrada, unidad, decena, centena, u_millar, d_millar, digito, clave_str Como Caracter
	clave_mostrada = "_ _ _ _ _"
	
	Escribir "Primer jugador: Ingresa una clave de 5 dígitos"
	Leer clave
	clave_str = ConvertirATexto(clave)
	clave_lon = Longitud(clave_str)
	Mientras clave_lon <> 5 Hacer
		Escribir "Tiene que ser una clave de 5 dígitos!"
		Leer clave
		clave_str = ConvertirATexto(clave)
		clave_lon = Longitud(clave_str)
	Fin Mientras
	
	unidad = ConvertirATexto(clave%10)
	decena = ConvertirATexto(TRUNC(clave%100 / 10))
	centena = ConvertirATexto(TRUNC(clave%1000 / 100))
	u_millar = ConvertirATexto(TRUNC(clave%10000 / 1000))
	d_millar = ConvertirATexto(TRUNC(clave%100000 / 10000))
	
	i = 5
	Mientras i >= 0 y adivinado = Falso Hacer
		Escribir "Segundo Jugador: Ingrese un número que cree que estará en la clave"
		Leer digito
		
		Si d_millar = digito Entonces
			Si d_m = Verdadero Entonces
				Escribir "ya adivinaste ese número!"
				i = i + 1
			SiNo
				Escribir "adivinaste un número!"
				d_m = Verdadero
				sub_str_1 = SUBCADENA(clave_mostrada, 2,10)
				clave_mostrada = Concatenar(d_millar, sub_str_1)
				Escribir clave_mostrada
				Escribir "Te quedan ", i, " intentos"
			FinSi
		SiNo
			Si u_millar = digito Entonces
				Si u_m = Verdadero Entonces
				Escribir "ya adivinaste ese número!"
				i = i + 1
				Sino	
					Escribir "adivinaste un número!"
					u_m =Verdadero
					sub_str_1 = Subcadena(clave_mostrada, 0, 2)
					sub_str_2 = Subcadena(clave_mostrada, 4,10)
					clave_mostrada = Concatenar(sub_str_1, u_millar)
					clave_mostrada = Concatenar(clave_mostrada,sub_str_2)
					Escribir clave_mostrada
					Escribir "Te quedan ", i, " intentos"
				FinSi
			SiNo
				Si centena = digito  Entonces
					Si c = Verdadero Entonces
						Escribir "ya adivinaste ese número!"
						i = i + 1
					Sino
						Escribir "adivinaste un número!"
						c = Verdadero
						sub_str_1 = Subcadena(clave_mostrada, 0, 4)
						sub_str_2 = Subcadena(clave_mostrada, 6,10)
						clave_mostrada = Concatenar(sub_str_1, centena)
						clave_mostrada = Concatenar(clave_mostrada,sub_str_2)
						Escribir clave_mostrada
						Escribir "Te quedan ", i, " intentos"
					FinSi
				SiNo
					Si decena = digito  Entonces
						Si d = Verdadero Entonces
							Escribir "ya adivinaste ese número!"
							i = i + 1
						Sino
							d = Verdadero
							Escribir "adivinaste un número!"
							sub_str_1 = Subcadena(clave_mostrada, 0, 6)
							sub_str_2 = Subcadena(clave_mostrada, 8,10)
							clave_mostrada = Concatenar(sub_str_1, decena)
							clave_mostrada = Concatenar(clave_mostrada,sub_str_2)
							Escribir clave_mostrada
							Escribir "Te quedan ", i, " intentos"
						FinSi
					SiNo
						Si unidad = digito Entonces
							Si u = Verdadero Entonces
								Escribir "ya adivinaste ese número!"
								i = i + 1
							Sino
								u = Verdadero
								Escribir "adivinaste un número!"
								sub_str_1 = Subcadena(clave_mostrada, 0, 8)
								clave_mostrada = Concatenar(sub_str_1, unidad)
								Escribir clave_mostrada
								Escribir "Te quedan ", i, " intentos"
							FinSi
						SiNo
							Escribir "Ese número no está en la clave!"
							Escribir "Te quedan ", i, " intentos"
						FinSi
					FinSi
				FinSi
			FinSi
		FinSi

		Si u = Verdadero y d = Verdadero y c = Verdadero y u_m = Verdadero y d_m = Verdadero Entonces
			Escribir "Felicidades has descifrado la clave secreta"
			adivinado = Verdadero
		SiNo
			Si i = 0 y adivinado = Falso Entonces
				Escribir "No lograste adivinar el número secreto, el número buscado era: ", clave
			FinSi
		FinSi
	i = i - 1
	Fin Mientras
FinAlgoritmo
