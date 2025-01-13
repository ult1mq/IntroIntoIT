f = open('task2.txt','w')
n = int(input())
for i in range(1,n):
    for j in range(1,n):
        f.write(str(i*j) + " ")
    f.write("\n")