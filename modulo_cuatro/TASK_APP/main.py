from services.service_task import TaskService        
from repository.repository_task import TaskRepository 

def main() -> None:                                 
    service = TaskService(TaskRepository("data/tasks.txt"))  

    while True:                                     
        print("\n1. Agregar tarea")                 
        print("2. Listar tareas")                   
        print("3. Salir")                           

        option = input("Seleccione: ")              

        if option == "1":                            
            title = input("Tarea: ")              
            try:                                    
                service.create_task(title)          
                print("Guardado correctamente")      
            except Exception as e:                   
                print("Error:", e)                  

        elif option == "2":                          
            tasks = service.list_tasks()            
            for i, task in enumerate(tasks, 1):     
                print(f"{i}. {task.title}")          

        elif option == "3":   
            try:
                number = int(input("Ingrese el número de la tarea: "))
                service.complete_task(number)
                print("Tarea completa")
            except ValueError as e:
                print("Error: ", e)  
        
        elif option == "4":            
            break                               


if __name__ == "__main__":                          
    main()                                           