N = int(input())
list_num = input().split()
count = 0
for i in range(N):
    num = int(list_num[i])
    is_valid = True
    if(num == 1):
        continue
    for j in range(2,num):
        if num % j == 0:
            is_valid = False
            break
    if(is_valid):
        count += 1
print(f"{count}")