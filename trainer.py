class Trainer:
    def __init__(self, id, nombres, apellidos, especialidad, rutas_asignadas=None):
        if rutas_asignadas is None:
            rutas_asignadas = []
        self.id = id
        self.nombres = nombres
        self.apellidos = apellidos
        self.especialidad = especialidad
        self.rutas_asignadas = rutas_asignadas

    def to_dict(self):
        return {
            "id": self.id,
            "nombres": self.nombres,
            "apellidos": self.apellidos,
            "especialidad": self.especialidad,
            "rutas_asignadas": self.rutas_asignadas
        }

    