
"""
Clase: 
    - palabrasReservadas

Atributos: 
    - nombre
    - tipo
    - dato
    - ID
    - origen

Métodos: 
    - Gets()
    - Sets()
    - __init__() ->Constructor
    - toString()
"""

class palabrasReservadas:
    def __init__(self):
        self.nombre=""
        self.tipo=""
        self.dato=""
        self.ID=""
        self.origen=""

    def setTipo(self, tipo):
        self.tipo = tipo

    def setNombre(self, nom):
        self.nombre = nom

    def setID(self, identificador):
        self.ID = identificador

    def setOrigen(self, origen):
        self.origen = origen

    def setDato(self, dato):
        self.dato = dato
        
    def getOrigen(self):
        return self.origen

    def getNombre(self):
        return self.nombre
    
    def getTipo(self):
        return self.tipo
    
    def getDato(self):
        return self.dato
    
    def getID(self):
        return self.ID
    
    
    def toString(self):
        print("Nombre" + self.nombre + '\n')
        print("Tipo" + self.tipo + '\n')
        print("Identificador" + self.ID + '\n')
        print("Origen" + self.origen + '\n')
        print("Dato" + self.dato + '\n')