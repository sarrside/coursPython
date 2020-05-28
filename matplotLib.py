import matplotlib.pyplot as plt
import numpy as np 

x = np.linspace(0, 2, 10)
y = x**2
print(x)
#Tracer une courbe
plt.plot(x, y, c="red", lw=6)
plt.show()
#Tracer le nuage de point params : c= couleur, lw= line width ou epaisseur
plt.scatter(x, y, c="yellow")
plt.show()

#Plus normal avec matplotlib il faut créer une figure avant de commencer

plt.figure()
plt.plot(x, y, label="quadratique")
#Ajouter une autre courbe
plt.plot(x, x**3, label="Cubique")
#Ajouter un titre
plt.title("Figure 1")
#Ajouter les labels abcissi et coordonnée
plt.xlabel("axe X")
plt.ylabel("axe Y")
#Ajouter une legende
plt.legend() 
plt.show()

#Enregistrer la figure
plt.savefig("result.png")
#On utilise subplot() pour avoir plusieurs figures avec comme parametre nombre de ligne, nombre de colonnes, et le numero de figure que l'on veut mettre en oeuvre
plt.figure()
plt.subplot(2,1, 1)
plt.plot(x, y)
plt.subplot(2, 1, 2)
plt.plot(x, x**3)
plt.show()

#Exercice à faire
dataset = {f"experience{i}": np.random.randn(100) for i in range(4)}
print(dataset)

#Fonction pour afficher plusieur figure d'une dictionnaire
def graphique(dataset):
    plt.figure(figsize=(12, 8))
    for k, i in zip(dataset.keys(), range(1, len(dataset) + 1)):
        plt.subplot(len(dataset), 1, i)
        plt.plot(dataset[k])
    plt.show()    

graphique(dataset)