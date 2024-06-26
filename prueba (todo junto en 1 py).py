import json


with open("biblioteca.json", "r") as archivo_json:
    lectura = json.load(archivo_json)

autor = lectura["Autor"]
categoria = lectura["Categoria"]
libro = lectura["Libro"]
usuario = lectura["Usuario"]
prestamo = lectura["Prestamo"]

def agregar_todo():
    todo = {
        "Autor":autor,
        "Categoria":categoria,
        "Libro":libro,
        "Usuario":usuario,
        "Prestamo":prestamo
    }

    with open("biblioteca.json", "w") as archivo_json:
        lectura = json.dump(todo, archivo_json, indent=4)

def main_menu():
    while True:
        try:
            print("\n*********************************")
            print("*          MUNDO LIBRO          *")
            print("*********************************")
            print("\n1. Mantenedor de autores")
            print("2. Reportes")
            print("0. Salir")
            print("*********************************")
            op = int(input("Seleccione una opción: "))
            if op >= 2 and op <= 0:
                if op == 1:
                    mantenedor_autores()
                elif op == 2:
                    reportes()
                elif op == 0:
                    break
            else:
                print("Seleccione una opción válida")
        except ValueError:
            print("ERROR! Ingrese un valor válido")

def mantenedor_autores():
    while True:
        try:
            print("\n*********************************")
            print("*          MUNDO LIBRO          *")
            print("*********************************")
            print("\n1. Agregar autor")
            print("2. Editar autor")
            print("3. Eliminar autor")
            print("4. Buscar autor")
            print("0. Salir")
            print("*********************************")
            op = int(input("Seleccione una opción: "))
            if op >= 0 and op <= 4:
                if op == 1:
                    agregar_autor()
                elif op == 2:
                    editar_autor()
                elif op == 3:
                    eliminar_autor()
                elif op == 4:
                    buscar_autor()
                elif op == 0:
                    break
            else:
                print("Seleccione una opción válida")
        except ValueError:
            print("ERROR! Ingrese un valor válido")

def agregar_autor():
    global autor
    global categoria
    global libro 
    global usuario
    global prestamo
    id = []
    for datos in autor:
        id.append(datos["AutorID"])
    autorid = len(id) + 1
    nombre = input("Ingrese el nombre del autor: ")
    nacionalidad = input("Ingrese la nacionalidad del autor: ")

    autor_nuevo = {
        "AutorID": autorid,
        "Nombre": nombre,
        "Nacionalidad": nacionalidad
    }
    autor.append(autor_nuevo)
    agregar_todo()

def editar_autor():
    id_autor = int(input("Ingrese la id del autor: "))
    nombre = input("Ingrese el nombre del autor: ")
    nacionalidad = input("Ingrese la nacionalidad del autor: ")
    for datos in autor:
        if datos["AutorID"] == id_autor:
            datos["Nombre"] = nombre
            datos["Nacionalidad"] = nacionalidad
    agregar_todo()
            
def eliminar_autor():
    id_autor = int(input("Ingrese la id del autor: "))
    for datos in autor:
        if datos["AutorID"] == id_autor:
            autor.remove(datos)

    agregar_todo()

def buscar_autor():
    id_autor = int(input("Ingrese la id del autor: "))
    for datos in autor:
        if datos["AutorID"] == id_autor:
            print(datos)

def reportes():
    libros_id = {}
    for datos in prestamo:
        nombre = datos["LibroID"]
        if nombre in libros_id:
            libros_id[nombre] +=1
        else:
            libros_id[nombre] = 1
    reporte = []

    reporte.append("**************************************************************")
    reporte.append("*   Autor           Cantidad de libros prestados *")
    for datos in autor:
        for id, cantidad in libros_id.items():
            if id == datos["AutorID"]:
                nombre_autor = datos["Nombre"] 
                reporte.append(f"{nombre_autor}             {cantidad}")
    reporte.append("**************************************************************")

    with open("Reportes_biblioteca_mundo_libro.json", "w") as archivo_json:
        json.dump(reporte, archivo_json, indent= 4)

            



    
main_menu()



