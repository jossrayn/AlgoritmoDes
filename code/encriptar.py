from ClaveDes import  *
from Des2 import *
#e=Encriptar()
#e.getClaves("0001 0010 0011 0100 0101 0110 0111 1000 1001 1010 1011 1100 1101 1110 1111 0001")
class Encriptar:
    def __init__(self):
        self.logFile=[]
        self.obtener_Clave=ClavesDes()
        self.funciones_Secundarias=FuncionesSecundarias()
#-------------------------------------Seccion de las claves    
    def getClaves(self,clave):
        self.obtener_Clave.cifrar(clave)
##        print("Pc-1 ",str(self.obtener_Clave.pc))
##        print("Di",str(self.obtener_Clave.matrizRotacionesCi))
##        print("Di",str(self.obtener_Clave.matrizRotacionesDi))
##        print("K",str(self.obtener_Clave.matrizK))
    
    def getPC(self):
        return self.obtener_Clave.pc

    def getCI(self):
        return self.obtener_Clave.matrizRotacionesCi

    def getDI(self):
        return self.obtener_Clave.matrizRotacionesDi

    def getKI(self):
        return self.obtener_Clave.matrizK
        
    def getPcLog(self):
        self.logFile.append("El Pc obtenedidos de la clave")
        self.logFile.append("Pc: "+str(self.obtener_Clave.pc))

    def getCiLog(self):
        self.logFile.append("Los Ci obtenedidos de la clave")
        for i in range(len(self.obtener_Clave.matrizRotacionesCi)):
            texto="C"+str(i)+" "+str(self.obtener_Clave.matrizRotacionesCi[i][0])
            self.logFile.append(texto)
    
    def getDiLog(self):
        self.logFile.append("Los Di obtenedidos de la clave")
        for i in range(len(self.obtener_Clave.matrizRotacionesDi)):
            texto="D"+str(i)+" "+str(self.obtener_Clave.matrizRotacionesDi[i][0])
            self.logFile.append(texto)
    
    def getKiLog(self):
        self.logFile.append("Los Ki obtenedidos de la clave")
        for i in range(len(self.obtener_Clave.matrizRotacionesDi)):
            texto="K"+str(i)+" "+str(self.obtener_Clave.matrizK[i])
            self.logFile.append(texto)

    def getLog(self):
        for i in self.logFile:
            print(str(i))
#-------------------------------------Seccion del mensaje   