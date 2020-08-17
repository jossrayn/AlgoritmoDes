#principal("0000 0000 0000 0000 0000 0001 0111 0101 0100 0010 0000 0100","0001 1011 0000 0010 1110 1111 1111 1100 0111 0000 0111 0010 ")#
listaConversiones=[1,10,11,100,101,110,111,1000,1001,1010,1011,1100,1101,1110,1111]

def principal(ri,ki):
    print("R",ri)
    print("K",ki)
    Xor=xor(ri,ki)
    print("Xor",agrupasicon4(Xor))
    print("Agrupasicon",agrupasicon(Xor))
    cajas=ultimoPaso(Xor)
    print("Aplicando cajas a R0",agrupasicon4(cajas))
    print("Permutacion",agrupasicon4(permutacion(cajas)))
    
def xor(ri,ki):
    ri=ri.replace(" ","")
    ki=ki.replace(" ","")
    xorResultado=""
    for i in range(len(ri)):
        if ri[i]=="0" and ki[i]=="0":
            xorResultado+="0"
        elif ri[i]=="1" and ki[i]=="1":
            xorResultado+="0"
        else:
            xorResultado+="1"
    return xorResultado

def agrupasicon4(cadena):
    agrepasionResultando=""
    for i in range(len(cadena)):
        if i%4==0:
            agrepasionResultando+=" "
            agrepasionResultando+=cadena[i]
        else:
            agrepasionResultando+=cadena[i]
    return agrepasionResultando

def agrupasicon(cadena):
    agrepasionResultando=""
    for i in range(len(cadena)):
        if i%6==0:
            agrepasionResultando+=" "
            agrepasionResultando+=cadena[i]
        else:
            agrepasionResultando+=cadena[i]
    return agrepasionResultando

def fila_columna(cadena):
    for i in range(len(listaConversiones)):
        if int(cadena)==listaConversiones[i]:
            return i+1
        elif int(cadena)==0:
            return 0

def permutacionSexteto(cadena,cajaS):
    fila = fila_columna(cadena[0]+cadena[5])
    columna = fila_columna(cadena[1:5])
    return convertir4Bits(str(listaConversiones[(cajaS[fila][columna])-1]))

def convertir4Bits(cadena):
    tamano=len(cadena)
    for i in range(4):
        if tamano==4:
            return cadena
        else:
            cadena="0"+cadena
            tamano+=1
            
def ultimoPaso(cadena):
    cadena=cadena.replace(" ","")
    s1 = [[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
        [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
        [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
        [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]]
    
    s2 = [[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
          [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
          [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
          [13,9,10,1,3,15,4,2,11,6,7,12,0,5,14,9]]

    s3 = [[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
          [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
          [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
          [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]]

    s4 = [[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
          [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
          [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
          [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]]

    s5 = [[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
          [14,11,3,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
          [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
          [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]]

    s6 = [[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
          [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
          [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
          [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]]

    s7 = [[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
          [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
          [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
          [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]]

    s8 = [[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
          [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
          [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
          [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]]

    st0 = permutacionSexteto(cadena[0:6],s1)
    st1 = permutacionSexteto(cadena[6:12],s2)
    st2 = permutacionSexteto(cadena[12:18],s3)
    st3 = permutacionSexteto(cadena[18:24],s4)
    st4 = permutacionSexteto(cadena[24:30],s5)
    st5 = permutacionSexteto(cadena[30:36],s6)
    st6 = permutacionSexteto(cadena[36:42],s7)
    st7 = permutacionSexteto(cadena[42:48],s8)

    return st0+st1+st2+st3+st4+st5+st6+st7

def permutacion(bloque):
    bloque= bloque[16-1]+bloque[7-1]+bloque[20-1]+bloque[21-1]+bloque[29-1]+bloque[12-1]+bloque[28-1]+bloque[17-1]+bloque[1-1]+bloque[15-1]+bloque[23-1]+bloque[26-1]+bloque[5-1]+bloque[18-1]+bloque[31-1]+bloque[10-1]+bloque[2-1]+bloque[8-1]+bloque[24-1]+bloque[14-1]+bloque[32-1]+bloque[27-1]+bloque[3-1]+bloque[9-1]+bloque[19-1]+bloque[13-1]+bloque[30-1]+bloque[6-1]+bloque[22-1]+bloque[11-1]+bloque[4-1]+bloque[25-1]
    return bloque
