#Encoding
# -*- coding: utf-8 -*-

class Longitudes(object):

    def __init__(self):
        lista = [1,4,3,2,5,7,8]
        contador = 0
        for i in range(len(lista)):
            contador= contador+1
        print "La longitud es: " + str(contador)

Longitudes()
