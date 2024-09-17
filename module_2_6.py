import random
from random import randint

first = randint(3, 20)
print("первое чило ", first)
result = []
for i in range(1, first):

    for j in range(2, first):
        if j < i or j == i:
            continue
        if first % (i + j) == 0:
            result.append([i, j])

a = str(result)
print("второе число", a)
a = a.replace('[', '')
a = a.replace(']', '')
a = a.replace(',', '')
a = a.replace(' ', '')
print("второе число", a)