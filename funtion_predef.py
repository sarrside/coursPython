x = -2
y=10
liste = [i**2 for i in range(10)]
print(abs(x))
tuple_1 = (1,2,3,4,5,6,7)
print(min(tuple_1), max(tuple_1))
str(y)
print(bin(15))
print(hex(11))
print(oct(4))
x = input('Donner votre age')
print('Votre age est ',x)

print("X vaut {} et y vaut {} ".format(x, y))

f = open('fichier.txt', 'w')
f.write('Bonjour')
f.close()
with open('fichier.txt', 'r') as f:
    print(f.read())

with open('fichier.txt', 'w') as f:
    for i in range(20):
        f.write("{}^2 = {} \n".format(i, i**2))