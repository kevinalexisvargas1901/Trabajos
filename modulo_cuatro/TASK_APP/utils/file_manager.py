from pathlib import Path            # Permite manejar rutas de archivos de forma segura y multiplataforma
from typing import List   
import tempfile
import os # Permite indicar tipos de datos (en este caso lista de strings)

class FileManager:                  # Clase encargada de gestionar archivos de texto
    """Gestiona operaciones seguras sobre archivos de texto."""

    def __init__(self, file_path: str) -> None:   # Constructor: recibe la ruta del archivo
        self._path = Path(file_path)              # Convierte el string en un objeto Path
        self._ensure_file()                       # Garantiza que el archivo exista antes de usarlo

    def _ensure_file(self) -> None:               # Método interno (privado) para asegurar existencia
        """Garantiza que el archivo exista."""
        self._path.parent.mkdir(parents=True, exist_ok=True)  # Crea carpetas si no existen
        self._path.touch(exist_ok=True)                        # Crea el archivo si no existe

    def read_lines(self) -> List[str]:           # Lee el archivo y devuelve una lista de líneas
        try:                                     # Bloque de control de errores
            with self._path.open("r", encoding="utf-8") as file:  # Abre archivo en modo lectura
                return [line.strip() for line in file.readlines()] # Lee todas las líneas y elimina saltos
        except OSError as error:                 # Si ocurre un error del sistema de archivos
            raise RuntimeError("Error leyendo archivo") from error # Lanza error más claro para la app

    def append_line(self, text: str) -> None:    # Agrega una nueva línea al archivo
        if "\n" in text:                         # Valida que no tenga saltos de línea internos
            raise ValueError("El texto no debe contener saltos de línea") # Evita corrupción del archivo

        try:                                     # Manejo de errores de escritura
            with self._path.open("a", encoding="utf-8") as file:  # Abre archivo en modo añadir (append)
                file.write(text + "\n")          # Escribe el texto y agrega salto de línea manualmente
        except OSError as error:                 # Si falla escritura en disco
            raise RuntimeError("Error escribiendo archivo") from error # Error controlado para el sistema
        

    
    def overwrite_all(self, Lines: List[str]) -> None:
            try:
                    with tempfile.NameTemporaryFile(
                    mode = "w",
                    encording="utf-8",
                    delete=False,
                    dir= self._path.parent
                
                ) as tmp:
                     for line in Lines:
                        tmp.write(line + "\n")
                    
                    os.replace(tmp.name, self._path)
            except OSError as error:
                raise RuntimeError("Error sobreescribiendo el archivo") from error    