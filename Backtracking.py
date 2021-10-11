M=2 #PlataAInvertirTotal
n=3 #CantidadDeBancos
I=[0,0,0] #Cada posicion indica cuantos pesos invierto en cada banco
F=[[0,43,56,99],[0,32,79,80],[0,51,62,71]] #Interes que genera c/banco por cada peso
maximo=0
 
def Ganancia(F,n,M,I):
    global maximo
    tot=0 #Cantidad de dinero invertido hasta el momento
    suma=0
    for i in range(0,n):
        tot=tot+I[i]
 
    if tot==M:
        for i in range(0,n):
            suma= (F[i][I[i]]) + suma
            if suma>maximo:
                maximo=suma
 
    else:
        for i in range(0,n):
            nuevoI=I[:] #porCopia
            nuevoI[i]=nuevoI[i]+1
            Ganancia(F,n,M,nuevoI)
    return maximo
 
print("La ganancia maxima con ",M,"pesos será: ",Ganancia(F,n,M,I))