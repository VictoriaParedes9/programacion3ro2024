zapatilla={"01":{"modelo":"clasicc","material":"croslite","numero":39,"cantidad en stok":16}, "02":{"Modelo":"convers","material":"lona de algodon","numero":40,"cantidad en stok":"57"},"03":{"modelo":"nike","material":"algodón orgánico certificado","numero":35,"cantidad de stok":30}}

while True:
    opcion=input("ingrese una de las siguientes opciones: \n1 Mostrar zapatillas en stock \n2 Agregar zapatilla al stock \n3 salir \n")
    if opcion=="i":
        print("_____________________________")
        print("_________zapatillas__________")
        print("_____________________________")
        for c,v in zapatilla.items():
            print(c,":", v)
            print("_______________________")
    elif opcion=="2":
        zapatillaAgregar=input("Escriba el codigo de zapatilla a agregar al stock: ")
        MODELO=input("Escriba el modelo de zapatila que desea agregar: ")
        MATERIAL=input("Escriba el material de zapatillas agregar: ")
        NUMERO=input("Escribir el numero de zapatillas a agregar: ")
        CANTIDADSTOCK=input("ingrese la cantidad en stock de zapatillas a agregar: ")
        zapatilla[zapatillaAgregar]=MODELO,MATERIAL,NUMERO,CANTIDADSTOCK
    elif opcion==3:
        break
    
