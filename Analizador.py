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



    #Modificar de aquí hasta abajo...


    def leer_archivo_texto(self, codigo_fuente):
        try:
            with open(codigo_fuente, 'r') as archivo:
                text = archivo.read()
            return text
        except FileNotFoundError:
            print(f"El archivo '{codigo_fuente}' no se encontró.")
            return None
        

    #def tokenize(self, codigo_fuente):
    #    if self.leer_archivo_texto(codigo_fuente) is not None:
    #        tokens = re.findall(r'\b\w+\b', codigo_fuente)
    #        return tokens
    #    return None

    def tokenize(self, source_code):
        tokens = re.findall(r'\b\w+\b', source_code)
        return tokens
        
    
    #Verificamos si la funcion es tipo int, float, void, string#
    def validar_funcion(self, codigo_fuente): 
        tokens = self.tokenize(codigo_fuente)
        tipo_actual = None     # Tipo de dato de la función (int, void, float o string)#
        nombre_actual = None   # Nombre de la función#
        dentro_funcion = False # Nos indica si estamos dentro de los parámetros de la función (dentro de las {})#

        if tokens is not None:
            for i, token in enumerate(tokens):
                if token in ['int','float','string','void']: # Si nos encontramos algunas de estos 4 palabras se refieren al tipo de función y lo guardamos en tipo_actual#
                    tipo_actual = token
                elif token == '{': #Agregar contador para verificar cantidad de llaves abiertas para ver las llaves cerradas.
                    if nombre_actual and tipo_actual:
                        self.tabla_simbolos[nombre_actual] = tipo_actual
                        self.tipo_funcion = tipo_actual
                    tipo_actual = None
                    nombre_actual = None
                    dentro_funcion = True
                elif token == '}':
                    dentro_funcion = False
                elif tipo_actual and not dentro_funcion:
                    nombre_actual = token
                elif self.tipo_funcion and token == 'return':
                    return_tipo = tokens[i + 1]
                    if return_tipo != self.tipo_funcion:
                        print(f"Error - Línea {i + 1}: Valor de retorno no coincide con la declaración de la función")





 