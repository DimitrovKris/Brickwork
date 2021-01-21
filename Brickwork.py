

n = int(input('Enter rows: '))
m = int(input('Enter columns: '))

i = int(input())
j = int(input())


layer1 = []
for i in range (0,n):
    layer1.append([])
    for i in range(0,n):
        for j in range(0,m):
            layer1[i].append(j)
            layer1[i][j]=0
    for i in range(0,n):
        for j in range (0,m):
            print(i+1, j+1)

print(layer1)

