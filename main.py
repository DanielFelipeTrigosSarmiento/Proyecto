import os
from funciones import *

def menu_principal():
    print("Qué opcion necesitas?")
    print("1. Agregar Camper")
    print("2. Agregar Trainer")
    print("3. Agregar Ruta de Entrenamiento")
    print("4. Agregar Coordinador") 
    print("5. Consultar Campers")
    print("7. Consultar Trainers")
    print("8. Salir")

def main():
    while True:
        os.system('clear')
        menu_principal()
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            camper_data = {
                "id": int(input("Numero de documento: ")),
                "nombres": input("Nombres: "),
                "apellidos": input("Apellidos: "),
                "direccion": input("Dirección: "),
                "acudiente": input("Acudiente: "),
                "telefonos": int(input("Numero de telefono: ")),
                "estado": input("Estado: "),                
            }
            agregar_camper(camper_data)
        
        elif opcion == 2:
            trainer_data = {
                "id": int(input("ID: ")),
                "nombres": input("Nombres: "),
                "apellidos": input("Apellidos: "),
                "especialidad": input("Especialidad: "),
            }
            agregar_trainer(trainer_data)
        
        elif opcion == 3:
            ruta_data = {
                "nombre": input("Nombre de la Ruta: "),
                "modulo": input("Módulo: "),
                "capacidad_max": int(input("Capacidad Máxima: ")),
                "sgdb_principal": input("SGDB Principal: "),
                "sgdb_alternativo": input("SGDB Alternativo: ")
            }
            agregar_ruta(ruta_data)
        
        elif opcion == 4:
            coordinador_data = {
                "id": int(input("ID: ")),
                "nombres": input("Nombres: "),
                "apellidos": input("Apellidos: "),
                "clave_acceso": int(input("Clave de acceso: "))
            }
            agregar_coordinador(coordinador_data)
        
        elif opcion == 5:
             campers = cargar_json("campers.json")
             for camper in campers:
                 if camper['estado'] == 'Inscrito':
                     print(f"{camper['nombres']} {camper['apellidos']}")        
        elif opcion == 7:
            trainers = cargar_json("trainers.json")
            for trainer in trainers:
                print(f"{trainer['nombres']} {trainer['apellidos']}")
        
        elif opcion == 8:
            os.system('clear')
            print('hasta pronto')
            input('ingrese cualquier tecla para continuar :')
            break
        
        else:
            print("Opción no válida.")
            input("Presione cualquier tecla para continuar...")

if __name__ == "__main__":
    main()
