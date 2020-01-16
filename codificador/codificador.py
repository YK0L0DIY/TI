import sys
from struct import *

input_file = sys.argv[1]
maximum_table_size = 4096

file = open(input_file)
data = file.read()
file.close()

dictionary = {
    'b': 0,
    'e': 1,
    'f': 2,
    'k': 3,
    'n': 4,
    'o': 5,
    'r': 6,
    'u': 7,
    'w': 8,
    '-': 9,
    '\n': 10,
}

string = ""
compressed_data = []

for symbol in data:
    string_plus_symbol = string + symbol
    if string_plus_symbol in dictionary:
        string = string_plus_symbol

    else:
        compressed_data.append(dictionary[string])

        if len(dictionary) <= maximum_table_size:
            dictionary[string_plus_symbol] = len(dictionary)
        string = symbol

if string in dictionary:
    compressed_data.append(dictionary[string])

for data in compressed_data:
    print(pack('>H', int(data)), end='')
    #print(bin(data), end='')
