import random


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
    return listaNueva


def bolillas(listaNueva):
  lista = listaNum(1, 20)
  while len(lista) > 0:
    a = random.randint(0, len(lista)-1)
    n = lista[a]
    print(n, end=" ")
    lista.pop(a)
    print()

listaNueva = Cartillas(1,20,16)
bolillas(listaNueva)
