xlist = []
ylist = []
for _ in range(3):
    X,Y = input().split()
    xlist.append(X)
    ylist.append(Y)

minx = []
miny = []
for x,y in zip(xlist,ylist):
    if x in minx:
        minx.remove(x)
    else:
        minx.append(x)
    if y in miny:
        miny.remove(y)
    else:
        miny.append(y)

print(minx[0],miny[0])