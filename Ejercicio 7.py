
#Se crean las listas para almacenar la informacion 
pasajeros_dic = {}
pasajerosPref_dic = {}


def Input_Data():

    #Se crea un bucle para agregar clientes
    while True:
        #Se pide el INE y si el input es igual a x se cierra el bucle
        INE = input("INE o IFE del pasajero: ")
        INE = INE.upper()
        if INE == "X":
            print("\n")
            break

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
            prefer = input("Cliente preferente (Si/No):")
            prefer = prefer.upper()

            #Se abre If para que el input solo sea 'SI' o 'NO'
            if prefer == "SI":
                preferential = True
                pasajerosPref_dic [INE] = [name, age, iata, preferential]
                print("Pasajero agregado \n")

                break
            elif prefer == "NO":
                preferential = False
                pasajeros_dic [INE] = [name, age, iata, preferential]
                print("Pasajero agregado \n")

                break
            else:
                print("Error con la preferencia \n")
            
#Se llama la funcion

Input_Data()
#Se imprimen los datos

print("\n")
print("pasajeros no preferentes")
print(pasajerosPref_dic)
print("\n")
print("pasajeros no preferentes")
print(pasajeros_dic)