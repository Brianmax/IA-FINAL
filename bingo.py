import random
import time
#Crear una lista de números enteros.
def listaNum(start, end):
  lista = []

  for x in range(start,end+1):
    lista.append(x)

  return lista

def Cartillas(inicio, fin, cantidad): #parámetros: inicio y final de la lista
                                            # y cantidad de números elegidos

    lista = listaNum(inicio, fin)     #crear una lista de números para un grupo específico
    listaNueva = []
    for x in range(cantidad):
        a = random.randint(0,len(lista)-1)  #Elegir un índice al azar de la lista
        n = lista[a]                  #Escoger el elemento de la lista correspondiente a dicho índice
        listaNueva.append(n)
        lista.pop(a)
    print(listaNueva)
    return listaNueva

def indice(listaNueva, elemento):
    index = 0
    for e in listaNueva:
        if e == elemento:
            return index
        index = index + 1
def bolillas(listaNueva):
  lista = listaNum(1, 20)
  while len(lista) > 0:
    a = random.randint(0, len(lista)-1)
    n = lista[a]
    print(n, end=" ")
    lista.pop(a)
    if n in listaNueva:
        index = indice(listaNueva, n)
        listaNueva.pop(index)
    print()
    time.sleep(5)
    print(listaNueva)

listaNueva = Cartillas(1,20,16)
bolillas(listaNueva)
