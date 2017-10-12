#Encoding
# -*- coding: utf-8 -*-

class Mayor(object):

    def __init__(self):
        a = int(raw_input("¿Define el primer numero ?\n"))
        b = int(raw_input("¿Define el segundo numero ?\n"))
        if a > b:
            print "El primer parametro es el mayor tiene el valor " + a
        elif b > a:
            print "El segundo parametro es el mayor tiene el valor " + b
        elif b == a:
            print "Los dos parametros son iguales con los valores " + str(a) + " como b " + str(b)

Mayor()