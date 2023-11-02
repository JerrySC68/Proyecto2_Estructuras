import re

# Definición de la tabla de símbolos
symbol_table = {}
current_function_type = None

# Analizador léxico
def tokenize(source_code):
    tokens = re.findall(r'\b\w+\b', source_code)
    return tokens

# Analizador sintáctico
def parse_source_code(source_code):
    tokens = tokenize(source_code)
    current_type = None
    current_name = None
    inside_function = False

    for i, token in enumerate(tokens):
        if token in ['int', 'float', 'string', 'void']:
            current_type = token
        elif token == '{':
            if current_name and current_type:
                symbol_table[current_name] = current_type
            current_type = None
            current_name = None
            inside_function = True
        elif token == '}':
            inside_function = False
        elif current_type and not inside_function:
            current_name = token
            if current_name not in symbol_table:
                symbol_table[current_name] = current_type
            else:
                print(f"Error - Línea {i + 1}: '{current_name}' ya está declarado")
        elif current_function_type and token == 'return':
            return_type = tokens[i + 1]
            if return_type != current_function_type:
                print(f"Error - Línea {i + 1}: Valor de retorno no coincide con la declaración de la función")



# Código fuente de ejemplo
source_code = """
int x = 40
void funcion(float v, string n){
 if (v > 0.0){
 n = “Mayor”
 x = x + 5
 }
}
"""

# Crear la tabla de símbolos
parse_source_code(source_code)

# Imprimir la tabla de símbolos
print("Tabla de Símbolos:")
for name, data_type in symbol_table.items():
    print(f"Nombre: {name}, Tipo: {data_type}")
