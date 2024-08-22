numeroentero=[]
while True:
    numero=int(input("ingrese numero entero: "))
    numeroentero.append(numero)
    if numero==0:
        break
print("el valor mayor es:")
print(max(numeroentero))