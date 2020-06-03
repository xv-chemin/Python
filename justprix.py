#!/usr/bin/python
# -*- coding: utf-8- -*-

import flask
from random import randint

nbAleatoire = randint(0, 100)
print(nbAleatoire)

nbEntre = input("Quel nombre choisi-tu ? ")
nbEntre = int(nbEntre)
a = 0

essaye = 6


while nbEntre != nbAleatoire and a < 6 and essaye != 1 :
    if nbEntre < nbAleatoire :
        print("c'est plus")
        essaye -= 1
        print("Plus que "+ str(essaye) +" coups")
        nbEntre = int(input("Essaye encore :"))
    elif nbEntre > nbAleatoire :
        print("c'est moins")
        essaye -= 1
        print("Plus que "+ str(essaye) +" coups")
        nbEntre = int(input("Essaye encore :"))
    if nbEntre == nbAleatoire :
        print("Bravo")
    if essaye == 1 :
        print("Perdu")



