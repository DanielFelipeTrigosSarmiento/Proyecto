class Coordinador:
    def __init__(self, id, nombres, apellidos, clave_acceso):
        self.id = id
        self.nombres = nombres
        self.apellidos = apellidos
        self.clave_acceso = clave_acceso

    def to_dict(self):
        return {
            "id": self.id,
            "nombres": self.nombres,
            "apellidos": self.apellidos,
            "clave_acceso": self.clave_acceso
        }
