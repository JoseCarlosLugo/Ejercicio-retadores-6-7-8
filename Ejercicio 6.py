
#Se crean listas para los datos
BJX_list = []
GDL_list = []
JAL_list = []

Data = []

#se crean las varibles para el bucle
name = ""
age = 0
iata = ""

# se crea un bucle para agregar clientes
while True:

    #Se pide el nombre y si el input es igual a x se cierra el bucle
    name = input("Nombre del pasajero: ")
    name = name.upper()
    if name == "X":
        print("\n")
        break

    #Bucle para evitar errores con el input de la edad
    while True:
        #Try y except para que el input solo sea int
        try:
            age = int(input("Edad del pasajero: ")) 
            print("\n")
            break

        except:
            print("Error con la edad \n")


    #input del IATA
    print(
        "Destino      |   Código IATA \n",
        "Guanajuato  |     BJX \n",
        "Guadalajara |     GDL \n",
        "Veracruz    |     JAL \n"
    )

    iata = input("IATA del pasajero: ")
    iata = iata.upper()

    #Se agregan los datos segun su IATA a su lista respectivamente 
    if iata == "BJX":
        #La informacion se agregan en tuplas
        BJX_list.append((iata, name, age))
        print("Pasajero agregado \n")
        print("Para dejar de agregar pasajeros escriba 'X' \n")

    elif iata == "GDL":
        GDL_list.append((iata, name, age))
        print("Pasajero agregado \n")
        print("Para dejar de agregar pasajeros escriba 'X' \n")

    elif iata == "JAL" :
        JAL_list.append((iata, name, age))
        print("Pasajero agregado")
        print("Para dejar de agregar pasajeros escriba 'X' \n")
    else:
        print("Error con el IATA \n")

#If para ver si tienen informacion la listas    
if  (len(BJX_list)) > 0:

    edad_total = 0
    for edad in BJX_list:
        edad_total += edad[2]
        
    len_bjx = (len(BJX_list))    
    promedio = (edad_total/len(BJX_list))

    #Se agregan los datos del promedio de los vuelos a una lista en general 
    BJX_tuple = ("BJX", len_bjx, promedio)    
    Data.append(BJX_tuple)

if (len(GDL_list)) > 0:

    edad_total = 0
    for edad in GDL_list:
        edad_total += edad[2]

    len_gdl = (len(GDL_list))
    promedio = (edad_total/len(GDL_list))

    GDL_tuple = ("GDL", len_bjx, promedio)    
    Data.append(GDL_tuple)

if (len(JAL_list)) > 0:

    edad_total = 0
    for edad in JAL_list:
        edad_total += edad[2]    
            
    len_jal = (len(JAL_list))    
    promedio = (edad_total/len(JAL_list))

    JAL_tuple = ("JAL", len_jal, promedio)    
    Data.append(JAL_tuple)


#Se imprimen los datos
for vuelos in Data:
    print("Detalles de vuelos: ", vuelos[0], ", ", vuelos[1])
    print("Edad promedio por vuelo: ", vuelos[0],", ", vuelos[2], "\n")