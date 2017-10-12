#Encoding
# -*- coding: utf-8 -*-

class Maximo_tres(object):

    def __init__(self):
        a = int(raw_input("¿Primer parametro? \n"))
        b = int(raw_input("¿Segundo Parametro? \n"))
        c = int(raw_input("¿Tercer Parametro? \n"))
        mayor = 0
        if a > b:
            mayor = a
            if mayor > c:
                print "El primer parametro es el mayor"
            elif b > a:
                mayor = b
                if mayor > c:
                    print "El segundo parametro es el mayor"
            elif c > a:
                mayor = c
                if mayor > b:
                    print "El tercer parametro es el mayor"
        #print mayor

Maximo_tres()