matriz_ip=[[58,50,42,34,26,18,10,2],
           [60,52,44,36,28,20,12,4],
           [62,54,46,38,30,22,14,6],
           [64,56,48,40,32,24,16,8],
           [57,49,41,33,25,17,9,1],
           [59,51,43,35,27,19,11,3],
           [61,53,45,37,29,21,13,5],
           [63,55,47,39,31,23,15,7]]

matriz_Permutacion=[[32,1,2,3,4,5],
                    [4,5,6,7,8,9],
                    [8,9,10,11,12,13],
                    [12,13,14,15,16,17],
                    [16,17,18,19,20,21],
                    [20,21,22,23,24,25],
                    [24,25,26,27,28,29],
                    [28,29,30,31,32,1]]
#funcionIP("0100 0101 0100 1010 0100 0101 0100 1101 0101 0000 0100 1100 0100 1111 0100 1101")

def funcionIP(cadena):
    cadena="0"+cadena.replace(" ","")
    matrizPermutada=[]
    for i in matriz_ip:
        lista=[]
        for j in i:
            lista.append(cadena[j])
        matrizPermutada.append(lista)
    cadenaPermutada=""
    for i in matrizPermutada:
        for j in i:
            cadenaPermutada+=j
    print("IP(M)=",cadenaPermutada)
    print("R(0) =",cadenaPermutada[len(cadenaPermutada)//2:])
    print("L(0) =",cadenaPermutada[0:len(cadenaPermutada)//2])
    print("Aplicacion de E")
    print("R(0) =",agrupasicon(expansionE(cadenaPermutada[len(cadenaPermutada)//2:])))
    print("L(0) =",agrupasicon(expansionE(cadenaPermutada[0:len(cadenaPermutada)//2])))

def agrupasicon(cadena):
    agrepasionResultando=""
    for i in range(len(cadena)):
        if i%4==0:
            agrepasionResultando+=" "
            agrepasionResultando+=cadena[i]
        else:
            agrepasionResultando+=cadena[i]
    return agrepasionResultando

def expansionE(cadena):
    matrizPermutada=[]
    for i in matriz_Permutacion:
        lista=[]
        for j in i:
            lista.append(cadena[j-1])
        matrizPermutada.append(lista)
    cadenaPermutada=""
    for i in matrizPermutada:
        for j in i:
            cadenaPermutada+=j
    return(cadenaPermutada)
