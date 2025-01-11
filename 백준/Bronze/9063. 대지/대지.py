N = int(input())
xlist = []
ylist = []
for _ in range(N):
    X,Y = map(int,input().split())
    xlist.append(X)
    ylist.append(Y)
if N == 1:
    print(0)
else:
    max_x = max(xlist)
    min_x = min(xlist)
    max_y = max(ylist)
    min_y = min(ylist)
    print((max_x - min_x) * (max_y - min_y))