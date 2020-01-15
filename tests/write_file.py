import sys

with open(sys.argv[1], 'w') as file:
    for x in range(int(sys.argv[3])):
        file.write(str(sys.argv[2]))

