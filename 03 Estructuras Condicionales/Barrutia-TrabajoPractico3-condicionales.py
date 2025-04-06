#Actividad 1 

edad_usuario=int(input("Ingrese su edad "))
if edad_usuario>18 :
    print("Eres mayor de edad")

#Actividad 2 

nota =int(input("Ingrese su nota: "))
print("Aprobado") if (nota >= 6) else print("Desaprobado")

#Actividad 3

numero  =int(input("Ingrese un numero par: "))
print("Es un numero par") if (numero%2==0) else print("El numero ingresado es impar. Por favor ingrese un numero par")
numero  =int(input("Ingrese un numero par: "))

#Actividad 4 

dad_usuario= int(input ( "Ingrese su edad : "))

if edad_usuario<12 :
    print ("Categoria:niño")
 #Agrego la segunda condicion : adolescentes
elif  18>edad_usuario>=12 :
    print ("Cateogoria: Adolescente")    
 # Agrego otro elif para condicionar a los adultos jovenes.
elif 30>=edad_usuario>=18 :
    print ("Cateogoria :Adulto joven")
    #  Agrego el else, en otro caso ,solo quedan mayores de 30 que son los adultos
else :
    print ( "Categoria: Adulto" )


#Actividad 5

contraseña= input("Ingrese una contraseña entre 8 y 14 caracteres" )
# len cuenta los caracteres 
if len (contraseña)>=8  and len(contraseña)<=14:
    print ("Ha ingresado una contrasena correcta")
    
else:
    print (" Contraseña invalida. Por favor ingrese una contraseña entre 8 y 14 caracteres")
    contraseña= input("Ingrese una contraseña nuevamente" )
if len (contraseña)>=8  and len(contraseña)<=14:
    print ("Ha ingresado una contrasena correcta") 


#Actividad 6 
# Elige  50 numeros aleatorios entre el 1 y el 100
import random
numeros_aleatorios = [random.randint(1, 100)for i in range(50)]

from statistics import mode,median,mean 
moda=mode(numeros_aleatorios)
mediana=median(numeros_aleatorios)
media=mean(numeros_aleatorios)
print ("Se define con el analisis de los numeros que : ")
if media>mediana>moda:
    print ("El sesgo es positivo")
    print ("La media es " ,media, "la mediana es " ,mediana, " La moda es " ,moda)

elif media<mediana<moda : 
    print ("El sesgo es negativo")
    print ("La media es " ,media, "la mediana es " ,mediana, " La moda es " ,moda)
elif media==moda==mediana:
    print ("sin sesgo")
    print ("La media es " ,media, "la mediana es " ,mediana, " La moda es " ,moda)


#Actividad 7
cadena=input ( "Ingrese una palabra o una frase ")
## cadena-1, imprime la ultima letra de la variable cadena
ultimaletra= cadena[-1] 

if ultimaletra== "a" or  ultimaletra== "e" or ultimaletra== "i" or ultimaletra=="o" or ultimaletra=="u":
    print(cadena + "!")
else:
     print (cadena)

#Actividad 8 

nombre= input("Ingrese su nombre")
#Se imprimen las opcion disponibles
print ("Por favor eliga una opcion luego de leer las opciones")
print("1 , si quiere su nombre en mayusculas")
print("2, si desea su nombre en minisculas")
print("3, si quiere su nombre con la primera letra en mayusculas")
#se solicita al usuario la opcion 
opciones= int (input("Ingrese una opcion:"))

if opciones==1  :
   print(nombre.upper())
elif opciones==2 :
   print(nombre.lower())
elif opciones==3 :
   print(nombre.title())
else:
   print ("No escribio una opcion valida") 

#Actividad 9

magnitud= float(input("Ingrese la magnitud del terremoto"))
if magnitud<3 :
    print("Muy leve.Imperceptible")
elif 4>magnitud>=3 :
    print("Leve ligeramente imperceptible")
elif 5>magnitud>=4 :
    print("Moderado. Sentido por personas pero no causa daños")
elif 6>magnitud>=5 :
     print("Fuerte. Puede causar daños")
elif 7>magnitud>=6 :
    print("Muy fuerte. Puede causar daños")
elif magnitud>=7 :
    print("Extremo. Puede causar dañ8os a gran escala")

#Actividad 10 

hemisferio= input("En que hemisferio se encuentra ")
mes= input("En que mes se encuentra? ")
dia= int(input(" En dia se encuentra "))

# Abro 2 ramas, una para hemisferio sur y otra para hemisferio norte. En cada hemisferio condiciono por mes y limito los dias. 

if hemisferio=="sur" and (mes=="diciembre" and (31>=dia>=21 ) or mes=="enero" and (31>=dia>=1 ) or mes=="febrero" and (28>=dia>=1 )  or mes=="marzo" and (20>=dia>=1 )) :
    print(" Es verano")
elif hemisferio=="sur" and (mes=="marzo" and (31>=dia>=21 ) or mes=="abril" and (30>=dia>=1 ) or mes=="mayo" and (31>=dia>=1 )  or mes=="junio" and (20>=dia>=1 )) :
    print ("Es otoño")
elif hemisferio=="sur" and (mes=="junio" and (30>=dia>=21 ) or mes=="julio" and (31>=dia>=1 ) or mes=="agosto" and (31>=dia>=1 )  or mes=="septiembre" and (30>=dia>=1 )) :
    print ("Es invierno")
elif hemisferio=="sur" and (mes=="septiembre" and (31>=dia>=21 ) or mes=="octubre" and (31>=dia>=1 ) or mes=="noviembre" and (30>=dia>=1 )  or mes=="diciembre" and (20>=dia>=1 )) :
    print("Es primavera")


if hemisferio=="norte" and (mes=="diciembre" and (31>=dia>=21 ) or mes=="enero" and (31>=dia>=1 ) or mes=="febrero" and (28>=dia>=1 )  or mes=="marzo" and (20>=dia>=1 )) :
    print(" Es invierno")
elif hemisferio=="norte" and (mes=="marzo" and (31>=dia>=21 ) or mes=="abril" and (30>=dia>=1 ) or mes=="mayo" and (31>=dia>=1 )  or mes=="junio" and (20>=dia>=1 )) :
    print ("Es primavera")
elif hemisferio=="norte" and (mes=="junio" and (30>=dia>=21 ) or mes=="julio" and (31>=dia>=1 ) or mes=="agosto" and (31>=dia>=1 )  or mes=="septiembre" and (30>=dia>=1 )) :
    print ("Es verano")
elif hemisferio=="norte" and (mes=="septiembre" and (31>=dia>=21 ) or mes=="octubre" and (31>=dia>=1 ) or mes=="noviembre" and (30>=dia>=1 )  or mes=="diciembre" and (20>=dia>=1 )) :
    print("Es otoño")