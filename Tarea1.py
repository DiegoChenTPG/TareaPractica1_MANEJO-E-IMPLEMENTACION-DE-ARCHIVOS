def inicializar_memoria(size):
    memoria = [0] * size #llenamos de ceros el vector 
    return memoria

def asignar_memoria(memoria):
    for i in range(len(memoria)):
        if memoria[i] == 0: #Este if busca el primer bloque libre y lo ocupa colocandole un 1
            memoria[i] = 1 
            return i
    return -1

def liberar_memoria(indice, memoria):
    for i in range(len(memoria)):
        if i == indice:
            memoria[i] = 0
            print("SE DESOCUPO EL BLOQUE CORRECTAMENTE\n")
            break

memoria_size = 10
memoria = inicializar_memoria(memoria_size)


def pruebas():
    print("ESTADO INICIAL DE LA MEMORIA")
    print(memoria)
    print("\n")

    print("PRUEBA 1: ASIGNACION DE MEMORIA")
    asignacion1 = asignar_memoria(memoria)
    print("Bloque asignado en la posicion "+str(asignacion1)+"\n")


    print("ESTADO DE LA MEMORIA")
    print(memoria)
    print("\n")


    print("PRUEBA 2: ASIGNACION DE MEMORIA Y LIBERACION DE MEMORIA")
    asignacion2 = asignar_memoria(memoria)
    print("Bloque asignado en la posicion "+str(asignacion2)+"\n")
    print(memoria)
    liberar_memoria(asignacion2, memoria)
    print("Bloque liberado en la posicion "+str(asignacion2)+"\n")


    print("ESTADO DE LA MEMORIA")
    print(memoria)
    print("\n")


    print("PRUEBA 3: ASIGNACION DE MEMORIA A TODOS LOS BLOQUES")
    for y in range(memoria_size):
        asignacion = asignar_memoria(memoria)
        if asignacion == -1:
            print("YA NO HAY BLOQUES DISPONIBLES")
            break

    
    print("ESTADO DE LA MEMORIA")
    print(memoria)
    print("\n")   

    print("PRUEBA 4: ASIGNACION DE MEMORIA CUANDO TODOS LOS BLOQUES ESTAN LLENOS")
    otra_asignacion = asignar_memoria(memoria)
    if otra_asignacion == -1:
        print("YA NO HAY BLOQUES DISPONIBLES")

    print("ESTADO DE LA MEMORIA")
    print(memoria)
    print("\n")

    print("PRUEBA 5: LIBERACION DE MEMORIA EN OTRA POSICION EN ESPECIFICO")
    liberar_memoria(5, memoria)
    print("Bloque liberado en la posicion "+str(5)+"\n")


    print("ESTADO DE LA MEMORIA")
    print(memoria)
    print("\n")

pruebas()


print("FIN DEL PROGRAMA")


