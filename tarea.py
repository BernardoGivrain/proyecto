class Tarea:
    def __init__(self, titulo, fecha_creacion, fecha_limite):
        self.id = 1
        self.titulo = titulo
        self.fecha_creacion = fecha_creacion
        self.fecha_limite = fecha_limite
        self.completado = "❌"
