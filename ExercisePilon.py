#Encoding
# -*- coding: utf-8 -*-

class pilon(object):

    def __init__(self):
        self.__lista = [4,9,7]
        self.barra()

    def barra(self):
        variable = ""
        for i in range(0,len(self.__lista)):
            for x in range(self.__lista[i]):
                variable = variable + "*"
            print variable

pilon()
