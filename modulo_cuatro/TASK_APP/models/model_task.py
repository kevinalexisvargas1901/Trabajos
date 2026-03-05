from dataclasses import dataclass          # Permite crear clases de datos automáticamente (menos código boilerplate)

@dataclass(frozen=True)                    # Genera constructor, equals y repr; frozen=True lo hace inmutable
class Task:                                # Representa una tarea del sistema
    title: str                             # Nombre o descripción de la tarea
    completed: bool = False                # Estado de la tarea (por defecto no completada)

    def serialize(self) -> str:            # Convierte el objeto a texto para guardarlo en archivo
        return f"{self.title}|{int(self.completed)}"  # Guarda como: titulo|0 o titulo|1

    @staticmethod                          # Método de clase sin necesidad de instancia previa
    def deserialize(data: str) -> "Task":  # Convierte una línea de texto nuevamente en objeto Task
        title, completed = data.split("|") # Separa los datos usando el separador |
        return Task(title=title, completed=bool(int(completed)))  # Reconstruye el objeto convirtiendo 0/1 a booleano
    
    def mark_completed(self)-> "Task":
        return Task(title= self.title, completed=True)