                                            #EJErcicio 1
#Definicion de funciones
def imprimir_mensaje() :
    print("Hola mundo")
#programa  principal
imprimir_mensaje()

                                             #ejercicio 2 
#Definicion de funciones                                     
def saludar_usuario(nombre) :
   return (f"Hola{nombre}")
#programa
nombre=input("Ingrese su nombre")
saludar_usuario(nombre)
        
                                              #Ejercicio 3
 
#Definicion de funcion

def informacion_personal(nombre,apellido,edad, residencia) :
 print( f"Soy {nombre} {apellido} tengo {edad} años y vivo en {residencia} ")

#programa principal
nombre= input("Ingrese su nombre")
apellido=input("Ingrese su apellido")
edad= input(" Y su edad? ")
residencia= input("Donde vive")

informacion_personal(nombre,apellido,edad,residencia)
 
                                       #EJERCICIO 4
import math
def calcular_area_circulo(radio):
    return radio**2*math.pi
def perimetro_circulo(radio) :
    return radio*2*math.pi
def pedir_radio():
    radio= int("Ingrese el radio del circulo")
    return radio
 
radio=pedir_radio()
area=calcular_area_circulo(radio)
perimetro=perimetro_circulo(radio)
print(f"El area del circulo de {radio} es {area} y el perimetro es{perimetro}")

                                    #EJERCICIO 5

def segundos_a_horas(segundos):
    horas=segundos/3600
 # 1 hora equivale a 3600 segundos, dividiendo los segundos por 3600 obtengo la cantidad de horas
    return print(f"{segundos} equivalen a {horas}")

#programa principal
segundos=int(input("Ingrese la cantidad de segundos"))
segundos_a_horas(segundos)
 
 #EJERCICIO 6
def tabla_multiplicar(numero) :
     for x in range(1, 11):
      print (x*numero)
     
numero=int (input("Ingrese un numero"))
tabla_multiplicar(numero)

# EJERCICIO 7
def suma(a,b) :
     return   a+b
def resta (a,b) :
     return a-b
def multiplicacion (a,b) :
    return a*b
def division(a,b) :
      if b!=0 :
        return (f"La division entre {a} y {b} es {a/b}")
      elif b==0: 
        return (f"Error. No se puede dividir {a} por 0")


def operaciones_basicas(a,b) :
      print (f"La suma entre {a} y {b} es", suma(a,b))
      print (f"La resta entre {a} y {b} es" , resta(a,b ) )
      print (f"La multiplicacion  entre {a} y {b} es", multiplicacion(a,b))
      print (division(a,b))


#Programa principal
n=float(input("ingrese un numero: "))
n2=float(input("ingrese un numero: "))
 
operaciones_basicas(n,n2)

#EJERCICIO 8
def ingreso_peso():
      n= int(input("Ingrese su peso en kilos"))
      return n
def ingreso_altura() :
     n= float(input("Ingrese la altura"))
     return n 
def calcular_imc(peso,altura) : 
     imc= float(peso/(altura*2))
     return imc

peso=ingreso_peso()
altura=ingreso_altura()
# pongo print, sino no lo imprime. 
print(calcular_imc (peso,altura))


#Ejercicio 9
def celsius_a_farenheit(celsius) :
    temperatura_farenheit= 32*celsius
    return print (f"La temperatura en grados Celsis es {temperatura_farenheit}")

def ingreso_grados():
        numero=int(input("Ingrese los grados celsius"))
        return numero



#Programa principal
grados=ingreso_grados()
celsius_a_farenheit(grados)


#ejercicio 10
def calcular_promedio(a,b,c) :
    promedio=a+b+c/3
    return print(f"El promedio es {promedio}")

def ingreso_numeros():
    n=int(input("Ingrese el primer numero"))
   
    return n

#programa principal
n1=ingreso_numeros()
n2=ingreso_numeros()
n3=ingreso_numeros()
calcular_promedio(n1,n2,n3)