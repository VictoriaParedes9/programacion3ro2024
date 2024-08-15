n=int(input("Ingrese un numero: "))
if n>0 and n<=9:
   print("n es una unidad")
elif n>9 and n<=100:
     print("n es una decena")
elif n>99 and n<=1000:
    print("n es una centena")  
elif n>999 and n<=100000:
     print("n es una milena")  
else:
    print("n es mayor a 100.000")