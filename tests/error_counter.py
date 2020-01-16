import sys

with open(sys.argv[1], 'r') as file:
    info = file.read()
    error_counter = 0
    for x in info:
        if x == 'A':
            error_counter += 1

    print("File:", sys.argv[1], "\nErrors:", error_counter, "\nP(error):", error_counter / int(sys.argv[2]))
