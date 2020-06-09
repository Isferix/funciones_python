#!/usr/bin/env python
'''
Bucles [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import random
import math

def promedio(lista_numeros):
    '''
    Promedia la suma de los elementos de una lista

    @param 'lista_numeros' Lista que contiene los numeros a promediar
    '''
    sumatoria_numeros = sum(lista_numeros)
    cantidad_numeros = len(lista_numeros)
    promedio = sumatoria_numeros / cantidad_numeros
    #print("El promedio resultante es:", promedio)
    return promedio


def lista_aleatoria(inicio, fin, cantidad):
    '''
    Genera una lista con numeros aleatorios
        
    @param 'inicio' \tNumero que indica el piso de los numeros aleatorios generados\n
    @param 'fin' \tNumero que indica el techo de los numeros aleatorios generados\n
    @param 'cantidad' \tNumero que indica la cantidad de numeros que se generaran
    '''
    lista = []
    for i in range(cantidad):
        lista.append(random.randint(inicio, fin))
    # for numero in lista:
    #     print(numero, " ", end='')
    # print("\n")
    return lista


def ordenar(lista):
    '''Ordena ascendentemente una lista y la imprime en pantalla
    
    @param lista Lista que se ordenara
    '''

   # print(sorted(lista))
    return sorted(lista)


def contar(lista, elemento):
    ''' Devuelve la cantidad de repeticiones de un elemento en una lista
    
    @param lista Lista donde buscaremos el elemento\n 
    @param elemento Elemento que se buscara en la lista'''
    print("{} se repite".format(elemento), lista.count(elemento), "veces")


def buscar(lista, elemento):
    ''' Devuelve el/los indice/s de un elemento dentro de una lista
    
    @param lista Lista donde buscaremos el elemento\n 
    @param elemento Elemento que se buscara en la lista'''
    lista_indices = []
    for indice, numero in enumerate(lista):
        if numero == elemento:
            lista_indices.append(indice)
    # [ numero for numero in [lista.index(numero)] if numero == elemento]
    # print("El elemento {} se encuentra {} veces(vez) en el/los indice/s {}".format(elemento, len(lista_indices), lista_indices))
    return lista_indices


def ej1():
    # Ejercicios con funciones del sistema
    numeros = [2, 4, 6, 8, 10, 12]
    '''
    Realice una funcion llamada "promedio" la cual
    reciba como parámetro una lista de números y calcule
    el promedio de ella como:
    promedio = sumatoria_numeros / cantidad_numeros
    
    Resuelva la sumatoria y la cantidad con las herramientas
    que desee, recomendamos usar las funciones disponibles
    de Python para ello o en tal caso realizar un bucle
    https://docs.python.org/3.7/library/functions.html

    La función debe retornar el promedio calculado
    La función debe contemplar si se le pasa una lista vacia
    (es decir, de "0" elementos)

    Utilice esa función para calcular el promedio y luego
    imprima en pantalla el resultado
    '''

    promedio(numeros)

def ej2():
    # Ejercicios con modulos del sistema
    inicio = 0
    fin = 10

    # Ejemplo de como obtener un numero aleatorio
    # entre inicio y fin
    # inicio <= numero <= fin
    numero = random.randrange(inicio, fin+1)
    # Documentación oficial de random
    # https://docs.python.org/3.7/library/random.html

    '''
    Realice una funcion llamada "lista_aleatoria" la cual
    reciba como parámetro el rango de aceptación de la lista
    "inicio y fin" y la cantidad de elementos que deseamos que
    contenga la lista, es decir, la cantidad de elementos random a generar.
    def lista_aleatoria (inicio, fin, cantidad)

    Dicha función debe retornar la lista de elementos random generados.
    '''
    # numeros = lista_aleatoria (inicio, fin, cantidad)
    lista_1 = lista_aleatoria(inicio, fin, 10)
    # Imprima en pantalla la lista de elementos generados
    # print(....)
    for numero in lista_1:
        print(numero, sep=',', end=',')
    # Utilice el método random.choice para obtener 2 numeros
    # de la lista de elementos generados
    # numero_1 = random.choice(...)
    # numero_2 = random.choice(...)
    numero_1 = random.choice(lista_1)
    numero_2 = random.choice(lista_1)

    # Importar en este programa/documento el modulo "math"
    # Calcular la raiz cuadrada (square root) de esos
    # dos numeros obtenidos utilizando el método del
    # módulo "math" que crea correspondiente
    # Documentación oficial de math
    # https://docs.python.org/3.7/library/math.html
    # NOTA: Puede buscar en el medio que prefiera la info
    # solicitada
    # raiz_cuadrada_1 = ....
    # raiz_cuadrada_2 = ....
    raiz_cuadrada_1 = math.sqrt(numero_1) 
    raiz_cuadrada_2 = math.sqrt(numero_2)
    print("\nLa raiz cuadrada del numero 1 es: {0:.2f}".format(raiz_cuadrada_1))
    print("La raiz cuadrada del numero 2 es: {0:.2f}".format(raiz_cuadrada_2))

def ej3():
    # Ejercicios de listas y métodos
    numeros = [2, 4, 6, 8, 10, 12]

    '''
    Generar una una nueva funcion que se llame "ordenar",
    que utilizaremos para odernar la lista de numeros.
    Dentro de la función puede ordenar la lista
    usando bucles o las funciones nativas de Python
    La función no hace falta que retorne la lista ordenada,
    ya que al tratarce de una lista se pasa como referencia
    a la función (es decir que las modificaciones realizadas
    en la función afectan a la variable pasada como argumento)

    '''

    ordenar(numeros)

def ej4():
    # Ejercicios de listas y métodos
    cantidad_numeros = 5

    '''
    Utilice la función "lista_aleatoria" para generar
    una lista de 5 números en un rango de 1 a 9 inclusive

    Generar una nueva funcion que se llame "contar",
    que cuenta la cantidad de veces que un elemento pasado
    por parámetro se repite en la lista.
    Para saber cuantas veces se repiten el elemento pasado 
    en la lista pueden usar bucles o el método nativo de list
    "count"

    '''

    # Por ejemplo creo una lista de 5 elemtnos
    # lista_numeros = lista_aleatoria(...,...,cantidad_numeros)
    # Luego quiero averiguar cuantas veces se repite el numero 3
    # cantidad_tres = contar(lista_numeros, 3)

    lista_1 = lista_aleatoria(1, 9, 5)
    contar(lista_1, 3)
    
def ej5():
    # Ejercicios de listas y métodos
    cantidad_numeros = 5

    '''
    Utilice la función "lista_aleatoria" para generar
    una lista de 5 números en un rango de 1 a 9 inclusive

    Generar una una nueva funcion que se llame "buscar",
    que genere una lista con los índice de las posiciones
    en donde se encuentra dicho elemento en la lista.
    Si el elemento en la lista no existe, la función
    debe retornar una lista vacia.
    Para encontrar los índices del elemento en la lista
    puede usar el método "index" o bucles.
    Recuerde que el elemento puede repetirse más de una
    vez en la lista.
    '''
    # Por ejemplo creo una lista de 5 elemtnos
    # lista_numeros = lista_aleatoria(...,...,cantidad_numeros)
    # Luego quiero averiguar cuantas veces se repite el numero 3
    # cantidad_tres = contar(lista_numeros, 3)
    lista_1 = lista_aleatoria(1, 9, cantidad_numeros)
    buscar(lista_1, 5)


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    #ej5()
