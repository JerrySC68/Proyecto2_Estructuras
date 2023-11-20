class palabrasReservadas:
    """
     Clase: palabrasReservadas
        Esta clase nos ayudará almacenar los distintos datos
        de funciones y variables del código fuente dentro
        de sus respectivos diccionarios.

    Atributos
    -----------

    - nombre (string): Nombre de la variable o función. 
    - tipo   (string): Tipo de la variable o función. 
    - dato   (string): Dato de la variable o función. 
    - ID     (string): Identificador de la variable o función. 
    - origen (string): Origen de la variable o función. 

    Métodos
    ----------

    - Gets(): Obtiene el atributo.
    - Sets(): Settea el atributo.
    - __init__(): Es el constructor de la clase.
    - toString(): Imprime los atributos de la clase.
    """

    
    def __init__(self):
        """
        Constructor de la clase
        """
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
        """
        Imprime los datos de la clase
        """
        print("Nombre" + self.nombre + '\n')
        print("Tipo" + self.tipo + '\n')
        print("Identificador" + self.ID + '\n')
        print("Origen" + self.origen + '\n')
        print("Dato" + self.dato + '\n')