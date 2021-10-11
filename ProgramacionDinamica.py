def intereses(F,I,n,m):
   for i in range (0,n):
       I[i][0]=0
   for j in range (m+1):
       I[0][j]=F[0][j]
   for i in range (1,n):
       for j in range (1,m+1):
           I[i][j]=IntMax(I,F,i,j)
   return(I[n-1][m])
 
def IntMax(I,F,i,j):
   #maxim=0
   #t=0
   maxim=I[i-1][j]+F[i][0]
   for t in range(1,j+1):
       maxim=max(maxim,I[i-1][j-t]+F[i][t])
   return (maxim)
 
def crearMatriz(m,n):
   matriz = []
   for i in range(0,m):
       fila=[]
       for j in range (0,n):
           fila=fila[0:j]+[0]
       matriz=matriz[0:i]+[fila]
   return matriz
 
#MAIN
bancos = int(input("Coloque la cantidad de bancos:"))
dinero = int(input("Coloque la cantidad de dinero:"))
matF=[[0,43,56,99],[0,32,79,80],[0,51,62,71]]
matI=crearMatriz(bancos,dinero+1)
resultado=intereses(matF,matI,bancos,dinero)
print("La ganancia maxima con ",dinero,"pesos será: ",resultado)