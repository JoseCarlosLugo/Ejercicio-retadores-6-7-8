
#Diccionario para los datos

clientes={45471:["Luis Perez",45,"BJX", True], 8944411:["FernandaGarcia",25,"JAL", True], 
5223:["Alejandra Ortiz",33,"JDL", True]}

#se crean una funcion para agregar clientes
def Agregar():

        #Bucle para evitar errores con el input del INE
        while True:
            
            #Try y except para que el input solo sea int
            try:
                INE = int(input("INE del pasajero: ")) 
                break

            except:
                print("Error con la INE ")

         # Se pide nombre
        name = input("Nombre del pasajero: ")

        #Bucle para evitar errores con el input de la edad
        while True:
            #Try y except para que el input solo sea int
            try:
                age = int(input("Edad del pasajero: ")) 
                print("\n")
                break

            except:
                print("Error con la edad \n")


        print(
            "Destino      |   Código IATA \n",
            "Guanajuato  |     BJX \n",
            "Guadalajara |     GDL \n",
            "Veracruz    |     JAL \n"
        )

        #input del IATA
        iata = input("IATA del pasajero: ")
        iata = iata.upper()

        #Se abre If para que el input solo sea uno de los 3 codigos IATA
        if iata == "BJX":
            iata = "BJX"

        elif iata == "GDL":
            iata = "GDL"

        elif iata == "JAL" :
            iata = "JAL"

        else:
            print("Error con el IATA \n")

        #While para evitar errores con el input del cliente 
        while True:
            prefer = input("Cliente preferente (Si/No): ")
            prefer = prefer.upper()

            #Se abre If para que el input solo sea 'SI' o 'NO'
            if prefer == "SI":
                preferential = True
                break

            elif prefer == "NO":
                preferential = False
                break

            else:
                print("Error con la preferencia \n")

        #Se agregan los datos al diccionarios la llave es la INE y lo demas los valores
        clientes [INE] = [name, age, iata, preferential]    
        print("Pasajero agregado \n")
        
        #while para evitar errores
        while True:
            #Inputo para agregar otro cliente
            salir = input("Quiere agrecar otro cliente (Si/No): ")
            salir = salir.upper()
            if salir == "SI":
                #Se llama otra vez a la funcion para que sea un bucle
                print("\n")
                Agregar()
            elif salir == "NO":
                #termina la funcion 
                print("\n")
                print("Volviendo al menu")
                print("\n")
                break
            else:
                print("Error con la eleccion \n")    

#Funcion para eliminar clientes
def eliminar():
    
    while True:
    
        #Input para preguntar si quiere elimnar
        do = input("Quiere eliminar un cliente (Si/No): ")
        do = do.upper()
        #If para que solo sean dos input "SI" y "NO"
        if do == "SI":

            #Input para saber cual cliente se eliminara
            del_Key = int(input("INE del pasajero que quiere eliminar: "))

            #If para saber si el cliente esta en el diccionario
            if del_Key in clientes:
                #Se elimina
                del clientes[del_Key]
                print("Se ha eliminado al cliente \n")
                break
            else:
                print("No se ha encontrado al cliente \n")

        elif do == "NO":
            #Termina la funcion
            print("\n")
            break
        else:
            print("Error con la eleccion \n")

#funcion para ver los clientes
def Mostrar():

    print(" Mostrar todos los clientes    ('1') \n",
          "Mostar los cliente preferente ('2') \n",
          "Mostar los clientes normales  ('3')")
    #input para la eleccion
    hacer = input(":")      
    

    if hacer == "2":
        print("\n")
        #for para recorrer el diccionario
        for key in clientes:
            #for para recorrer la lista segun la llave
            for a in clientes[key]:
                # si el cliente es preferente se imprime
                if a == True:
                    print(clientes[key])
        print("\n")

    elif hacer == "3": 
        print("\n")        
        for key in clientes:
            for a in clientes[key]:
                # si el cliente no es preferente se imprime
                if a == False:
                    print(clientes[key])
        print("\n")

    elif hacer == "1":
        print("\n")
        for key in clientes:
            #Se imprimen todos los clientes
            print(clientes[key])
        print("\n")
    else:
            print("Error con la eleccion \n") 

#funcion para ver los promedios de los clientes
def edad():
    

    edad_total = 0
    print(" Edad promedio de todos los clientes     ('1') \n",
          "Edad promedio delos cliente preferentes ('2') \n")

    #input para la eleccion     
    do = input(": ")

    if do == "2":
        print("\n")
        cont = 0
        for key in clientes:
            for a in clientes[key]:
                # si el cliente es preferente se suma su edad al total
                if a == True:
                    edad_total += clientes[key][1]
                    cont += 1
        print("\n")            
        #Se imprime el promedio
        print("Edad promedio de los clientes preferentes: ", edad_total/cont)            

    elif do == "1":
        print("\n")
        for key in clientes:   
         #Se suma la edad de los clientes al total 
           edad_total += clientes[key][1]
        
        #Se imprime el promedio
        print("Edad promedio de todos los clientes: ", edad_total/(len(clientes))) 
        print("\n")
    else:  
        print("Error con la eleccion \n")   

