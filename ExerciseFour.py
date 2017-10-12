#Encoding
# -*- coding: utf-8 -*-

class vocales(object):

    def __init__(self):
        bandera = False
        letter = raw_input("Escribe una letra...")
        vowels = ['a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U']
        for y in vowels:
            if y == letter:
                bandera = True
        if bandera == True:
            print "Es una vocal :) !!"
        else:
            print "No es una vocal :( !!"



vocales()