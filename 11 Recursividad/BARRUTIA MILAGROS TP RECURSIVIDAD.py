# Ejercicio 1
def factorial_recur(num) :
    if num ==0 :
        return 1
    else :
        return num*factorial_recur(num-1)
    
num= int(input("Ingrese un numero: "))

print(factorial_recur(num))
#Ejercicio 2 


def fibonacci_recursiva(posicion):
    if posicion==0 :
        return 0
    elif posicion==1 :
        return 1
    else :
        return fibonacci_recursiva(posicion-1) + fibonacci_recursiva(posicion-2)
    

posic= int(input("Ingrese la posicion hasta donde quiere calcular la sucesion de Fibonacci: "))

print(fibonacci_recursiva(posic))

#Ejercicio 3
def potencia_recursiva(n,m):
   if m==0 :
      return 1
   else :
      return  n*potencia_recursiva(n, m-1)

n=int(input("Ingrese la base"))
m=int(input("Ingrese el exponente"))

print(potencia_recursiva(n,m))

#ejercicio 4
def numero_binario(n) :
    if n==0 :
        return " "
    else :
        return numero_binario(n//2) + str(n%2)


n=int(input("Ingrese un numero"))
print( numero_binario(n))

#Ejercicio 5 
def es_palindromo(palabra):
    if len(palabra)==0 or len(palabra)==1:
        return True
    elif palabra[0]==palabra[-1]:
        return True
    return es_palindromo(palabra[1:-1])

palabra= input("Ingresa una palabra")
print(es_palindromo(palabra))

#ejercicio 6 
def suma_digitos(digito) :
    if digito==0 :
        return 0
    else :
        return suma_digitos(digito//10) + digito%10
    

digito = int(input (" Ingres eel digito"))

print (suma_digitos(digito))

#ejercicio 7 
def contar_bloques(n) :
    if n==1 :
      return 1
    elif n==0 : 
      return 0  
    else:
      return n + contar_bloques(n-1)
    
  

bloques= int(input ("Indica la cantidad de bloques"))

print(contar_bloques(bloques))

def contar_digito(numero,digito) :
    if numero==0 :
        return 0 
    elif numero==digito%10 :
        return  1 + contar_digito(numero//10,digito)
    else :
        return contar_digito(numero//10,digito)