import sys
import argparse
import src.funcionesPrincipal as op
import src.funcionesClean as opc

def main():   
    args = op.parse()
    nombre = args.nombre
    poke = args.Pokemon
    pok_num = args.Numero_pokemon
    gen = args.Generacion
    print(args)
    print(f"Hola {nombre} bienvenido a la Pokedex de Ironhack")
    if poke:
        return op.pokemon(poke)
    elif gen:
        return op.generationgb(gen)
    elif pok_num:
        return op.poke_num(pok_num)

if __name__ == "__main__":
    main()
