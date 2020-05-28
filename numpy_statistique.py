import numpy as np 

A = np.random.randint(0, 10, [2, 3])
print(A)

moyenne = A.mean()
ecart_type = A.std()
variance = A.var()
print(moyenne)
matrice_correlation = np.corrcoef(A)
print(matrice_correlation)