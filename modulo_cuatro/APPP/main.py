from infrastructure.file_repository import FileRepository
from application.user_service import UserService
from domain.exceptions import(
    ArchivoVacioErrro,
    EdadInvalidaError,
    EdadNegativaError,
    LineaCorruptaError,
)

def main() -> None:
    repo = FileRepository("usuarios.csv")
    service = UserService(repo)
    
    try:
        usuarios = service.procesar()

    except FileNotFoundError as e:
        print(f"[ERROR DE SISTEMA] {e}")
        
    except PermissionError as e:
        print(f"[ERROR DE PERMISOS] {e}")
        
    except UnicodeDecodeError as e:
        print(f"[ERROR ENCONDING] {e}")
        
    except ArchivoVacioErrro as e:
        print(f"[ERROR DATOS] {e}")
    
    except LineaCorruptaError as e:
        print(f"[ERROR FORMATO] {e}")
        
    except EdadInvalidaError as e:
        print(f"[ERROR VALIDACION] {e}")
    
    except EdadNegativaError as e:
        print(f"[ERROR NEGATIVO] {e}")
        
    except Exception as e:
        print(f"[ERROR INESPERADO] {e}")
        
    else:
        print("Usuarios cargados correctamente: ")
        for u in usuarios:
            print(f"{u.nombre}")
    
    