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

    #Toma un ID y retorna un valor hash
    def hashing(self, ID):
        aux=0
        for iterad in ID:        #ord sirve para obtener el valor ASCII de un carácter.
            aux += ord(iterad)   #retorna el unicode de el caracter enviado.
        return aux % 20
        
    #Añade objeto al diccionario de Funciones y usa la función hashing para obtener la clave
    def appendDiccionarioFun(self, objeto):
        key = self.hashing(objeto.nombre)
        key +=self.iterad
        self.hashFunc[key]=objeto
        self.iterad =0 
        
      #Añade objeto al diccionario de Variables y usa la función hashing para obtener la clave
    def appendDiccionarioVar(self, objeto):
        key = self.hashing(objeto.nombre)
        key +=self.iterad
        self.hashVar[key]=objeto
        self.iterad =0 
        
    #Para verificar la cantidad de llaves dentro del código a analizar
    #Osea verifica si las llaves están balanceadas.
    def cantLlaves(self, dato):
        stack=queue.LifoQueue()
        for iterad in range(len(dato)):
            if dato[iterad] == "{":
                stack.put("{")
            elif dato[iterad] == "}":
                if not stack.empty():  #Se asegura de que el stack no este vacio, esto significaría
                    stack.get()        #que no hay una llave que abra dentro del stack
        return stack.empty()   
    

    #Para verificar el contenido dentro de los parentesís de la función (Parametro) y agregarlos al diccionario de variables.
    def verificaParam(self, valor, aux):
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
            
    #Para verificar la existencia de una variable revisando su respectivo nombre en el diccionario.
    def verificaExistencia_d(self, nombre):
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
        print(self.codigo)
    

    #Nos servirá para mostrar errores del código o indicar si no hay. 
    def muestraErrores_d(self):
        if len(self.error)==0:
            print("Compilación exitosa")
        else:
            for iterad in self.error:
                print("Error:" + iterad)
                
                
    def muestraErrores(self):
        return self.muestraErrores_d()
    

    #Para verificar la validez de los parámetros, ver si han sido declaradas en los diccionarios o no.
    def checkParam(self, dato):
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
      
    
    #Va leer el archivo.txt con el código fuente, lo almacena en atributo "codigoFuente".
    def leeArchivo_d(self, file):
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

    #
    def __leer_String(self, linea,flag):
        #Aquí se analizará el código, se usará el hashing y verificaremos los errores, si lo hay...
        stack = queue.LifoQueue()