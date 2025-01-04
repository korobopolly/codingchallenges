import math
while (1):
    N = int(input())
    if N == -1:
        break
    divisors = []
    for i in range(1,int(math.sqrt(N))+1):
        if N % i == 0:
            divisors.append(i)
            if i != N//i:
                divisors.append(N // i)
    divisors.sort()
    if (divisors[-1] == sum(divisors) - divisors[-1]):
        print(f"{divisors[-1]} = {divisors[0]} ",end="")
        for i in range(len(divisors)-2):
            print(f"+ {divisors[i+1]} ",end="")
        print()
    else:
        print(f"{N} is NOT perfect.")