import funciones as f
registro_ciudadano = []
while True:
    print("*" * 20)
    print("Registro de Ciudadanos")
    print("")
    print("[1]"  "Grabar datos de Persona")
    print("[2]"  "Buscar Persona")
    print("[3]"  "Guardar datos")  
    print("[4]"  "Salir del pograma...")  
    print("*" * 20)

    try:
            opc = int(input("Ingrese una opción --> "))
            if opc < 1 or opc > 4:
                print("Opción NO válida!")
    except ValueError:
                print("Opción DEBE ser un número!")

    if opc == 1:
          f.grabar_datos(registro_ciudadano)
        
    elif opc == 2:
          while True:
            nif = input("Ingrese NIF a buscar: ")
            if not nif:
               raise ValueError("NIF NO válido!!")
            f.buscar_ciudadano(nif, registro_ciudadano)
          
          
                
            
        
                
                

    elif opc == 4:
        print("Hasta pronto!")
        break

