"""
class Libro:
    #Constructor
    def __init__(self, titulo, autor, isbn, precio):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.precio = precio
        
libro1 = Libro("Matematicas", "Luis Molero", "2132321-32", 12324)
print(libro.titulo)

"""

#Encapsulamiento

class Libro:
    def __init__(self, titulo, precio):
        self.__titulo = titulo
        self.__precio = precio
    
    def get_precio(self):
        return self.__precio
    
    def set_precio(self, nuevo_precio):
        #Validar precio
        if isinstance(nuevo_precio,(int,float)) and nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("Error ingrese un valor correcto")
        
    def mostrar_info(self):
        print(f"Titulo: {self.__titulo}")
        print(f"Precio {self.__precio}")
        
def main():
    print ("\n*** SISTEMA DE REGISTRO DE LIBROS ***")
    
    book1 = Libro("Biología", 1000)
    
    print("Informacion del libro")
    
    book1.mostrar_info()

if __name__ == "__main__":
    main()