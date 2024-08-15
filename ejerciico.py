t=[]
while True:#condición a evaluar
    opcion=input("Menú de opciones\n1-Agregar\n2-Eliminar\n3-Modificar\n4-Mostrar\n5-Salir\n")
    if opcion=="1":
        elementoagregar=input("ingrese elemento a agregar: ")
        t.append(elementoagregar) 
    elif opcion=="2":
        elementoeliminar=input("ingrese el elemento que desea eliminar: ")  
        t.remove(elementoeliminar)   
    elif opcion=="3":
        em=input("ingreae elemento a modificar:")
        if em in t:
           elementomodificar=input("que elemnto desea modificar")
           t[em]=elementomodificar
           print("elemento eliminado con exito")
    else:
        print("el elementoque desea modificar no esta en la lista")
    elif opcion=="4":
    prin("elemento de la lista")
    print("el elemento ")