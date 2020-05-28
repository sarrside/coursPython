import numpy as np 
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from mpl_toolkits.mplot3d import Axes3D
from scipy import misc

iris = load_iris()
x = iris.data
y = iris.target
names = list(iris.target_names)
print(f'x contient {x.shape[0]} exemples et {x.shape[1]} variables ')
print(f'Il y\'a {np.unique(y).size} classes')

#Graphique 3D nuages de point
ax = plt.axes(projection="3d")
ax.scatter(x[:,0], x[:,1], x[:,2], c=y)
plt.show()

#Graphique 3D en mode surface
f= lambda x,y: np.sin(x) + np.cos(x+y)
X = np.linspace(0, 5, 100)
Y = np.linspace(0, 5, 100)
X, Y = np.meshgrid(X, Y)
Z = f(X, Y)
print(Z.shape)
ax = plt.axes(projection="3d")
ax.plot_surface(X, Y, Z, cmap='plasma')
plt.show()

#Tracer un histogramme pour la première variable avec bins param qui signifie le nombre de section de l'histogramme
plt.hist(x[:,0], bins=30)
plt.show()
#Tracer un histogramme pour les deux première variables
plt.hist(x[:,0], bins=30)
plt.hist(x[:,1], bins=30)
plt.show()

#Histogramme en deux D
plt.hist2d(x[:,0], x[:, 1], cmap="Blues")
plt.colorbar()
plt.show()

#Analyse d'une image bins sera égale 255
face = misc.face(gray=True)
plt.imshow(face, cmap="gray")
plt.hist(face, bins=255)
plt.show()