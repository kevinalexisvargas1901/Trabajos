from repository.repository_task import TaskRepository  # Importa la capa de acceso a datos
from models.model_task import Task                     # Importa el modelo de tarea
from utils.validator import validate_title    
from typing import List# Importa la función de validación

class TaskService:                                     # Capa de negocio: coordina validaciones y repositorio

    def __init__(self, repository: TaskRepository) -> None:  # Recibe el repositorio por inyección de dependencia
        self._repository = repository                        # Guarda referencia al repositorio

    def create_task(self, title: str) -> None:               # Caso de uso: crear una tarea
        clean_title = validate_title(title)                  # Valida el título antes de procesar
        task = Task(clean_title)                             # Crea el objeto de dominio
        self._repository.save(task)                          # Persiste la tarea

    def list_tasks(self) -> list[Task]:                      # Caso de uso: listar tareas
        return self._repository.get_all()                    # Obtiene todas las tareas almacenadas
    
    def complete_task(self, index: int) -> None:
        tasks = self._repository.get_all()
        validated_index = validated_index(index, len(tasks))
        updated_task[validated_index].mark_completed()
        tasks[validated_index] = updated_task
        self._repository.overwrite_all(tasks)