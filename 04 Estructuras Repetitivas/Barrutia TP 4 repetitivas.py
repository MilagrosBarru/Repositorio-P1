
#Ejercicio 1 
for x in range (0,101) :
    print (x)

#ejercicio2

numero= int(input("Ingresa un numero"))
contador=0

while numero>0 :
    numero=numero//10
    contador+=1
print (f"el numero tiene  {contador} digitos")

#ejercicio 3

num1= int(input("Ingrese el primer numero"))
num2= int(input("Ingrese el segundo numero"))
sumatoria=0

for x in range (num1+1,num2) :
    sumatoria=sumatoria+x
print(sumatoria)

#ejercicio 4
num= int(input("Ingrese un numero"))
sumatoria=0
while num!=0 :
# Coloco la sumatoria primero, asi me toma el primer numero y lo agrega a la sumatoria. Sino pisaba el primer numero ingresaod y no lo sumaba
 sumatoria= sumatoria+num
 num= int(input("Ingrese otro numero"))
print(sumatoria) 

#ejercicio 5 

cont=1
from random import *
numero_aleatorio=(randint(0, 9))

numero=int(input("Ingrese un numero del 1 al 10"))
while numero_aleatorio!= numero :
    numero=int(input("Ingrese otro numero del 1 al 10"))
    cont +=1

print(f"La cantidad de intestos fue: {cont}")

#ejercicio 6
for x in range(100,-2,-2):
 print(x)
 

 #ejercicio 7 
 num=int(input("Ingrese un numero positivo"))
sumatoria=0

if num>0 :
    for x in range(0,num+1) :
     sumatoria= sumatoria+x

    print(sumatoria)

else:
    print("Ingrese un numero positivo por favor")

    #Ejercicio 8 

cantidad_de_numeros=0
numeros_pares=0
numeros_inpares= 0
numeros_negativos=0
numeros_positivos=0
 
while cantidad_de_numeros<100 :
    numeros=int(input("Ingresa un numero"))
    cantidad_de_numeros+=1

    if numeros%2 == 0 :
        numeros_pares +=1
    if numeros%2 != 0 :
     numeros_impares +=1
    if numeros <0 :
     numeros_negativos+=1
    if numeros>0 :
        numeros_positivos+=1
      
print (f"Los numeros pares son {numeros_pares}, los impares son {numeros_impares} los negativos son {numeros_negativos} y los positivos son {numeros_positivos}")

#EJercicio 9 

from statistics import mode, median,mean 
cantidad_de_numeros =0 
#La moda,mediana y media trabajan con listas
lista=[]
while cantidad_de_numeros<5 :
    numeros= int(input("Ingrese un numero"))
# Agrego a la lista los numeros que ingresa el usuario
    lista.append( numeros)
    cantidad_de_numeros+=1

print (f"La moda es {mode(lista)}")
print(f"La mediana es {median(lista)}")
print(f"La media es {mean(lista)}")


#Ejercicio 10
import math
numero= int(input("Ingresa un numero"))
contador=0
inverso=0
digito=0

while numero>0 :
    digito=numero%10
    numero= math.trunc(numero/10)
    inverso=inverso*10+digito

print(inverso)
