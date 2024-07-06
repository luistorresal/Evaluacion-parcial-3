# PRUEBA PARCIAL 3
import csv

lista_estudiantes = []

def procesar_lista_estudiantes():
    with open("ListaCurso5B.csv", "r") as archivo_csv:
        lectura_csv = csv.reader(archivo_csv)
        for fila in lectura_csv:
            print(fila)

def registrar_estudiante():
    rut = input("Ingresar RUT: ")
    nombre = input("Ingresar nombre: ")
    nota_1 = float(input("Ingresar NOTA 1: "))
    nota_2 = float(input("Ingresar NOTA 2: "))
    lista_estudiantes.append({"rut":rut,"nombre":nombre,"nota 1":nota_1,"nota 2":nota_2})
    print("Estudiante registrado con éxito")

def modificar_nota():
    rut = input("Ingresar rut estudiante: ")
    nota = float(input("Ingresar NOTA para modificar (NOTA 1 o NOTA 2): "))
    return rut, nota

def eliminar_estudiante():
    rut = input("Ingresar rut estudiante: ")
    resp = int(input("¿Estás seguro de eliminar? [1]si [2]no"))

def generar_promedio_notas():
    pass

def generar_acta_cierre_notas():
    with open("Acta_cierre_5B.csv", "w") as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow(["Rut", "Nombre", "Nota 1", "Nota 2", "Promedio", "Estado"])

def salir():
    print("Programa Terminado")

while True:
    print("********************")
    print("Colegio EducandoAndo")
    print("1.- Procesar lista de estudiantes")
    print("2.- Registrar estudiante")
    print("3.- Modificar nota")
    print("4.- Eliminar estudiante")
    print("5.- Generar promedio de notas")
    print("6.- Generar aca de cierre de curso")
    print("7.- Salir")
    print("********************")
    try: 
        opcion = int(input("Ingresar una opción: "))
        if opcion == 1:
            procesar_lista_estudiantes()
        elif opcion == 2:
            registrar_estudiante()
        elif opcion == 3:
            modificar_nota()
        elif opcion == 4:
            eliminar_estudiante()
        elif opcion == 5:
            generar_promedio_notas()
        elif opcion == 6:
            generar_acta_cierre_notas()
        elif opcion == 7:
            salir()
            break
        else:
            print("Opcion no válida")
    except ValueError:
        print("Debes ingresar un valor númerico del 1 al 7")