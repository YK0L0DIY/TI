import sys
from struct import *

data = sys.stdin.readlines()

'''
Cada palavra gerada pela fonte é tratada como simbolo
indivisivel, i.e. um átomo.
'''
dictionary = {
    'broken-\n': 0,
    'on-----\n': 1,
    'off----\n': 2,
    'unknown\n': 3,
}

string = ""
compressed_data = []

for word in data:
    string_plus_word = string + word

    if string_plus_word in dictionary:
        string = string_plus_word

    else:
        compressed_data.append(dictionary[string])

        dictionary[string_plus_word] = len(dictionary)
        string = word

if string in dictionary:
    compressed_data.append(dictionary[string])

with open('../descodificador/codificado.bin', 'wb') as file:
    for data in compressed_data:

        #short = p1p2
        short = pack('>H', int(data) << 1)
        p1 = short[0]
        p2 = short[1]

        #p2 ja tem redundancia no ultimo bit. (adicionada na operacao pack << 1)
        #p1 nao tem, "adicionar" o bit de redundancia e fazer or com p2.
        p1 = p1 << 1
        to_write = (p1 << 8) ^ p2
        file.write(pack('>H', int(to_write)))
