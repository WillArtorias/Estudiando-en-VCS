#def msg():
#    return "Mensaje de prueba" 
#x=msg()
#print(x)
#def good_morning ():
#    greetings="Hello , Good Morning!"
#    return greetings
#msg=good_morning ()
#print(msg)
#def saludo (name):
#        print ("Hello {}".format(name))
#name=input("Tell me you name :--")
#saludo(name)
#def calc(x,y):
#   q=x//y
#    r=x%y
#    return q , r
#co=int(input("Introduce dividendo:"))
#re=int(input("Introduce divisor: "))
#co,re=calc(x=co,y=re)
#print(co)
#print(re)
#def sum_numbers(*numbers):
#    sum=0
#    media=0
#    for n in numbers:
#        sum+=n
#    return sum
#print(sum_numbers(2,2,2,2,10))          
#def complete_name(name,**surname):
#    print("El full name es:{}".format(name),end="")
#    for i in surname.items():
#        print("{}".format(i[1]),end="")
#complete_name(name="Will",surname="Gomez",surname0="Fernandez")
def mult(x,y=2):
    return x*y
print(mult(8))
def sum(x,y=5,w=4):
    return x+y*w
print(sum(5))
def promedio(x,y=5):
    return x//y
print(promedio(40))