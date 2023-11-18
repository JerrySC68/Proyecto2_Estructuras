import re
import queue
import array
import hashlib
import palabrasReservadas
from io import open

class Analizador:
    def __init__(self):
         #Declaracion de diccionarios
        self.hashFunc={}
        self.hashVar={}

        self.error=[] #Arreglo de los errores
        self.codigo=""
        self.mensjeError=""
        self.iterad=0 #Iterador

        #queues que funcionan como un stack
        self.fun=queue.LifoQueue()
        self.toString = queue.LifoQueue()
        self.variables=queue.LifoQueue()
        
        self.primeraL=1
        self.codigoFuente=[]
        self.check=[]

        
    def appendDiccionarioFun(self, obj):
        key = self.hashing(obj.nombre)
        key +=self.iterad
        self.hashFunc[key]=obj
        self.iterad =0 
        
    def appendDiccionarioVar(self, obj):
        key = self.hashing(obj.nombre)
        key +=self.iterad
        self.hashVar[key]=obj
        self.iterad =0 
        
    def cantLlaves(self, dato):
        stack=queue.LifoQueue()
        for iterad in range(len(dato)):
            if dato[iterad] == "{":
                stack.put("{")
            elif dato[iterad] == "}":
                if not stack.empty():  #Se asegura de que el stack no este vacio, esto significaría
                    stack.get()        #que no hay una llave que abra dentro del stack
        return stack.empty()   
    