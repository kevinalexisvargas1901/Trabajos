def validate_title(title: str) -> str:      # Función que valida el texto del título de la tarea
    title = title.strip()                   # Elimina espacios al inicio y al final

    if not title:                           # Verifica que no quede vacío
        raise ValueError("La tarea no puede estar vacía")  # Error si el texto está vacío

    if len(title) > 60:                     # Verifica longitud máxima permitida
        raise ValueError("La tarea es demasiado larga")    # Error si supera 60 caracteres

    if "|" in title:                        # Evita el uso del separador del archivo
        raise ValueError("Caracter inválido")              # Error si contiene '|'

    return title                            # Retorna el título limpio y válido

def validate_index(index: int, size: int) -> int:
    if size == 0:
        raise ValueError("No hay tareas registradas")
    if index < 1:
        raise ValueError("El indice de la tarea modificar de ser superior a 0")
    if index > size:
        raise ValueError("El indice de latarea modificar debe estar dentro del rago de registros")
    
    return index - 1