
import sys
import argparse
import json
import urllib
import requests
import pandas as pd
from pandas import json_normalize
from IPython.display import Image
import matplotlib.pyplot as plt
import src.funcionesClean as opc

def altura(x):
    '''
    Sacamos la altura segun poquemon
    '''
    url = f"https://pokeapi.co/api/v2/pokemon/{x}"
    response = requests.get(url)
    results = response.json()
    return results["height"]

def peso(x):
    '''
    Sacamos el peso segun poquemon
    '''
    url = f"https://pokeapi.co/api/v2/pokemon/{x}"
    response = requests.get(url)
    results = response.json()
    return results["weight"]


def api(x):
    '''
    Utilizamos esta funcion para unicamente llamar una vez a la API en la funcion
    de pokemon y poke_num
    '''
    url = f"https://pokeapi.co/api/v2/pokemon/{x}"
    response = requests.get(url)
    results = response.json()
    return results

def graficos():
    '''
    Con esta funcion, importamos graficos agrupados por generaciones y los imprimimos.
    '''
    from PIL import Image
    data = opc.cleaning('input/pokemon.csv')  
    print(f'Por si te interesa, los datos estadisticos agrupados por generaciones son: ')
    total_gen= data.groupby("Generation").agg({"Attack":"mean", "Defense":"mean",
    }).plot.line()
    plt.title('Media de ataque y defensa por generacion')
    plt.savefig("output/Meanattack.jpg", bbox_inches='tight')
    max_gen = data.groupby("Generation").agg({"Attack":"max", "Defense":"max",
    }).plot.bar()
    plt.title('Ataques y defensas mas altos de cada generación')
    plt.savefig("output/Maxattack.jpg", bbox_inches='tight')
    min_gen = data.groupby("Generation").agg({"Attack":"min", "Defense":"min",}).plot.barh()
    plt.title('Ataques y defensas mas bajos de cada generacion')
    plt.savefig("output/Minattack.jpg", bbox_inches='tight')                                                                              
    img = Image.open('output/Meanattack.jpg')
    img.show() 
    img2 = Image.open('output/Minattack.jpg')
    img2.show() 
    img3 = Image.open('output/Maxattack.jpg')
    img3.show()

def pokemon(x):
    '''
    Con esta funcion, cogemos en nombre de un pokemon y devolvemos sus estadisticas
    '''
    data = opc.cleaning('input/pokemon.csv')
    x= x.lower()
    results = api(x)
    print(f' Te presentamos a {x} , si te esfuerzas, podras ser su amigo, aqui van sus estadisticas:' )
    name = data[(data["Name"]== x.title())]
    ataque = name['Attack'].values[0].round(2)
    print(f'    Su ataque es de {ataque}')
    defensa = name['Defense'].values[0].round(2)
    print(f'    Su defensa es de {defensa}')
    velocidad =name['Speed'].values[0]
    print(f'    Tiene una velocidad de {velocidad}')
    tipo =name['Type 1'].values[0]
    print(f'    Es un pokemon de tipo {tipo}')
    peso = results["weight"]
    altura = results["height"]
    print(f'    Este pokemon mide {altura} centimetros')
    print(f'    Tiene un peso de {peso} gramos')
    return 

def poke_num(x):
    '''
    Con esta funcion, cogemos en numero de un pokemon y sacamos su nombre y estadisticas
    '''
    data = opc.cleaning('input/pokemon.csv')
    results = api(x)
    x = int(x)
    name = data[(data["#"]== x)]
    nombre = name['Name'].values[0]
    print(f' El pokemon numero {x} es {nombre}')
    ataque = name['Attack'].values[0].round(2)
    print(f'     Su ataque es de {ataque}')
    defensa = name['Defense'].values[0].round(2)
    print(f'     Su defensa es de {defensa}')
    velocidad =name['Speed'].values[0]
    print(f'     Tiene una velocidad de {velocidad}')
    tipo =name['Type 1'].values[0]
    print(f'     Es un pokemon de tipo {tipo}')
    peso = results["weight"]
    altura = results["height"]
    print(f'     Este pokemon mide {altura} cm')
    print(f'     Tiene un peso de {peso} gramos')
    return 

def generationgb(x):
    '''
    Con esta funcion, sacamos las estadisticas de una funcion.
    '''
    data = opc.cleaning('input/pokemon.csv')
    x = int(x)
    print(f' Los datos estadisticos de la generacion {x} son:' )
    data1 = data[(data["Generation"]== x)]
    mediaataque = data1[['Attack']].mean().values[0].round(2)
    print(f'  La media de ataque es {mediaataque}')
    mediadefensa = data1[['Defense']].mean(axis=0).values[0].round(2)
    print(f'  La media de defensa es {mediadefensa}')
    maxataque =data1[['Attack']].max(axis=0).values[0]
    print(f'  El mayor ataque es {maxataque}')
    maxdef =data1[['Defense']].max(axis=0).values[0]
    print(f'  La mayor defensa es {maxdef}')
    minataque =data1[['Attack']].min(axis=0).values[0]
    print(f'  El menor ataque es {minataque}')
    mindef =data1[['Defense']].min(axis=0).values[0]
    print(f'  La menor defensa es {mindef}')
    graficos()
    return 


def parse():
    '''
    definimos argumentos 
    '''
    parser = argparse.ArgumentParser(description='Programa de ayuda al entrenador pokemon')
    parser.add_argument('-s', dest='nombre',
                        default='entrenador desconocido',
                        required=True,
                        help="Añade tu nombre aqui")
    group = parser.add_mutually_exclusive_group()                   
    group.add_argument('-a', dest='Pokemon',
                        default=None,
                        required=False, 
                        help='El pokemon del cual queremos info')
    group.add_argument('-g', dest='Generacion',
                        default=None,
                        required=False, 
                        help='La generacion de la cual queremos sacar estadisticas')
    group.add_argument('-n', dest='Numero_pokemon',
                        default=None,
                        required=False,
                        help="Numero del pokemon que queremos sus estadisticas")
                        
    args = parser.parse_args()
    #print(args)
    return args

