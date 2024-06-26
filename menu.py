import json
from funciones import agregar_todo, agregar_autor, editar_autor, eliminar_autor, buscar_autor, reportes

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


main_menu()