import sys
from struct import *

input_file = sys.argv[1]

# mudar para ser por stdin no futuro :D
file = open(input_file, 'rb')

dictionary = {
    0: 'broken-\n',
    1: 'on-----\n',
    2: 'off----\n',
    3: 'unknown\n',
}
compressed_data = []

while True:
    rec = file.read(2)
    if len(rec) != 2:
        break
    (data,) = unpack('>H', rec)
    compressed_data.append(data)

decompressed_data = ""
string = ""
next_code = len(dictionary)

for current_code in compressed_data:

    if not (current_code in dictionary):
        dictionary[current_code] = string + (string[:8])
    decompressed_data += dictionary[current_code]

    if not (len(string) == 0):
        dictionary[next_code] = string + (dictionary[current_code][:8])
        next_code += 1
    string = dictionary[current_code]

print(decompressed_data, end='')
file.close()
