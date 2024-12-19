import json

class Camper:
    def __init__(self, id, nombres, apellidos, direccion, acudiente, telefonos, estado):
        self.id = id
        self.nombres = nombres
        self.apellidos = apellidos
        self.direccion = direccion
        self.acudiente = acudiente
        self.telefonos = telefonos  
        self.estado = estado  
     

    def to_dict(self):
        return {
            "id": self.id,
            "nombres": self.nombres,
            "apellidos": self.apellidos,
            "direccion": self.direccion,
            "acudiente": self.acudiente,
            "telefonos": self.telefonos,
            "estado": self.estado,
            
        }
