import math
N1 = int(input())
N2 = int(input())
list_num = []
for i in range(N1,N2+1):
    is_valid = True
    if i == 1:
        continue
    for j in range(2,int(math.sqrt(i))+1):
        if i % j == 0:
            is_valid = False
            break
    if is_valid:
        list_num.append(i)

if len(list_num) == 0:
    print(-1)
else:
    print(sum(list_num))
    print(list_num[0])