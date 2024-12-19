import json
from camper import Camper
from trainer import Trainer
from ruta import Ruta
from cordinador import Coordinador

def cargar_json(ruta_archivo):
    try:
        with open(ruta_archivo, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def guardar_json(ruta_archivo, datos):
    with open(ruta_archivo, 'w') as f:
        json.dump(datos, f, indent=4)

def agregar_camper(camper_data, ruta_archivo="campers.json"):
    campers = cargar_json(ruta_archivo)
    camper = Camper(**camper_data)
    campers.append(camper.to_dict())
    guardar_json(ruta_archivo, campers)
    print(f"Camper {camper.nombres} {camper.apellidos} agregado correctamente.")

def agregar_trainer(trainer_data, ruta_archivo="trainers.json"):
    trainers = cargar_json(ruta_archivo)
    trainer = Trainer(**trainer_data)
    trainers.append(trainer.to_dict())
    guardar_json(ruta_archivo, trainers)
    print(f"Trainer {trainer.nombres} {trainer.apellidos} agregado correctamente.")

def agregar_ruta(ruta_data, ruta_archivo="rutas.json"):
    rutas = cargar_json(ruta_archivo)
    ruta = Ruta(**ruta_data)
    rutas.append(ruta.to_dict())
    guardar_json(ruta_archivo, rutas)
    print(f"Ruta {ruta.nombre} agregada correctamente.")

def agregar_coordinador(coordinador_data, ruta_archivo="coordinadores.json"):
    coordinadores = cargar_json(ruta_archivo)
    coordinador = Coordinador(**coordinador_data)
    coordinadores.append(coordinador.to_dict())
    guardar_json(ruta_archivo, coordinadores)
    print(f"Coordinador {coordinador.nombres} {coordinador.apellidos} agregado correctamente.")

#
