from enum import Enum
import numpy as np
from numpy.linalg import eig
import time
import sys

def getIndex(letter):
    if letter == 'n':
        return 1
    elif letter == 'o':
        return 2
    elif letter == 'f':
        return 3
    elif letter == 'b':
        return 4
    elif letter == 'r':
        return 5
    elif letter == 'k':
        return 6
    elif letter == 'e':
        return 7
    elif letter == 'u':
        return 8
    elif letter == 'w':
        return 9
    elif letter == '-':
        return 10
    elif letter == '\n':
        return 11

def getLetter(number):
    if number == 0:
        return 'n'
    elif number == 1:
        return 'n'
    elif number == 2:
        return 'o'
    elif number == 3:
        return 'f'
    elif number == 4:
        return 'b'
    elif number == 5:
        return 'r'
    elif number == 6:
        return 'k'
    elif number == 7:
        return 'e'
    elif number == 8:
        return 'u'
    elif number == 9:
        return 'w'
    elif number == 10:
        return '-'
    elif number == 11:
        return '\n'

def defineArray(number, array, tag):
    if(tag == 'f'):
        for x in range(0, number):
            array.append([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
    else:
        for x in range(0, number):
            array.append(0)




f = open(sys.argv[1], "r")

totalLetters = 0
array = []
marginal = []

defineArray(12, marginal, 'i')
print(marginal)
defineArray(12, array, 'f')

array = np.array(array)


while True:
    line = f.readline()

    if not line:
        break

    for x in range(0, len(line) - 1):
        array[getIndex(line[x+1])][getIndex(line[x])] += 1
        marginal[getIndex(line[x])] += 1
        if x == 0:
            array[getIndex(line[x])][0] += 1
            marginal[0] += 1


print(array)
print(marginal)

for x in range (0, 12):
    for y in range(0,12):
        if(array[y][x] == 0):
            array[y][x] = 0
            continue
        array[y][x] = round((array[y][x] / marginal[x]), 4)

print(array)
values, vectors = eig(array)
print(values)
