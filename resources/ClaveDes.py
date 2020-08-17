
listaIteraciones=[1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

matrizPermutaciones=[[57,49,41,33,25,17,9],
                     [1,58,50,42,34,26,18],
                     [10,2,59,51,43,35,27],
                     [19,11,3,60,52,44,36],
                     [63,55,47,39,31,23,15],
                     [7,62,54,46,38,30,22],
                     [14,6,61,53,45,37,29],
                     [21,13,5,28,20,12,4]]

matrizPermutaciones2=[[14,17,11,24,1,5],
                     [3,28,15,6,21,10],
                     [23,19,12,4,26,8],
                     [16,7,27,20,13,2],
                     [41,52,31,37,47,55],
                     [30,40,51,45,33,48],
                     [44,49,39,56,34,53],
                     [46,42,50,36,29,32]]

##0001 0010 0011 0100 0101 0110 0111 1000 1001 1010 1011 1100 1101 1110 1111 0001
def claveDes(clave):
    pc=""
    c0=""
    d0=""
    print("Clave ",clave)
    clave="0"+(clave.replace(" ",""))    
    matrizPermutada=[]
    for i in matrizPermutaciones:
        listaPermutada=[]
        for j in i:            
            listaPermutada.append(clave[j])
        matrizPermutada.append(listaPermutada)
    for i in matrizPermutada:
        cont2=1
        for j in i:
            if cont2%4==0:
                pc+=" "
                cont2=1
            pc+=j
            cont2+=1
    print("Pc-1 ",pc)
    print("\n")
    pc=pc.replace(" ","")
    return rotacion(pc[0:len(pc)//2],pc[len(pc)//2:])

def rotacion(c0,d0):
    matrizRotacionesCi=[]
    matrizRotacionesDi=[]
    for i in listaIteraciones:
        listaRotacionesCi=[]
        listaRotacionesDi=[]
        
        c0Tempo=c0[:i]
        c0Sobra=c0[i:]        
        c0Total=c0Sobra+c0Tempo
        listaRotacionesCi=[c0Total]
        c0=c0Total
        matrizRotacionesCi.append(listaRotacionesCi)
        
        d0Tempo=d0[:i]
        d0Sobra=d0[i:]
        d0Total=d0Sobra+d0Tempo
        listaRotacionesDi=[d0Total]
        d0=d0Total
        matrizRotacionesDi.append(listaRotacionesDi)
        
    print("Ci")
    contCi=0
    for i in matrizRotacionesCi:
        print("C"+str(contCi),i)
        contCi+=1
    print("\n")
    print("Di")
    contDi=0
    for i in matrizRotacionesDi:
        print("D"+str(contDi),i)
        contDi+=1
    permutaciones2(matrizRotacionesCi,matrizRotacionesDi)

def permutaciones2(matrizRotacionesCi,matrizRotacionesDi):
    matriz=[]
    for i in range(len(matrizRotacionesDi)):        
        matriz.append(str(matrizRotacionesCi[i][0])+str(matrizRotacionesDi[i][0]))
        
    matrizPermutada=[]
    for lista in matriz:
        lista="0"+str(lista)
        listaPermutada=[]
        for i in matrizPermutaciones2:
            for j in i:                
                listaPermutada.append(lista[j])
        matrizPermutada.append(listaPermutada)
    matrizK=[]   
    for i in matrizPermutada:
        var=""
        for j in i:
            var=var+j
        matrizK.append(var)
    printearK(matrizK)
   
def printearK(matriz):
    print("\n")
    print("K")
    for i in range(len(matriz)):        
        print("["+str(matriz[i])+"]")
