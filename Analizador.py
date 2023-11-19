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
    

    def verificaParam(self, valor, aux):
        declaraciones=[]
        read=""
        for iterad in range(len(valor)):
            if valor[iterad] != " " and valor[iterad] != "," and valor[iterad] != ")":
                read += valor[iterad]
            elif valor[iterad] == '' and valor[iterad-1] == ",":
                a=0
            elif valor[iterad] == "," or valor[iterad] == ")": #Setteamos segun los valores para insertar en diccionario
                palabra=palabrasReservadas.PR()
                palabra.setIde("parametro")
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
    

    def muestraErrores_d(self):
        if len(self.error)==0:
            print("Compilación exitosa")
        else:
            for iterad in self.error:
                print("Error:" + iterad)
                
                
    def muestraErrores(self):
        return self.muestraErrores_d()
    

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
      
      
    def leeArchivo_d(self, file):
        archivo=open(file, "r", encoding="utf-8")
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
        #Aquí se analizará el código, se usará el hashing y verificaremos los errores, si lo hay...
        stack = queue.LifoQueue()