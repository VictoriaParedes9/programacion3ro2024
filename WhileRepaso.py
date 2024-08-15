prod=[]
rta="si"

while rta=="si" or rta=="si" or rta=="si":
    opcion=input("1. agregar un producto a la lista \n2. mostrar productos de la lista\n3. Salir \n")
    if   opcion=="1":    
         productosAgregar=input("Ingresar el producto a agregar: ")
         prod.append(productosAgregar)
    elif opcion=="2":
        for p in prod:
           print("los productos en la lista son: ",p)
    elif opcion=="3":
         rta=input("Esta seuro de salir del sistema")
         if rta=="no" or rta=="NO" or rta=="No":
          print("Saliendo del Sistema")
    else:
         print("opcion invalida")
    