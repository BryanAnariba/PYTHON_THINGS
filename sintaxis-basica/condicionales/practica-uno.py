def estaAprobado(notaFinal):
    status = "Analizando"
    if notaFinal < 65:
        status = 'Reprobado'
    else:
        status = 'Aprobado'
    return status

print("++++Verificacion de notas del alumnos++++")
notaAlumnoUno = float(input("Digite la nota del primer alumno: "))
notaAlumnoDos = float(input("Digite la nota del segundo alumno: "))

verificacionAlumnoUno = estaAprobado(notaAlumnoUno)
verificacionAlumnoDos = estaAprobado(notaAlumnoDos)

print("Nota del alumno Uno => ", verificacionAlumnoUno)
print("Nota del alumno Dos => ", verificacionAlumnoDos)

