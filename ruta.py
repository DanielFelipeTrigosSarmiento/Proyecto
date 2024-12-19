class Ruta:
    def __init__(self, nombre, modulo, capacidad_max, sgdb_principal, sgdb_alternativo):
        self.nombre = nombre
        self.modulo = modulo  
        self.capacidad_max = capacidad_max
        self.sgdb_principal = sgdb_principal
        self.sgdb_alternativo = sgdb_alternativo
        self.campers_asignados = []

    def agregar_camper(self, camper):
        if len(self.campers_asignados) < self.capacidad_max:
            self.campers_asignados.append(camper)
        else:
            print(f"La ruta {self.nombre} ha alcanzado su capacidad máxima.")

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "modulo": self.modulo,
            "capacidad_max": self.capacidad_max,
            "sgdb_principal": self.sgdb_principal,
            "sgdb_alternativo": self.sgdb_alternativo,
            "campers_asignados": [camper.to_dict() for camper in self.campers_asignados]
        }
