import numpy as np 
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris


iris = load_iris()
x = iris.data
y = iris.target
names = list(iris.target_names)
print(f'x contient {x.shape[0]} exemples et {x.shape[1]} variables ')
print(f'Il y\'a {np.unique(y).size} classes')

#Classification avec alpha transparence
plt.scatter(x[:,0], x[:,1], c=y, alpha=0.5) 
plt.xlabel('Longueur sepale')
plt.ylabel('Largeur sepale')
plt.show()

