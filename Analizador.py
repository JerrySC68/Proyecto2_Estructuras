import re

class Analizador:
    def __init__(self):
        self.tabla_simbolos = {}
        self.tokens = None

    def leer_archivo_texto(nombre_archivo):
        try:
            with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
                text = archivo.read()
            return text
        except FileNotFoundError:
            print(f"El archivo '{nombre_archivo}' no se encontró.")
            return None
    #Analiza el contenido del txt y lo extrae en una lista de tokens
    def getTokens(self):
        texto =  leer_archivo_texto("codigo.txt")
        self.tokens = re.findall(r'\b\w+|[\=\+\{\}\(\)\[\]\-]\b', texto)
       

    #Verificamos si la variable es tipo int, float, void, string#
    def validar_variable(self):
        tipoVariable = {"void", "int", "float", "string"}
        for token in  getToken():
            if token in tipoVariable:
                return self.getTokens
           

    #Agrega la variable a la tabla de simbolos, antes se tiene que validar la variable#
    def agregar_variable():
        
        
    #Verificamos si la funcion es tipo int, float, void, string#
    def validar_funcion(): 
    

    #Agrega la funcion a la tabla de simbolos, antes se tiene que validar la variable#
    def agregar_funcion():
    

    #def validar_contenido_funcion posible método a desarrollar#
   

        
    