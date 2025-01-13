f = open('example.txt','r')
for l in f:
    if l[-1] == ('\n'):
        print(l[:-1])
    else:
        print(l)