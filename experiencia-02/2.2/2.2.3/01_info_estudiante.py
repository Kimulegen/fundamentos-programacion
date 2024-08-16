#! Python3
# Ask for student info, show it formatted

nomAlum = input("Ingrese el nombre del alumno: ")
rut = input("Ingrese rut apoderado: ")
curso = input("Ingrese curso al cual el alumno debe matricularse: ")
matricula = int(25000)
mensualidad = int(30000)
resultadoAnual = (mensualidad * 10) + matricula

print(f" Detalle Anualidad Colegio ".center(30, "="))
print(f"NOMBRE ALUMNO: {nomAlum}")
print(f"RUT APODERADO: {rut}")
print(f"CURSO MATRICULADO: {curso}")
print(f"VALOR MATRÍCULA: {matricula}")
print(f"VALOR MENSUALIDAD: {mensualidad}")
print(f"VALOR TOTAL A PAGAR: {resultadoAnual}")
