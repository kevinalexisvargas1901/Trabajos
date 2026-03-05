from typing import List                     # Permite tipar listas para mayor claridad y control
from models.model_task import Task                # Importa el modelo de datos Task
from utils.file_manager import FileManager # Importa la capa encargada de manejar archivos

class TaskRepository:                       # Capa repositorio: comunica el sistema con el almacenamiento
    """Repositorio basado en archivo plano."""

    def __init__(self, file_path: str) -> None:  # Constructor que recibe la ruta del archivo
        self._file = FileManager(file_path)      # Inicializa el gestor de archivos

    def get_all(self) -> List[Task]:        # Obtiene todas las tareas almacenadas
        lines = self._file.read_lines()     # Lee todas las líneas del archivo
        return [Task.deserialize(line) for line in lines if line]  # Convierte cada línea en objeto Task

    def save(self, task: Task) -> None:     # Guarda una nueva tarea en el archivo
        self._file.append_line(task.serialize()) # Convierte el objeto a texto y lo agrega al archivo
        
        
    def overwrite_all(self, tasks: List[Task]) -> None:
        serialized = [task.serialize() for task in tasks]
        self._file.overwrite_all(serialized)