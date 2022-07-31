
#Se importan las funciones del ejercicio 8
from Ejercicio_8_func import Agregar
from Ejercicio_8_func import eliminar
from Ejercicio_8_func import Mostrar
from Ejercicio_8_func import edad


#Se crea un while para el menu
while True:

    #Se imprimen las opciones del menu
    print(" Que quieres hacer? \n",
          "Agregar clientes     (1) \n",
          "Eliminar clientes    (2) \n",
          "Mostrar los clientes (3) \n",
          "Ver la edad promedio (4) \n", 
          "Salir                (5)")
          
    #Input para la eleccion
    #       
    do = input(": ")
    print("\n")
    
    #Se usa la funccion segun la eleccion
    if do == "1":
        Agregar()
    elif do == "2":
        eliminar()
    elif do == "3":
        Mostrar()
    elif do == "4":
        edad()
    elif do == "5":
        print("Cerrando programa.")
        break                     
    else:
        print("Error con la eleccion \n")  








