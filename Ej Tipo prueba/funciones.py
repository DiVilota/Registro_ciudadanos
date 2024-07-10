def grabar_datos(registro_ciudadano):
    nombres = str(input("Ingrese nombre y apellido: "))
    if all(palabra.isalpha() or palabra.isspace() for palabra in nombres):
        print("Nombres guardados correctamente")
    else:
        print("Sólo se permiten caracteres y espacios!!")


    while True:
        try:
            edad = int(input("Ingrese su edad: "))
            if edad < 15 or edad > 110:
             print("Edad NO válida!!")
            else:
                print("Edad guardada correctamente") 
                break      
        except ValueError:
            print("Edad DEBE ser un número!!")



    while True:
        nif = input("Ingrese NIF: ")
        if len(nif) != 12:
            print("La longitud del NIF es incorrecta!!")
        else:
            print("NIF guardado correctamente")
            break

    personas = {
        'Nombre y apellido' : nombres,
        'Edad'   : edad,
        'NIF'    : nif
    }
    registro_ciudadano.append(personas)

def buscar_ciudadano(registro_ciudadano, nif):
    encontrado = False
    for persona in registro_ciudadano:
        if persona['NIF'] == nif:
            print(f"NIF {persona['NIF']}, {persona['Edad']}, {persona['Nombre y apellido']}")
            encontrado = True
    if not encontrado:
        print("No se puede encontrar a la persona con NIF: ", nif)
        


            

