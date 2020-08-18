class ClavesDes:
    def __init__(self):
        self.listaIteraciones=[1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

        self.matrizPermutaciones=[[57,49,41,33,25,17,9],
                            [1,58,50,42,34,26,18],
                            [10,2,59,51,43,35,27],
                            [19,11,3,60,52,44,36],
                            [63,55,47,39,31,23,15],
                            [7,62,54,46,38,30,22],
                            [14,6,61,53,45,37,29],
                            [21,13,5,28,20,12,4]]

        self.matrizPermutaciones2=[[14,17,11,24,1,5],
                            [3,28,15,6,21,10],
                            [23,19,12,4,26,8],
                            [16,7,27,20,13,2],
                            [41,52,31,37,47,55],
                            [30,40,51,45,33,48],
                            [44,49,39,56,34,53],
                            [46,42,50,36,29,32]]
        self.matrizPermutada=[]
        self.matrizPermutada2=[]
        self.matrizRotacionesCi=[]
        self.matrizRotacionesDi=[]
        self.matrizK=[] 
        self.pc=""
        matrizRotacionesCi=[]
        self.listaRotacionesDi=[]
        
    ##0001 0010 0011 0100 0101 0110 0111 1000 1001 1010 1011 1100 1101 1110 1111 0001
    def cifrar(self,clave):
        c0=""
        d0=""
        clave="0"+(clave.replace(" ",""))    
        for i in self.matrizPermutaciones:
            listaPermutada=[]
            for j in i:            
                listaPermutada.append(clave[j])
            self.matrizPermutada.append(listaPermutada)
        for i in self.matrizPermutada:
            cont2=1
            for j in i:
                if cont2%4==0:
                    self.pc+=" "
                    cont2=1
                self.pc+=j
                cont2+=1
        pc=self.pc.replace(" ","")
        return self.rotacion(pc[0:len(pc)//2],pc[len(pc)//2:])

    def rotacion(self,c0,d0):
        for i in self.listaIteraciones:
            listaRotacionesCi=[]
            self.listaRotacionesDi=[]
            
            c0Tempo=c0[:i]
            c0Sobra=c0[i:]        
            c0Total=c0Sobra+c0Tempo
            listaRotacionesCi=[c0Total]
            c0=c0Total
            self.matrizRotacionesCi.append(listaRotacionesCi)
            
            d0Tempo=d0[:i]
            d0Sobra=d0[i:]
            d0Total=d0Sobra+d0Tempo
            self.listaRotacionesDi=[d0Total]
            d0=d0Total
            self.matrizRotacionesDi.append(self.listaRotacionesDi)
            
        contCi=0
        for i in self.matrizRotacionesCi:
            contCi+=1
        contDi=0
        for i in self.matrizRotacionesDi:
            contDi+=1
        self.permutaciones2()

    def permutaciones2(self):
        matriz=[]
        for i in range(len(self.matrizRotacionesDi)):        
            matriz.append(str(self.matrizRotacionesCi[i][0])+str(self.matrizRotacionesDi[i][0]))

        for lista in matriz:
            lista="0"+str(lista)
            listaPermutada=[]
            for i in self.matrizPermutaciones2:
                for j in i:                
                    listaPermutada.append(lista[j])
            self.matrizPermutada2.append(listaPermutada)
          
        for i in self.matrizPermutada2:
            var=""
            for j in i:
                var=var+j
            self.matrizK.append(var)
