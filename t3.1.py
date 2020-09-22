#Autor Ruddy Blehisner Choqueribe Huanca
a=int(input("ingrese num inicio: "))
b=int(input("ingrese num final: "))
d=0
sump=0
sumi=0
for c in range (a, b+1):
    print (c,end=" ")
    d=d+1
    if c%2==0:
        sump=sump+c
    else:
        sumi=sumi+c
print(": son ",d," numeros")
print("la suma de los pares es: ",sump)
print("la suma de los impares es: ",sumi)