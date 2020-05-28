import numpy as np 

tab = np.array([1,2,3])
#Dimension
print(tab.ndim)
#taille de la dimension
print(tab.shape)
#Creation de array avec 3 lignes et deux colonne remplis de zero
B = np.zeros((3,2))
print(B)
#Creation de array avec 3 lignes et deux colonne remplis de un
A = np.ones((3,2))
print(A)

#Creation de array avec 3 lignes et deux colonne remplis de ce que nous desirons exemple 
D = np.full((3,2),10)
print(D)

#Creation de array avec 3 lignes et deux colonne remplis de nombre aleatoire
#np.seed(0) permet de fixer les valeurs si on change le 0 les valeurs vont varier 
np.random.seed(0)
E = np.random.randn(3,2)
print(E)

#Creation de matrice d'identité le parametre est le nombre d'élément sur la diagonale 
F = np.eye(4)
print(F)

#Creation de array  a une dimension avec debut, fin et quantité comme parametre  
G = np.linspace(0,9, 20)
print(G)

#Creation de array  a une dimension avec element rempli par pas
H = np.arange(0, 50, 1.5)
print(H)


#On peut ajouter dans tous ces constructeurs le paramètre dtype pour spécifier le type des données
H = np.arange(0, 31, 3, dtype=float)
print(H)

def initialisation(m, n):
    matrice = np.random.randn(m, n)
    matrice = np.concatenate((matrice, np.ones((matrice.shape[0], 1))), axis= 1)
    return matrice

m = initialisation(4, 3)
print(m)