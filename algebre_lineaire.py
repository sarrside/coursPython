import numpy as np 
np.random.seed(0)
A = np.ones((3, 2))
B = np.ones((2, 3))

print("Transposée matrice ")
print(A.T)
print(A)
print(B)
#Produit matricielle de A et B
print(A.dot(B))

#Standariser une matrice A : (A-mean(A))/std(A) avec std =  ecart-type
A = np.random.randint(0, 20, [6,5])
C = (A - A.mean(axis=0))/A.std(axis=0)

print(C)