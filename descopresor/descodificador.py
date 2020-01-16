import sys
import struct

maximum_table_size = 4096
data = sys.stdin.buffer.read()
next_code = 256
decompressed_data = ""
string = ""

compressed_data = data

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

next_code = len(dictionary)

for code in compressed_data:
    print(code)
    if not (code in dictionary):
        dictionary[code] = string + (string[0])
    decompressed_data += dictionary[code]
    if not (len(string) == 0):
        dictionary[next_code] = string + (dictionary[code][0])
        next_code += 1
    string = dictionary[code]

for data in decompressed_data:
    print(data)
