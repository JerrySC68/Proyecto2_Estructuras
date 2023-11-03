import re

class Analizador:
    def __init__(self):
        self.tabla_simbolos = {}
        self.tipo_funcion = None



    def leer_archivo_texto(self, codigo_fuente):
        try:
            with open(codigo_fuente, 'r') as archivo:
                text = archivo.read()
            return text
        except FileNotFoundError:
            print(f"El archivo '{codigo_fuente}' no se encontró.")
            return None
        

    def tokenize(self, codigo_fuente):
        if self.leer_archivo_texto(codigo_fuente) is not None:
            tokens = re.findall(r'\b\w+\b', codigo_fuente)
        return tokens
        
    #Verificamos si la variable es tipo int, float, void, string#
    #def validar_variable:
        

    #Agrega la variable a la tabla de simbolos, antes se tiene que validar la variable#
    #def agregar_variable:
        
    
    #Verificamos si la funcion es tipo int, float, void, string#
    def validar_funcion(self, codigo_fuente): 
        tokens = self.tokenize(codigo_fuente)
        tipo_actual = None     # Tipo de dato de la función (int, void, float o string)#
        nombre_actual = None   # Nombre de la función#
        dentro_funcion = False # Nos indica si estamos dentro de los parámetros de la función (dentro de las {})#

        for i, token in enumerate(tokens):
            if token in ['int','float','string','void']: # Si nos encontramos algunas de estos 4 palabras se refieren al tipo de función y lo guardamos en tipo_actual#
                tipo_actual = token
            elif token == '{': #Agregar contador para verificar cantidad de llaves abiertas para ver las llaves cerradas.
                if nombre_actual and tipo_actual:
                    self.tabla_simbolos[nombre_actual] = tipo_actual
                tipo_actual = None
                nombre_actual = None
                dentro_funcion = True
            elif token == '}':
                dentro_funcion = False
            elif self.tipo_funcion and token == 'return':
                return_tipo = tokens[i + 1]
                if return_tipo != self.tipo_funcion:
                    print(f"Error - Línea {i + 1}: Valor de retorno no coincide con la declaración de la función")



    #Agrega la funcion a la tabla de simbolos, antes se tiene que validar la variable#
    #def agregar_funcion:
    

    #def validar_contenido_funcion posible método a desarrollar#



analizador1 = Analizador()
analizador1.validar_funcion("codigo_fuente.txt")

print("Tabla de Símbolos:")
for name, data_type in analizador1.tabla_simbolos.items():
    print(f"Nombre: {name}, Tipo: {data_type}")

 