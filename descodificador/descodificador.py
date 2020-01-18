import sys

input_file = sys.argv[1]

file = open(input_file, 'rb')

'''
Cada palavra gerada pela fonte é tratada como simbolo
indivisicel, i.e. um átomo.
'''
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

    p1 = rec[0]
    p2 = rec[1]

    #a p1 é feito um shift right de 1 bit (bit de redundancia adicionado pelo codificador).
    #são "adicionados" 8 bits a p1. É feito o or com p2.
    p1 = p1 >> 1
    short = (p1 << 8) ^ p2
    to_unpack = short >> 1

    compressed_data.append(to_unpack)

decompressed_data = ""
string = ""
next_code = len(dictionary)

'''
Implementação do algoritmo LZW baseado nos slides.
'''
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
