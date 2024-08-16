Algoritmo ordenar_numeros
	Definir n1,n2,n3 Como Entero
	Escribir 'ingrese el primer numero'
	Leer n1
	Escribir 'ingrese el segundo numero'
	Leer n2
	Escribir 'ingrese el tercer numero'
	Leer n3
	
	Si n1>n2 y n1>n3 Entonces
		Si n2> n3 Entonces
			Escribir "Los numeros en orden: ",n3, " " ,n2, " ",n1
		SiNo
			Escribir "Los numeros en orden: ",n2, " " ,n3, " ",n1
		FinSi
	SiNo
		Si n2>n3 Entonces
			Si n1> n3 Entonces
				Escribir "Los numeros en orden: ",n3, " " ,n1, " ",n2
			SiNo
				Escribir "Los numeros en orden: ",n1, " " ,n3, " ",n2
			FinSi
		SiNo
			Si n2>n1 Entonces
				Escribir "Los numeros en orden: ",n1, " " ,n2, " ",n3
			SiNo
				Escribir "Los numeros en orden: ",n2, " " ,n1, " ",n3
			FinSi
		FinSi
	FinSi
	
FinAlgoritmo
