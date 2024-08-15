t=[]
while True:# una condicion
    opcion=input("Menú de opciones\n1-Agregar producto\n2-Eliminar producto\n3-Modificar productor\n4-Mostar productos\n5-Salir \n")#agregamos opciones
    if opcion=="1":# esto es si el usuario toca 1,las distintas opciones que le aparecen
         elementoAgregar=input("Ingrese elemento a agregar:")# creamos una variable para que ingrese
         t.append(elementoAgregar)# agregamos lo que nos pidio el usuario
    elif opcion=="2":#si el usuario toca 2 ,le aparecera la opcion de eliminar
        elementoAeliminar=input("Ingrese el nombre del elemento a modificar: ")#que ingrese el elemento que quiere eliminar
        if elementoAeliminar in t:
           t.remove(elementoAeliminar)#boramos el elemento que nos pidio el ususario
           print("Elemento eliminado exitosamente")    #mostramos que se elimino
        else:#si no se cumple le decimos que no esta
            print("El elemento que desea eliminar no se encuentra en la lista")      
    elif opcion=="3":# si toca 3,va a modificar un elemento de la lista
        elementoAmodificar=input("Ingrese el nombre del elmento a modificar: ")# ingrese lo que quiere modificar de la lista creada anteriormente
        if elementoAmodificar in t:
            elementoModificacion=input("Ingrese el nombre por el que quiere modificar: ")
            index = t.index(elementoAmodificar)
            t[index] = elementoModificacion # usamos el indice para modificar
        else:#si no esta el elemento que el ususario nos pidio modificar 
            print("El elemento que desea modificar no se encuentra en la lista")
           
    elif opcion=="4":#si toca opcion 4, mostramos todo la lista creada anteriormente
        print("Elementos en la lista: \n",t)   #mostramos la lista 
    elif opcion=="5":   #     si toca la opcion 5 sale del sistema    
        print("Saliendo del sistema")
        break
    else:
        print("La opción ingresada es invalida")    #si no ingreso algo vailido le mostramos este cartelSs