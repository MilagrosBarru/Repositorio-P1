#Crear lista del 1 al 100 con la funcion range
lista1=list (range(1,101,4))
print (lista1)

#Ejercicio2
lista=[1,2,3,4,5]
print(lista[-2])
#Ejercicio 3
lista_vacia= []
lista_vacia.append("Hola")
lista_vacia.append("Chau")
lista_vacia.append("Dia")
print(lista_vacia)

#EJercicio 4 
animales = ["perro", "gato", "conejo", "pez"] 
animales[-1]= "OSO"
animales[1]="loro"
print(animales)

#ejercicio 5
numeros=[8,15,3,22,7]
numeros.remove(max(numeros))
print (numeros)
#Este codigo lo que hace es remover el maximo de los numeros de la lista numeros, en este caso es 22. 
#Ejercicio 6
lista1=list (range(10,30,5))
print(lista1[0])
print(lista1[1])

#Ejercicio 7 
autos = ["sedan", "polo", "suran", "gol"] 

autos[1]= "Ranger"
autos[2]= "133"

print(autos)

#Ejercicio 8 
dobles=[]

for x in range(5,16,5) :
    dobles.append(x*2)

print(dobles)

#ejercicio 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], 
["agua"]]
#) Agregar "jugo" a la lista del tercer cliente usando append. 
#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente. 
#c) Eliminar "pan" de la lista del primer cliente.  
#d) Imprimir la lista resultante por pantalla


compras[2].append("Jugo")
compras[1][1]="Tallarines"
compras[0].remove("pan")
print(compras)

#ejercicio10
lista_anidada= [[15], [True], [25.5,57.9,30.6], [False]]
print(lista_anidada)