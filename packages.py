import project_1 as p1
from project_1 import fibonacci
import math
import statistics
import os
import random
import glob


fibo = fibonacci(20)
print(fibo)
#MATH MODULE
print(math.pi)
print(math.cos(2*math.pi))

liste = [i**2 for i in range(10)]

#STATISTIC MODULE
print(statistics.mean(liste))
print(statistics.variance(liste))

#RANDOM MODULE
print(random.seed(0))

print(random.random())

random.shuffle(fibo)
print(fibo)

#OS MODULE
print(os.getcwd)

liste_1 = [line.strip() for line in open('fichier.txt', 'r')]
print(liste_1)