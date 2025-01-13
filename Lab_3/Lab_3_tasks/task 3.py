
try:
    f = open('example.txt')
    for l in f:
        if l[-1] == ('\n'):
            print(l[:-1])
        else:
            print(l)
except FileNotFoundError:
    print('File is not found')