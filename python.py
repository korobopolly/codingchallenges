# 코딩테스트 문제 LV1

# 정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.
# 제한 사항
# n은 0 이상 3000이하인 정수입니다.
# 입출력 예
# n	return
# 12	28
# 5	6
# 입출력 예 설명
# 입출력 예 #1
# 12의 약수는 1, 2, 3, 4, 6, 12입니다. 이를 모두 더하면 28입니다.
# 입출력 예 #2
# 5의 약수는 1, 5입니다. 이를 모두 더하면 6입니다.

def solution(n):
    x = 0
    for i in range(1,n+1):
        if n % i == 0:
            x += i
    answer = x
    return answer

# 자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
# 예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.
# 제한사항
# N의 범위 : 100,000,000 이하의 자연수

def solution(n):
    
    result = list(map(int, str(n)))
    answer = sum(result)

    return answer

# 정수 num이 짝수일 경우 "Even"을 반환하고 홀수인 경우 "Odd"를 반환하는 함수, solution을 완성해주세요.
# 제한 조건
# num은 int 범위의 정수입니다.
# 0은 짝수입니다.
# 입출력 예
# num	return
# 3	"Odd"
# 4	"Even"

def solution(num):
    return (lambda x: 'Odd' if x % 2 != 0 else 'Even')(num)

# 정수를 담고 있는 배열 arr의 평균값을 return하는 함수, solution을 완성해보세요.
# 제한사항
# arr은 길이 1 이상, 100 이하인 배열입니다.
# arr의 원소는 -10,000 이상 10,000 이하인 정수입니다.
# 입출력 예
# arr	return
# [1,2,3,4]	2.5
# [5,5]	5

def solution(arr):
    answer = sum(arr)/len(arr)
    return answer

# 함수 solution은 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다. 다음 제한 조건을 보고, 조건을 만족하는 함수, solution을 완성해주세요.
# 제한 조건
# x는 -10000000 이상, 10000000 이하인 정수입니다.
# n은 1000 이하인 자연수입니다.
# 입출력 예
# x	n	answer
# 2	5	[2,4,6,8,10]
# 4	3	[4,8,12]
# -4	2	[-4, -8]

def solution(x, n):
    answer = []
    inputnum = 0
    for i in range(n):
        inputnum += x
        answer.append(inputnum)
        
    return answer

# 자연수 n이 매개변수로 주어집니다. n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x를 return 하도록 solution 함수를 완성해주세요. 답이 항상 존재함은 증명될 수 있습니다.
# 제한사항
# 3 ≤ n ≤ 1,000,000
# 입출력 예
# n	result
# 10	3
# 12	11

def solution(n):
    answer = 0
    for i in range(n, 0, -1):
        if n % i == 1:
            answer = i
    
    return answer

# 문자열 s를 숫자로 변환한 결과를 반환하는 함수, solution을 완성하세요.
# 제한 조건
# s의 길이는 1 이상 5이하입니다.
# s의 맨앞에는 부호(+, -)가 올 수 있습니다.
# s는 부호와 숫자로만 이루어져있습니다.
# s는 "0"으로 시작하지 않습니다.
# 입출력 예
# 예를들어 str이 "1234"이면 1234를 반환하고, "-1234"이면 -1234를 반환하면 됩니다.
# str은 부호(+,-)와 숫자로만 구성되어 있고, 잘못된 값이 입력되는 경우는 없습니다.

def solution(s):
    answer = int(s)
    return answer

# 두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
# 예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.
# 제한 조건
# a와 b가 같은 경우는 둘 중 아무 수나 리턴하세요.
# a와 b는 -10,000,000 이상 10,000,000 이하인 정수입니다.
# a와 b의 대소관계는 정해져있지 않습니다.
# 입출력 예
# a	b	return
# 3	5	12
# 3	3	3
# 5	3	12

def solution(a, b):
    if a > b:
        a, b = b, a
    
    return sum(range(a, b+1))

# 대문자와 소문자가 섞여있는 문자열 s가 주어집니다. s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요. 'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.
# 예를 들어 s가 "pPoooyY"면 true를 return하고 "Pyy"라면 false를 return합니다.
# 제한사항
# 문자열 s의 길이 : 50 이하의 자연수
# 문자열 s는 알파벳으로만 이루어져 있습니다.
# 입출력 예
# s	answer
# "pPoooyY"	true
# "Pyy"	false

def solution(s):
    s1 = s.lower()
    counted = {}

    for i in s1:
        if i in counted:
            counted[i] += 1
        else:
            counted[i] = 1

    return counted.get('p',0) == counted.get('y',0) 

# 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.
# 제한 조건
# n은 10,000,000,000이하인 자연수입니다.
# 입출력 예
# n	return
# 12345	[5,4,3,2,1]

def solution(n):
    reversed_list = reversed(list(str(n)))
    answer = list(map(int, reversed_list))
    return answer

# 함수 solution은 정수 n을 매개변수로 입력받습니다. n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 예를들어 n이 118372면 873211을 리턴하면 됩니다.
# 제한 조건
# n은 1이상 8000000000 이하인 자연수입니다.
# 입출력 예
# n	return
# 118372	873211

def solution(n):
    return int(''.join(sorted(str(n), reverse=True)))

# 임의의 양의 정수 n에 대해, n이 어떤 양의 정수 x의 제곱인지 아닌지 판단하려 합니다.
# n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.
# 제한 사항
# n은 1이상, 50000000000000 이하인 양의 정수입니다.
# 입출력 예
# n	return
# 121	144
# 3	-1
# 입출력 예 설명
# 입출력 예#1
# 121은 양의 정수 11의 제곱이므로, (11+1)를 제곱한 144를 리턴합니다.
# 입출력 예#2
# 3은 양의 정수의 제곱이 아니므로, -1을 리턴합니다.

def solution(n):
    return (lambda x:int(((x)**(1/2)+1)**2) if x**(1/2) == int(x**(1/2)) else -1)(n)
print(solution(121))
