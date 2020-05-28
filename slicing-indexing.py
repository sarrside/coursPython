import numpy as np 
from scipy import misc
import matplotlib.pyplot as plt 

tab = np.zeros((4, 4))
tab_ = np.array([[1,2,3,], [4,5,6], [7,8,9]])
print(tab_)

#Extraire toute la premiere colonne
print(tab_[:, 0])

#Extraire toute la premiere ligne
print(tab_[0, :])

#Deux premiers lignes 3 premiers colonnes
print(tab_[0:2, 0:3])

#Mettre les elements du milieu à 2
tab[1:3, 1:3] = 2
print(tab)

print("Ligne 1 ")

face = misc.face(gray=True)
plt.imshow(face, cmap = plt.cm.gray )
plt.show()
#print(face.shape)

h = face.shape[0]
w = face.shape[1]
zoom_face = face[h//4:-h//4, w//4:-w//4]
print(zoom_face)