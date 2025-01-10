x,y,w,h = map(int,input().split())
distance = [w-x, h-y, x, y]
print(min(distance))