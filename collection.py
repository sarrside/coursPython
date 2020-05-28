#List modifiable  indexé
liste = [i**2 for i in range(10)]
print(liste)
dictio_1 = {k:v for k, v in enumerate([i**2 for i in range(10)]) }
dictio_2 = {
    str(k): k**2 for k in range(20)
}
print(dictio_2)
#Tuple non modifiable
tuple_1 = (1,2,3,4,5,6,7)
print(tuple_1[1])
#Dictionnaire modifiable non indexé concept de clé valeur
dictionnaire = {
    "Sénégal": "Dakar",
    "Mauritanie" : "Nouatchot",
    "France": "Paris",
}
