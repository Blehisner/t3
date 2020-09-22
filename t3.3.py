#Autor Ruddy Blehisner Choqueribe Huanca
r=int(input())
a=1
b=0
fibo=0
cont=0
for c in range (a,r+1):
    if cont!=2:
        print(0,end=",")
        cont=cont+1
    else:
        fibo = a + b
        print (fibo,end=",")
        a=b
        b=fibo
        cont=0