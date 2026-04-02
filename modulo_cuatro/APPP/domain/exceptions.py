class DomainError(Exception):
    pass

class EdadInvalidaError(DomainError):
    pass

class EdadNegativaError(DomainError):
    pass

class ArchivoVacioErrro(DomainError):
    pass