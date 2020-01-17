import sys
from struct import *

input_file = sys.argv[1]

# mudar para ser por stdin no futuro :D
file = open(input_file)
data = file.read()
file.close()

dictionary = {
    'broken-\n': 0,
    'on-----\n': 1,
    'off----\n': 2,
    'unknown\n': 3,
}

string = ""
compressed_data = []

word = data[:8]  # le a primeora palavra ex 'unknown\n'
data = data[8:]  # retira oque leu do input

while word:
    string_plus_symbol = string + word

    if string_plus_symbol in dictionary:
        string = string_plus_symbol

    else:
        compressed_data.append(dictionary[string])

        dictionary[string_plus_symbol] = len(dictionary)
        string = word

    word = data[:8]
    data = data[8:]

if string in dictionary:
    compressed_data.append(dictionary[string])

with open('teste.b', 'wb') as file:
    for data in compressed_data:
        file.write(pack('>H', int(data)))
