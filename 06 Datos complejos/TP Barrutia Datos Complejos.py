
#Ejercicio 1 ,2,3,4

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 
1450} 
#Naranja = 1200 
#● Manzana = 1500 
#● Pera = 2300 
precios_frutas['Naranja']=1200
precios_frutas['Manzana']=1200
precios_frutas['Pera']=1200

#● Banana = 1330 
#● Manzana = 1700 
#● Melón = 2800

precios_frutas['Banana']=1330
precios_frutas['Manzana']=1700
precios_frutas['Melon']=2800



lista_de_frutas = precios_frutas.keys()

print(lista_de_frutas)

#Ejercicio 4
cont=1
nombres= input("Ingrese un nombre: ")
celulares= int(input("Ingrese el numero de celular: "))
contactos= {nombres : celulares}
while cont <=4 :
    nombre= input("Ingrese un nombre: ")
    celular= int(input("Ingrese el numero de celular: "))
    contactos[nombre] = celular
    cont+=1

print(contactos)

name = input ("Ingrese el nombre: ")

if name in contactos :
    print (f"El numero de telefono de {name} es : ")
    print (contactos[name])


#ejercicio 5 
frase = input("Escriba una frase : ")
palabras_lista= frase.split(" ")
set_palabras=set(palabras_lista)


#Armo diccionario para que acumule las veces repetidas
recuento= {}
for palabras in palabras_lista :
    if palabras in recuento :
        recuento[palabras] +=1
    else :
        recuento[palabras] = 1 

print(recuento)


#ejercicio 6 
cont=0

nombre= input("Ingrese el nombre del estudiante : ")
nota1= int(input("Ingrese la nota 1  del estudiante: "))
nota2= int(input("Ingrese la nota 2  del estudiante: "))
nota3=int(input("Ingrese la nota 3 del estudiante: "))
registro_notas = (nota1 , nota2, nota3 )
promedio= (nota1 + nota2 + nota3 )/3
diccionario= {nombre : registro_notas}
diccionario_promedio={nombre : f"el promedio es :  {promedio}"}



while cont<2 : 
    nombre= input("Ingrese el nombre del estudiante : ")
    nota1= int(input("Ingrese la nota 1  del estudiante: "))
    nota2= int(input("Ingrese la nota 2  del estudiante: "))
    nota3=int(input("Ingrese la nota 3 del estudiante: "))
    registro_notas = (nota1 , nota2, nota3 )
    diccionario[nombre]= registro_notas
    promedio= (nota1 + nota2 + nota3 )/3
    diccionario_promedio[nombre]=f"el promedio es :  {promedio}"

    cont +=1

print(diccionario)
print(diccionario_promedio)

#ejercicio 7 
parcial1={1,2,3,4,5}
parcial2={4,5,6,7,8}

ambos= parcial1 & parcial2
solo_uno= parcial1 ^ parcial2 # o incluyente, devuelve verdaeero si 2 son verdaderos, 1+0=1 , 1+1=1 
al_menos_uno= parcial1 | parcial2 # o excluyente o exclusivo devuelve verdadero si y s solo si uno de los operandos es verdadero. 1+1=0
print(ambos)
print(solo_uno)
print(al_menos_uno)

#ejercicio 8 
def consulta_stock(diccionario) :
    articulo= input("Ingrese el articulo: ")
    return diccionario[articulo]
def cambiar_stock(diccionario) :
    articulo= input("Ingrese el articulo: ")
    if articulo in diccionario :
        stock =int(input ("Indique la cantidad a actualizar: "))
        diccionario[articulo]=stock 
    else:
        stock=int(input ("Indique la cantidad : "))
        diccionario[articulo]=stock

stock_cosas= {"Pantalones": 6 , "Remeras":2, "Buzos" : 5, " Camperas": 6 ,"Shorts": 4}

print(consulta_stock(stock_cosas))
cambiar_stock(stock_cosas) # Le saco el print porque sino imprime None, no tiene nada para imprimir.. solo cambia el stock 
print(stock_cosas)

#ejercicio 9 
agenda= { ("Lunes" , "9:00"): "Desayuno", ("Lunes" , "11:00"): "Yoga" , ("Martes" , "10:00"): "Gimasia" ,  ("Miercoles" , "12:00"): "Almuerzo" ,  ("Jueves" , "14:00"): "Merienda"}

dia= input("Ingrese el dia: ")
hora= input("Ingrese la hora: ")
clave_agenda= (dia, hora)
if clave_agenda in agenda :
    print(agenda[clave_agenda])
else : 
    print("No hay eventos para ese dia")



#Ejercicio 10
diccionario_1= {"Argentina" : "Buenos Aires", "Brasil": "San pablo", " Cuba": " La habana", " Bolivia": "La paz"}
diccionario_2 = {}

for paises, capitales in diccionario_1.items():
    diccionario_2[capitales]= paises
print(diccionario_2)