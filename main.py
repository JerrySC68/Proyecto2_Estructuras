
"""
Estructuras de Datos
Proyecto 2, 19/11/2023
Jerry Solera 
Reyder Fernández
John Colomer

"""

import Analizador
import palabrasReservadas

if __name__ == '__main__':
    print("Código normal\n")
    Tabla_1 = Analizador.TablaSimbolos()
    Tabla_1.leeArchivo("codigo_fuente.txt")
    Tabla_1.imprimirFuncion()
    Tabla_1.muestraErrores()

    print("\n\n\n\n\n\n")

    print("Código con errores\n")
    Tabla_2 = Analizador.TablaSimbolos()
    Tabla_2.leeArchivo("codigo_fuente_con_error.txt")
    Tabla_2.imprimirFuncion()
    Tabla_2.muestraErrores()


