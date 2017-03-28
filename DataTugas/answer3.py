data1 = "DataSet.txt"

def readData(data1):
    x = []
    with open(data1) as data:
        for line in data:
            x = line.split()
    return x

x = readData(data1)
y = []
z = []
for i in x:
    if (i.isdigit() == True) :
        y.append(i)
for i in x :
    if (i.isdigit() == True) :
        z.append(y.pop())
    else : z.append(i)
k = []
i = z[0]
i = ' '.join(l[0].upper() + l[1:] for l in i.split())
k.append(i)

for count in range(1,len(z)):
    i = z[count]
    n = z[count-1]
    if (n[len(n)-1] == '.') :
        i = ' '.join(l[0].upper() + l[1:] for l in i.split())
    k.append(i)

k = ' '.join(k)
print (k)