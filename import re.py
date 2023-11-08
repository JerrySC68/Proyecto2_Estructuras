import re

def leer_archivo_texto(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            text = archivo.read()
        return text
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no se encontró.")
        return None

source_code = leer_archivo_texto("codigo.txt")
# Encuentra todas las palabras completas en el texto
palabras_encontradas = re.findall(r'\b\w+|[\=\+\{\}\(\)\[\]\-]|[^\S\r\n]+|\n', source_code)
palabras_encontradas = [token for token in palabras_encontradas if not token.isspace() or token == '\n']

def parse_codigo():
    tabla_simbolos = {}
    tipo = None
    nombre = None
    valor = None
    salto_linea = 1
    for i, token in enumerate(palabras_encontradas):
        if token in '\n':
            salto_linea = salto_linea + 1
        if token in ['int', 'float', 'string', 'void']:
            tipo = token
            nombre = palabras_encontradas[i+1]
            tabla_simbolos[nombre] = {"tipo": tipo, "valor": valor}
        
        elif token == '=':
            valor = palabras_encontradas[i+1]
            nombre = palabras_encontradas[i-1]
            comprueba_tipo = palabras_encontradas[i-2]
            if nombre:
                if nombre in tabla_simbolos:
                     for variable, info in tabla_simbolos.items():
                         if variable == nombre and info['tipo'] == 'string':
                             info['valor'] = valor  #actualizar valores en la tabla de simbolos
                         if variable == nombre and info['tipo'] == 'int':
                             info['valor'] = valor  
                         if variable == 'funcion' and info['tipo'] in ['void']:
                             info['valor'] = 'void'
                elif comprueba_tipo not in ['int', 'float', 'string', 'void']:
                    print(f"error en la linea {salto_linea}. variable no declarada")
                       
                    #tabla_simbolos[nombre] = {"tipo": tipo, "valor": valor}
                #else:
                   # print(f"Error - La variable '{nombre}' ya está definida.")
          #  else:
              #  print(f"Error - Declaración incorrecta. en la linea {salto_linea}")
        elif token  == 'if' or token == 'while':
            if palabras_encontradas[i+1] not in '(':
                print(f"error falta un ( despues del {token} en la linea {salto_linea}")
            for a in range (i,):
                if palabras_encontradas[a] == '{':
                    print("  { encontrado"f" en la linea {salto_linea}")
                elif palabras_encontradas[a] != '{' and a == i+19:
                    print(f"error en la linea: {salto_linea}"" . { no encontrado" f" despues del {token}")
        elif token == '\n':
            tipo = None
            nombre = None
            valor = None
    

    

    # Imprimir la tabla de símbolos
    print("Tabla de símbolos:")
    for variable, info in tabla_simbolos.items():
        print(f"Variable: {variable}, Tipo: {info['tipo']}, Valor: {info['valor']}")

print(palabras_encontradas)
parse_codigo()