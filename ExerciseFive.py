#Encoding
# -*- coding: utf-8 -*-

class calculadora(object):

    def __init__(self):
        self.lista = [1,2,3,4]
        decide = int(raw_input("1.- Sumar \n2.- Multiplicar\n"))
        if decide == 1:
            self.sumar()
        elif decide == 2:
            self.multiplicar()

    def sumar(self):
        resultado = 0
        for i in self.lista:
            resultado = resultado + i
        print "El resultado de la lista es: ", resultado

    def multiplicar(self):
        result = 1
        for i in self.lista:
            result =result * i
        print result


calculadora()
