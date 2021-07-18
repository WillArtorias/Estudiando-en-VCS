lista=[]
n=int(input("Que cantidad de numeros desea sumar: "))
for i in range(n):
    lista.append(input("Introduzca numeros para sumar: "))
    i+=n
print("La suma de los numeros es de {}".format(i))    
