import numpy as np
import random
#MATRIZ [5][5] CON NUMPY RELLENAS DE 0.5
print("\tMATRIZ")
print()
lista_val=[[0.5,0.5,0.5,0.5],[0.5,0.5,0.5,0.5],[0.5,0.5,0.5,0.5],[0.5,0.5,0.5,0.5]]
matriz=np.array(lista_val)
print (matriz)

#MATRIZ [5][5] CON VALORES AL AZAR
print ()
print("ALEATORIO")
fila=random.randint(1,25)
print (fila)
print()

print("MATRIZ CON VALORES AL AZAR")
print()
dim=(5,5)
matriz1=np.random.randint(1,25,dim)
print(matriz1)

#fila=np.random.randint(5, size=(5,5))
#print(fila)
