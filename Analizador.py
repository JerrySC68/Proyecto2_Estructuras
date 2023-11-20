import re
import queue
import array
import hashlib
import palabrasReservadas
from io import open



class Analizador:
    """
    Clase: Analizador
    Esta clase se encargará de analizar y compilar todo el código fuente usando Hashing e
    indica sí tuvo una compilación exitosa o, en caso contrario, cuales fueron los errores
    dentro del código fuente.

    Atributos
    ----------

    - hashFunc: Diccionario para funciones.
    - hashVar: Diccionario para variables.
    - error: Arreglo para guardar errores del código.
    - codigo (string): Para guardar el código.
    - mensjeError (string): Para guardar mensajes de error.
    - iterad (int): Para iterar arreglos a lo largo de la clase.
    - fun: stack para las funciones del código fuente.
    - toString: stack para cadenas.
    - variables: stack para las variables del código fuente.
    - primeraL (int): Para indicar en que línea del código fuente se encuentra el error.
    - codigoFuente: Para almacenar el código fuente a compilar.
    - check: Arreglo para verificaciones.

    Métodos
    ----------

    - __init__() : Constructor de la clase.
    - hashing() : Para realizar la función hash y retornar el unicode.
    - appendDiccionarioFun(): Para agregar la función al diccionario respectivo.
    - appendDiccionarioVar(): Para agregar la variable al diccionario respectivo.
    - cantLlaves(): Para verificar si las llaves están balanceadas.
    - verificaParam(): Para agregar el contenido de los parámetros. 
                        de las funciones dentro del diccionario de variables.
    - verificaExistencia_d(): Para verificar la existencia de una variable dentro del diccionario respectivo.
    - verificaExistencia(): Para el Wrapper verificaExistencia_d().
    - imprimirFuncion(): Para imprimir el código.
    - muestraErrores_d(): Para mostrar los errores del código fuente o si fue exitosa la compilación.
    - muestraErrores(): Para el Wrapper muestraErrores_d().
    - checkParam(): Para verificar el contenido dentro de los parámetros.
    - leeArchivo(): Para el Wrapper de leeArchivo_d().
    - leeArchivo_d(): Para leer el archivo del código fuente.
    - __leer_String(): Para analizar todas las lineas de código fuente 
                        además usa distintos métodos de la clase para eso.
    """


    def __init__(self):

        self.hashFunc={}
        self.hashVar={}
        self.error=[] 
        self.codigo=""
        self.mensjeError=""
        self.iterad=0 
        self.fun=queue.LifoQueue()
        self.toString = queue.LifoQueue()
        self.variables=queue.LifoQueue()
        
        self.primeraL=1
        self.codigoFuente=[]
        self.check=[]


    def hashing(self, ID):
        """
        Toma un ID y retorna un valor hash.
        """
        aux=0
        for iterad in ID:        #ord sirve para obtener el valor ASCII de un carácter.
            aux += ord(iterad)   #retorna el unicode de el caracter enviado.
        return aux % 20
        

    def appendDiccionarioFun(self, objeto):
        """
        Añade objeto al diccionario de Funciones y usa la función hashing para obtener la clave.
        """
        key = self.hashing(objeto.nombre)
        key +=self.iterad
        self.hashFunc[key]=objeto
        self.iterad =0 
        
    
    def appendDiccionarioVar(self, objeto):
        """
        Añade objeto al diccionario de Variables y usa la función hashing para obtener la clave.    
        """
        key = self.hashing(objeto.nombre)
        key +=self.iterad
        self.hashVar[key]=objeto
        self.iterad =0 
        
    
    def cantLlaves(self, dato):
        """
        Para verificar la cantidad de llaves dentro del código a analizar, osea verifica si las llaves están balanceadas.
        """
        stack=queue.LifoQueue()
        for iterad in range(len(dato)):
            if dato[iterad] == "{":
                stack.put("{")
            elif dato[iterad] == "}":
                if not stack.empty():  #Se asegura de que el stack no este vacio, esto significaría
                    stack.get()        #que no hay una llave que abra dentro del stack
        return stack.empty()   
    

    
    def verificaParam(self, valor, aux):
        """
        #Para verificar el contenido dentro de los parentesís de la función (Parametro) y agregarlos al diccionario de variables.
        """
        declaraciones=[]
        read=""
        for iterad in range(len(valor)):
            if valor[iterad] != " " and valor[iterad] != "," and valor[iterad] != ")":
                read += valor[iterad]
            elif valor[iterad] == '' and valor[iterad-1] == ",":
                a=0
            elif valor[iterad] == "," or valor[iterad] == ")": #Setteamos segun los valores para insertar en diccionario de variables
                palabra=palabrasReservadas.PR()
                palabra.setID("parametro")
                palabra.setNombre(read)
                palabra.setTipo(declaraciones[0])
                palabra.setOrigen(aux)
                self.variables.put(palabra)
                self.check.append(palabra)
                declaraciones.pop()
                read=""
                self.appendDiccionarioVar(palabra)
            else:
                if read != '':
                    declaraciones.append(read)
                read=""
            
  
    def verificaExistencia_d(self, nombre):
        """
        Para verificar la existencia de una variable revisando su respectivo nombre en el diccionario.
        """
        a=self.hashing(nombre)
        a+= self.iterad
        temp=self.hashVar.get(a)
        if temp is not None and nombre != temp.getNombre():
            self.iterad += 1
            self.verificaExistencia_d(nombre)
            return False
        if temp is not None and nombre == temp.getNombre():
            return True
        return False
    

    def verificaExistencia(self, nombre):
        return self.verificaExistencia_d(nombre)
    

    def imprimirFuncion(self):
        """
        Imprime el código
        """
        print(self.codigo)
    

    
    def muestraErrores_d(self):
        """
        Para mostrar errores del código o indicar si no hay. 
        """
        if len(self.error)==0:
            print("Compilación exitosa")
        else:
            for iterad in self.error:
                print("Error:" + iterad)
                
                
    def muestraErrores(self):
        return self.muestraErrores_d()
    

    
    def checkParam(self, dato):
        """
        Para verificar la validez de los parámetros, ver si han sido declaradas en los diccionarios o no.
        Además de indicar en que lineas del código se encuentra el error.
        """
        read=""
        txt=""
        aux=""
        for iterad in range(len(dato)):
            if dato[iterad] == "(":
                break
            if dato[iterad] != " " and dato[iterad] != "(" and dato[iterad] != ")":
                read += dato[iterad] 
                txt=read
        read=""
        for iterad in range(len(dato)):
            if dato[iterad] != " " and dato[iterad] != "(" and dato[iterad] != ")" and dato[iterad] != ",":
                read += dato[iterad]
                aux=read
            elif dato[iterad] == "(":
                val=self.hashing(read)
                val2=self.hashFunc.get(val)
                if val2 is None:
                    self.mensjeError = "Error en la linea: " +str(self.primeraL)+ " la funcion " + read + " no esta declarada."
                    self.error.append(self.mensjeError)
                    return 
                read=""
                    
            elif dato[iterad] == "," or dato[iterad] == ")":
                for a in self.check:
                    if a.getOrigen() == txt:
                        if txt.isnumeric() and txt.find(".") != -1 and a.getTipo() != "float":
                            self.mensjeError = "Error en la linea: " + str(self.primeraL) + "Los parametros no coinciden con la funcion declarada"
                            self.error.append(self.mensjeError)
                        elif txt.isnumeric() and txt.find(".") == 1 and a.getTipo() != "int":
                            self.mensjeError = "Error en la linea: "+str(self.primeraL)+"Los parametros no coinciden con la funcion declarada"
                            self.error.append(self.mensjeError)
                if dato[iterad] == ")":
                    return 
                else:
                    read=""


    def leeArchivo(self, file):
        self.leeArchivo_d(file)
      
    

    def leeArchivo_d(self, file):
        """
        Va leer el archivo.txt con el código fuente, lo almacena en atributo "codigoFuente".
        """
        archivo=open(file, "r", encoding="utf-8") #No solo hay que poner el archivo, también se pone el tipo de codificación.
        valor= archivo.readlines()
        archivo.seek(0)
        self.codigo=archivo.read()
        alfa=" "
        alfa=self.codigo.strip()
        flag=self.cantLlaves(alfa)
        archivo.close()
        for iterad in valor:
            n=iterad
            nuevo=n.strip()           
            self.codigoFuente.append(nuevo)
            self.__leer_String(nuevo,flag)
            self.primeraL += 1

    
    def __leer_String(self, linea,flag):
        """
        Su objetivo es analizar todas las líneas del código en busca de errores,
        indicar en que línea ocurre y cuál es el error. Usa los diccionarios y algunos
        de los métodos de esta clase para realizar el mejor análisis posible.
        """