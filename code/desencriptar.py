from ClaveDes import  *
from Des2 import *
from Des3 import *
#e=Encriptar("0001 0010 0011 0100 0101 0110 0111 1000 1001 1010 1011 1100 1101 1110 1111 0001","0100 0101 0100 1010 0100 0101 0100 1101 0101 0000 0100 1100 0100 1111 0100 1101")
#e.main()
class Desencriptar:
    def __init__(self,clave,mensaje):
        self.logFile=[]
        self.obtener_Clave=ClavesDes()
        self.funciones_Secundarias=FuncionesSecundarias()
        self.final=DesFinal()
        self.switch=[]
        self.clave=clave
        self.mensaje=mensaje
#-------------------------------------Seccion de las claves    
    def getClaves(self):
        self.obtener_Clave.cifrar(self.clave)
        
    def getPcLog(self):
        self.logFile.append("El Pc obtenedidos de la clave")
        pc=self.obtener_Clave.pc
        self.logFile.append("Pc: "+str())
        return pc

    def getCiLog(self):
        self.logFile.append("-----------------------------------------------------------------------")
        self.logFile.append("Los Ci obtenedidos de la clave")
        ci=self.obtener_Clave.matrizRotacionesCi
        for i in range(len(ci)):
            texto="C"+str(i)+" "+str(ci[i][0])
            self.logFile.append(texto)
        self.logFile.append("\n")
        return ci
    
    def getDiLog(self):
        self.logFile.append("-----------------------------------------------------------------------")
        self.logFile.append("Los Di obtenedidos de la clave")
        di=self.obtener_Clave.matrizRotacionesDi
        for i in range(len(di)):
            texto="D"+str(i)+" "+str(di[i][0])
            self.logFile.append(texto)
        self.logFile.append("\n")
        return di
    
    def getKiLog(self):
        self.logFile.append("-----------------------------------------------------------------------")
        self.logFile.append("Los Ki obtenedidos de la clave")
        ki=self.obtener_Clave.matrizK
        for i in range(len(ki)):
            texto="K"+str(i)+" "+str(ki[i])
            self.logFile.append(texto)
        self.logFile.append("\n")
        return ki
    def getKi(self):
        return self.obtener_Clave.matrizK

    def getLog(self):
        for i in self.logFile:
            print(str(i))
#-------------------------------------Seccion del mensaje
#mensaje 0100 0101 0100 1010 0100 0101 0100 1101 0101 0000 0100 1100 0100 1111 0100 1101
    def getIP(self):
        return self.funciones_Secundarias.funcionIP(self.mensaje)

    def getR(self):
        return self.funciones_Secundarias.getR()

    def getL(self):
        return self.funciones_Secundarias.getL()
    def getMensaje(self):
        lista=self.logFile[-1].split(":")
        mensaje=lista[1]
        return mensaje
    def cifradoFinal(self):
        self.logFile.append("\n")
        self.logFile.append("\n")
        self.logFile.append("\n")
        self.logFile.append("-----------------------------------------------------------------------")
        self.logFile.append("Paso Final")
        self.switch=[self.getL(),self.getR()]
        self.logFile.append("L0: "+str(self.getL()))
        self.logFile.append("R0: "+str(self.getR()))
        longitud=len(self.getKi())
        for i in range(longitud):
            expansion=self.funciones_Secundarias.expansionE(self.switch[1])
            self.logFile.append("Expansion E: "+str(self.funciones_Secundarias.agrupasicon(expansion)))

            k=self.getKi()[longitud-i-1]
            self.logFile.append("\n")
            self.logFile.append("-----------------------------------------------------------------------")
            self.logFile.append("K"+str(i)+": "+str(self.getR()))

            ki_er0=self.final.xor(expansion,k)
            self.logFile.append("\n")
            self.logFile.append("-----------------------------------------------------------------------")
            self.logFile.append("KI ⊕ ER0: "+str(self.final.agrupasicon(ki_er0)))

            cajas=self.final.ultimoPaso(ki_er0)
            self.logFile.append("\n")
            self.logFile.append("-----------------------------------------------------------------------")
            self.logFile.append("Aplicando cajas: "+str(self.final.agrupasicon4(cajas)))

            permutacion=self.final.agrupasicon4(self.final.permutacion(cajas))
            self.logFile.append("\n")
            self.logFile.append("-----------------------------------------------------------------------")
            self.logFile.append("F(R"+str(i+1)+",k"+ str(i+1) +"):"+str(permutacion))

            r0=permutacion.replace(" ","")
            self.switch[1]=self.switch[0]
            self.switch[0]=r0
    
    def main(self):
        self.getClaves()
        self.getPcLog()
        self.getCiLog()
        self.getDiLog()
        self.getKiLog()
        self.getIP()
        self.cifradoFinal()
        self.getMensaje()