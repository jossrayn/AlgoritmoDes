from ClaveDes import  *
#e=Encriptar()
#e.getClaves("0001 0010 0011 0100 0101 0110 0111 1000 1001 1010 1011 1100 1101 1110 1111 0001")
class Encriptar:
    def __init__(self):
        self.logFile=[]
        self.obtenerClave=ClavesDes()
    
    def getClaves(self,clave):
        self.obtenerClave.cifrar(clave)
##        print("Pc-1 ",str(self.obtenerClave.pc))
##        print("Di",str(self.obtenerClave.matrizRotacionesCi))
##        print("Di",str(self.obtenerClave.matrizRotacionesDi))
##        print("K",str(self.obtenerClave.matrizK))
    
    def getPC(self):
        return self.obtenerClave.pc

    def getCI(self):
        return self.obtenerClave.matrizRotacionesCi

    def getDI(self):
        return self.obtenerClave.matrizRotacionesDi

    def getKI(self):
        return self.obtenerClave.matrizK
        
    def getPcLog(self):
        self.logFile.append("El Pc obtenedidos de la clave")
        self.logFile.append("Pc: "+str(self.obtenerClave.pc))

    def getCiLog(self):
        self.logFile.append("Los Ci obtenedidos de la clave")
        for i in range(len(self.obtenerClave.matrizRotacionesCi)):
            texto="C"+str(i)+" "+str(self.obtenerClave.matrizRotacionesCi[i][0])
            self.logFile.append(texto)
    
    def getDiLog(self):
        self.logFile.append("Los Di obtenedidos de la clave")
        for i in range(len(self.obtenerClave.matrizRotacionesDi)):
            texto="D"+str(i)+" "+str(self.obtenerClave.matrizRotacionesDi[i][0])
            self.logFile.append(texto)
    
    def getKiLog(self):
        self.logFile.append("Los Ki obtenedidos de la clave")
        for i in range(len(self.obtenerClave.matrizRotacionesDi)):
            texto="K"+str(i)+" "+str(self.obtenerClave.matrizK[i])
            self.logFile.append(texto)

    def getLog(self):
        for i in self.logFile:
            print(str(i))
