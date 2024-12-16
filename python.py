# 코딩테스트 문제 LV1 ~ LV3

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

# 양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다. 예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다. 자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, solution을 완성해주세요.
# 제한 조건
# x는 1 이상, 10000 이하인 정수입니다.
# 입출력 예
# x	return
# 10	true
# 12	true
# 11	false
# 13	false
# 입출력 예 설명
# 입출력 예 #1
# 10의 모든 자릿수의 합은 1입니다. 10은 1로 나누어 떨어지므로 10은 하샤드 수입니다.

# 입출력 예 #2
# 12의 모든 자릿수의 합은 3입니다. 12는 3으로 나누어 떨어지므로 12는 하샤드 수입니다.

# 입출력 예 #3
# 11의 모든 자릿수의 합은 2입니다. 11은 2로 나누어 떨어지지 않으므로 11는 하샤드 수가 아닙니다.

# 입출력 예 #4
# 13의 모든 자릿수의 합은 4입니다. 13은 4로 나누어 떨어지지 않으므로 13은 하샤드 수가 아닙니다.

def solution(x):
    answer = map(int, str(x))
    return x % sum(answer) == 0

# array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.
# divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.
# 제한사항
# arr은 자연수를 담은 배열입니다.
# 정수 i, j에 대해 i ≠ j 이면 arr[i] ≠ arr[j] 입니다.
# divisor는 자연수입니다.
# array는 길이 1 이상인 배열입니다.
# 입출력 예
# arr	divisor	return
# [5, 9, 7, 10]	5	[5, 10]
# [2, 36, 1, 3]	1	[1, 2, 3, 36]
# [3,2,6]	10	[-1]
# 입출력 예 설명
# 입출력 예#1
# arr의 원소 중 5로 나누어 떨어지는 원소는 5와 10입니다. 따라서 [5, 10]을 리턴합니다.
# 입출력 예#2
# arr의 모든 원소는 1으로 나누어 떨어집니다. 원소를 오름차순으로 정렬해 [1, 2, 3, 36]을 리턴합니다.
# 입출력 예#3
# 3, 2, 6은 10으로 나누어 떨어지지 않습니다. 나누어 떨어지는 원소가 없으므로 [-1]을 리턴합니다.

def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0 :
            answer.append(i)
    
    if(len(answer) == 0):
        answer.append(-1)
    return sorted(answer)

# String형 배열 seoul의 element중 "Kim"의 위치 x를 찾아, "김서방은 x에 있다"는 String을 반환하는 함수, solution을 완성하세요. seoul에 "Kim"은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.
# 제한 사항
# seoul은 길이 1 이상, 1000 이하인 배열입니다.
# seoul의 원소는 길이 1 이상, 20 이하인 문자열입니다.
# "Kim"은 반드시 seoul 안에 포함되어 있습니다.
# 입출력 예
# seoul	return
# ["Jane", "Kim"]	"김서방은 1에 있다"

def solution(seoul):
    i = seoul.index("Kim")
    return f"김서방은 {i}에 있다"

# 1937년 Collatz란 사람에 의해 제기된 이 추측은, 주어진 수가 1이 될 때까지 다음 작업을 반복하면, 모든 수를 1로 만들 수 있다는 추측입니다. 작업은 다음과 같습니다.
# 1-1. 입력된 수가 짝수라면 2로 나눕니다. 
# 1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다. 
# 2. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복합니다. 
# 예를 들어, 주어진 수가 6이라면 6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1 이 되어 총 8번 만에 1이 됩니다. 위 작업을 몇 번이나 반복해야 하는지 반환하는 함수, solution을 완성해 주세요. 단, 주어진 수가 1인 경우에는 0을, 작업을 500번 반복할 때까지 1이 되지 않는다면 –1을 반환해 주세요.
# 제한 사항
# 입력된 수, num은 1 이상 8,000,000 미만인 정수입니다.
# 입출력 예
# n	result
# 6	8
# 16	4
# 626331	-1
# 입출력 예 설명
# 입출력 예 #1
# 문제의 설명과 같습니다.
# 입출력 예 #2
# 16 → 8 → 4 → 2 → 1 이 되어 총 4번 만에 1이 됩니다.
# 입출력 예 #3
# 626331은 500번을 시도해도 1이 되지 못하므로 -1을 리턴해야 합니다.

def solution(num):
    for i in range (500):
        if num == 1:
            return i
        num = num / 2 if num % 2 == 0 else num * 3 + 1
    return -1

# 어떤 정수들이 있습니다. 이 정수들의 절댓값을 차례대로 담은 정수 배열 absolutes와 이 정수들의 부호를 차례대로 담은 불리언 배열 signs가 매개변수로 주어집니다. 실제 정수들의 합을 구하여 return 하도록 solution 함수를 완성해주세요.
# 제한사항
# absolutes의 길이는 1 이상 1,000 이하입니다.
# absolutes의 모든 수는 각각 1 이상 1,000 이하입니다.
# signs의 길이는 absolutes의 길이와 같습니다.
# signs[i] 가 참이면 absolutes[i] 의 실제 정수가 양수임을, 그렇지 않으면 음수임을 의미합니다.
# 입출력 예
# absolutes	signs	result
# [4,7,12]	[true,false,true]	9
# [1,2,3]	[false,false,true]	0
# 입출력 예 설명
# 입출력 예 #1
# signs가 [true,false,true] 이므로, 실제 수들의 값은 각각 4, -7, 12입니다.
# 따라서 세 수의 합인 9를 return 해야 합니다.
# 입출력 예 #2
# signs가 [false,false,true] 이므로, 실제 수들의 값은 각각 -1, -2, 3입니다.
# 따라서 세 수의 합인 0을 return 해야 합니다.

def solution(absolutes, signs):
    real_list = []
    for i in range(len(absolutes)):
        if signs[i]:
            real_list.append(absolutes[i])
        else:
            real_list.append(-absolutes[i])
    return sum(real_list)

# 0부터 9까지의 숫자 중 일부가 들어있는 정수 배열 numbers가 매개변수로 주어집니다. numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 return 하도록 solution 함수를 완성해주세요.
# 제한사항
# 1 ≤ numbers의 길이 ≤ 9
# 0 ≤ numbers의 모든 원소 ≤ 9
# numbers의 모든 원소는 서로 다릅니다.
# 입출력 예
# numbers	result
# [1,2,3,4,6,7,8,0]	14
# [5,8,4,0,6,7,9]	6

def solution(numbers):
    output = [1,2,3,4,5,6,7,8,9,0]
    for i in range(len(numbers)):
        if numbers[i] in output:
            del output[output.index(numbers[i])]

    if len(output) == 0:
        return 0
    answer = sum(output)
    return answer

# 정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수, solution을 완성해주세요. 단, 리턴하려는 배열이 빈 배열인 경우엔 배열에 -1을 채워 리턴하세요. 예를들어 arr이 [4,3,2,1]인 경우는 [4,3,2]를 리턴 하고, [10]면 [-1]을 리턴 합니다.
# 제한 조건
# arr은 길이 1 이상인 배열입니다.
# 인덱스 i, j에 대해 i ≠ j이면 arr[i] ≠ arr[j] 입니다.
# 입출력 예
# arr	return
# [4,3,2,1]	[4,3,2]
# [10]	[-1]

def solution(arr):
    min_arr = min(arr)
    answer = [x for x in arr if x != min_arr]
    return answer if answer else [-1]

# 프로그래머스 모바일은 개인정보 보호를 위해 고지서를 보낼 때 고객들의 전화번호의 일부를 가립니다.
# 전화번호가 문자열 phone_number로 주어졌을 때, 전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 *으로 가린 문자열을 리턴하는 함수, solution을 완성해주세요.
# 제한 조건
# phone_number는 길이 4 이상, 20이하인 문자열입니다.
# 입출력 예
# phone_number	return
# "01033334444"	"*******4444"
# "027778888"	"*****8888"

def solution(phone_number):
    phone_number_list = list(phone_number)
    for i in range(len(phone_number_list)-4):
        phone_number_list[i] = "*"
    return "".join(phone_number_list)

# 문자열 s에는 공백으로 구분된 숫자들이 저장되어 있습니다. str에 나타나는 숫자 중 최소값과 최대값을 찾아 이를 "(최소값) (최대값)"형태의 문자열을 반환하는 함수, solution을 완성하세요.
# 예를들어 s가 "1 2 3 4"라면 "1 4"를 리턴하고, "-1 -2 -3 -4"라면 "-4 -1"을 리턴하면 됩니다.
# 제한 조건
# s에는 둘 이상의 정수가 공백으로 구분되어 있습니다.
# 입출력 예
# s	return
# "1 2 3 4"	"1 4"
# "-1 -2 -3 -4"	"-4 -1"
# "-1 -1"	"-1 -1"

def solution(s):
    s_list = s.split()
    s_list = list(map(int,s_list))
    print(s_list)
    print(min(s_list))
    print(max(s_list))
    answer = min(s_list), max(s_list)
    return " ".join(list(map(str,answer)))

# 길이가 같은 배열 A, B 두개가 있습니다. 각 배열은 자연수로 이루어져 있습니다.
# 배열 A, B에서 각각 한 개의 숫자를 뽑아 두 수를 곱합니다. 이러한 과정을 배열의 길이만큼 반복하며, 두 수를 곱한 값을 누적하여 더합니다. 이때 최종적으로 누적된 값이 최소가 되도록 만드는 것이 목표입니다. (단, 각 배열에서 k번째 숫자를 뽑았다면 다음에 k번째 숫자는 다시 뽑을 수 없습니다.)
# 예를 들어 A = [1, 4, 2] , B = [5, 4, 4] 라면
# A에서 첫번째 숫자인 1, B에서 첫번째 숫자인 5를 뽑아 곱하여 더합니다. (누적된 값 : 0 + 5(1x5) = 5)
# A에서 두번째 숫자인 4, B에서 세번째 숫자인 4를 뽑아 곱하여 더합니다. (누적된 값 : 5 + 16(4x4) = 21)
# A에서 세번째 숫자인 2, B에서 두번째 숫자인 4를 뽑아 곱하여 더합니다. (누적된 값 : 21 + 8(2x4) = 29)
# 즉, 이 경우가 최소가 되므로 29를 return 합니다.
# 배열 A, B가 주어질 때 최종적으로 누적된 최솟값을 return 하는 solution 함수를 완성해 주세요.
# 제한사항
# 배열 A, B의 크기 : 1,000 이하의 자연수
# 배열 A, B의 원소의 크기 : 1,000 이하의 자연수
# 입출력 예
# A	B	answer
# [1, 4, 2]	[5, 4, 4]	29
# [1,2]	[3,4]	10
# 입출력 예 설명
# 입출력 예 #1
# 문제의 예시와 같습니다.
# 입출력 예 #2
# A에서 첫번째 숫자인 1, B에서 두번째 숫자인 4를 뽑아 곱하여 더합니다. (누적된 값 : 4) 다음, A에서 두번째 숫자인 2, B에서 첫번째 숫자인 3을 뽑아 곱하여 더합니다. (누적된 값 : 4 + 6 = 10)
# 이 경우가 최소이므로 10을 return 합니다.

def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    return sum(a*b for a,b in zip(A,B))

# 괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다. 예를 들어
# "()()" 또는 "(())()" 는 올바른 괄호입니다.
# ")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.
# '(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고, 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.
# 제한사항
# 문자열 s의 길이 : 100,000 이하의 자연수
# 문자열 s는 '(' 또는 ')' 로만 이루어져 있습니다.
# 입출력 예
# s	answer
# "()()"	true
# "(())()"	true
# ")()("	false
# "(()("	false
# 입출력 예 설명
# 입출력 예 #1,2,3,4
# 문제의 예시와 같습니다.

def solution(s):
    stack = []
    for char in s:
        if char == "(":
            stack.append("(")
        elif stack:
            stack.pop()
        else:
            return False
    return not stack

# JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다. 단, 첫 문자가 알파벳이 아닐 때에는 이어지는 알파벳은 소문자로 쓰면 됩니다. (첫 번째 입출력 예 참고)
# 문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.
# 제한 조건
# s는 길이 1 이상 200 이하인 문자열입니다.
# s는 알파벳과 숫자, 공백문자(" ")로 이루어져 있습니다.
# 숫자는 단어의 첫 문자로만 나옵니다.
# 숫자로만 이루어진 단어는 없습니다.
# 공백문자가 연속해서 나올 수 있습니다.
# 입출력 예
# s	return
# "3people unFollowed me"	"3people Unfollowed Me"
# "for the last week"	"For The Last Week"

def solution(s):
    answer = []
    UPPERCASE = True
    for i in s:
        if i== " ":
            answer.append(" ")
            UPPERCASE = True
        else:
            if UPPERCASE == True:
                answer.append(i.upper())
                UPPERCASE = False
            else:
                answer.append(i.lower())
            
    return "".join(answer)

# 0과 1로 이루어진 어떤 문자열 x에 대한 이진 변환을 다음과 같이 정의합니다.
# x의 모든 0을 제거합니다.
# x의 길이를 c라고 하면, x를 "c를 2진법으로 표현한 문자열"로 바꿉니다.
# 예를 들어, x = "0111010"이라면, x에 이진 변환을 가하면 x = "0111010" -> "1111" -> "100" 이 됩니다.
# 0과 1로 이루어진 문자열 s가 매개변수로 주어집니다. s가 "1"이 될 때까지 계속해서 s에 이진 변환을 가했을 때, 이진 변환의 횟수와 변환 과정에서 제거된 모든 0의 개수를 각각 배열에 담아 return 하도록 solution 함수를 완성해주세요.
# 제한사항
# s의 길이는 1 이상 150,000 이하입니다.
# s에는 '1'이 최소 하나 이상 포함되어 있습니다.

def solution(s):
    count_zero = 0
    num = 0
    while (len(s) > 1):
        count_zero += s.count('0')
        num += 1
        s = bin(s.count('1'))[2:]

    return [num, count_zero]

# Finn은 요즘 수학공부에 빠져 있습니다. 수학 공부를 하던 Finn은 자연수 n을 연속한 자연수들로 표현 하는 방법이 여러개라는 사실을 알게 되었습니다. 예를들어 15는 다음과 같이 4가지로 표현 할 수 있습니다.
# 1 + 2 + 3 + 4 + 5 = 15
# 4 + 5 + 6 = 15
# 7 + 8 = 15
# 15 = 15
# 자연수 n이 매개변수로 주어질 때, 연속된 자연수들로 n을 표현하는 방법의 수를 return하는 solution를 완성해주세요.
# 제한사항
# n은 10,000 이하의 자연수 입니다.

def solution(n):
    n = int(n)
    count = 0
    k = 1
    
    while k * (k - 1) // 2 < n:
        if (n - k * (k - 1) // 2) % k == 0:
            count += 1
        k += 1
    
    return count

# 자연수 n이 주어졌을 때, n의 다음 큰 숫자는 다음과 같이 정의 합니다.
# 조건 1. n의 다음 큰 숫자는 n보다 큰 자연수 입니다.
# 조건 2. n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같습니다.
# 조건 3. n의 다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 수 입니다.
# 예를 들어서 78(1001110)의 다음 큰 숫자는 83(1010011)입니다.
# 자연수 n이 매개변수로 주어질 때, n의 다음 큰 숫자를 return 하는 solution 함수를 완성해주세요.
# 제한 사항
# n은 1,000,000 이하의 자연수 입니다.

def solution(n):
    answer = n + 1
    n = bin(n).count("1")
    while (n != bin(answer).count("1")):
        answer += 1
    return answer

# 피보나치 수는 F(0) = 0, F(1) = 1일 때, 1 이상의 n에 대하여 F(n) = F(n-1) + F(n-2) 가 적용되는 수 입니다.
# 예를들어
# F(2) = F(0) + F(1) = 0 + 1 = 1
# F(3) = F(1) + F(2) = 1 + 1 = 2
# F(4) = F(2) + F(3) = 1 + 2 = 3
# F(5) = F(3) + F(4) = 2 + 3 = 5
# 와 같이 이어집니다.
# 2 이상의 n이 입력되었을 때, n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는 함수, solution을 완성해 주세요.
# 제한 사항
# n은 2 이상 100,000 이하인 자연수입니다.
# 입출력 예
# n	return
# 3	2
# 5	5
# 입출력 예 설명
# 피보나치수는 0번째부터 0, 1, 1, 2, 3, 5, ... 와 같이 이어집니다.

def solution(n):
    # 피보나치 수를 저장할 리스트 초기화
    fib = [0, 1]  # F0과 F1 초기값
    for i in range(2, n + 1):  # 2부터 n까지 계산
        fib.append(fib[i - 2] + fib[i - 1])
    return fib[n] % 1234567  # n번째 피보나치 수 % 1234567 반환

# 짝지어 제거하기는, 알파벳 소문자로 이루어진 문자열을 가지고 시작합니다. 먼저 문자열에서 같은 알파벳이 2개 붙어 있는 짝을 찾습니다. 그다음, 그 둘을 제거한 뒤, 앞뒤로 문자열을 이어 붙입니다. 이 과정을 반복해서 문자열을 모두 제거한다면 짝지어 제거하기가 종료됩니다. 문자열 S가 주어졌을 때, 짝지어 제거하기를 성공적으로 수행할 수 있는지 반환하는 함수를 완성해 주세요. 성공적으로 수행할 수 있으면 1을, 아닐 경우 0을 리턴해주면 됩니다.
# 예를 들어, 문자열 S = baabaa 라면
# b aa baa → bb aa → aa →
# 의 순서로 문자열을 모두 제거할 수 있으므로 1을 반환합니다.
# 제한사항
# 문자열의 길이 : 1,000,000이하의 자연수
# 문자열은 모두 소문자로 이루어져 있습니다.

def solution(s):
    list_s = []
    i = 0
    while (i < len(s)):
        if len(list_s) == 0:
            list_s.append(s[i])
        elif list_s[-1] == s[i]:
            list_s.pop()
        else:
            list_s.append(s[i])
        i += 1
    return 1 if len(list_s) == 0 else 0

# Leo는 카펫을 사러 갔다가 아래 그림과 같이 중앙에는 노란색으로 칠해져 있고 테두리 1줄은 갈색으로 칠해져 있는 격자 모양 카펫을 봤습니다.
# Leo는 집으로 돌아와서 아까 본 카펫의 노란색과 갈색으로 색칠된 격자의 개수는 기억했지만, 전체 카펫의 크기는 기억하지 못했습니다.
# Leo가 본 카펫에서 갈색 격자의 수 brown, 노란색 격자의 수 yellow가 매개변수로 주어질 때 카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하도록 solution 함수를 작성해주세요.
# 제한사항
# 갈색 격자의 수 brown은 8 이상 5,000 이하인 자연수입니다.
# 노란색 격자의 수 yellow는 1 이상 2,000,000 이하인 자연수입니다.
# 카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 깁니다.
# 입출력 예
# brown	yellow	return
# 10	2	[4, 3]
# 8	1	[3, 3]
# 24	24	[8, 6]

def solution(brown, yellow):
    box = brown + yellow
    list_divisor = [i for i in range(1, box+1) if box % i == 0]
    
    for height in list_divisor:
        width = box // height
        if width < height:
            continue
        if (width - 2) * (height - 2) == yellow:
            return [width, height]

# 두 수의 최소공배수(Least Common Multiple)란 입력된 두 수의 배수 중 공통이 되는 가장 작은 숫자를 의미합니다. 예를 들어 2와 7의 최소공배수는 14가 됩니다. 정의를 확장해서, n개의 수의 최소공배수는 n 개의 수들의 배수 중 공통이 되는 가장 작은 숫자가 됩니다. n개의 숫자를 담은 배열 arr이 입력되었을 때 이 수들의 최소공배수를 반환하는 함수, solution을 완성해 주세요.
# 제한 사항
# arr은 길이 1이상, 15이하인 배열입니다.
# arr의 원소는 100 이하인 자연수입니다.

def solution(arr):
    i = arr[-1]
    while(i):
        count = 0
        for j in arr:
            if i % j != 0:
                continue
            else:
                count += 1

        if(count == len(arr)):
            return i
        i += arr[-1]

# OO 연구소는 한 번에 K 칸을 앞으로 점프하거나, (현재까지 온 거리) x 2 에 해당하는 위치로 순간이동을 할 수 있는 특수한 기능을 가진 아이언 슈트를 개발하여 판매하고 있습니다. 이 아이언 슈트는 건전지로 작동되는데, 순간이동을 하면 건전지 사용량이 줄지 않지만, 앞으로 K 칸을 점프하면 K 만큼의 건전지 사용량이 듭니다. 그러므로 아이언 슈트를 착용하고 이동할 때는 순간 이동을 하는 것이 더 효율적입니다. 아이언 슈트 구매자는 아이언 슈트를 착용하고 거리가 N 만큼 떨어져 있는 장소로 가려고 합니다. 단, 건전지 사용량을 줄이기 위해 점프로 이동하는 것은 최소로 하려고 합니다. 아이언 슈트 구매자가 이동하려는 거리 N이 주어졌을 때, 사용해야 하는 건전지 사용량의 최솟값을 return하는 solution 함수를 만들어 주세요.
# 예를 들어 거리가 5만큼 떨어져 있는 장소로 가려고 합니다.
# 아이언 슈트를 입고 거리가 5만큼 떨어져 있는 장소로 갈 수 있는 경우의 수는 여러 가지입니다.
# 처음 위치 0 에서 5 칸을 앞으로 점프하면 바로 도착하지만, 건전지 사용량이 5 만큼 듭니다.
# 처음 위치 0 에서 2 칸을 앞으로 점프한 다음 순간이동 하면 (현재까지 온 거리 : 2) x 2에 해당하는 위치로 이동할 수 있으므로 위치 4로 이동합니다. 이때 1 칸을 앞으로 점프하면 도착하므로 건전지 사용량이 3 만큼 듭니다.
# 처음 위치 0 에서 1 칸을 앞으로 점프한 다음 순간이동 하면 (현재까지 온 거리 : 1) x 2에 해당하는 위치로 이동할 수 있으므로 위치 2로 이동됩니다. 이때 다시 순간이동 하면 (현재까지 온 거리 : 2) x 2 만큼 이동할 수 있으므로 위치 4로 이동합니다. 이때 1 칸을 앞으로 점프하면 도착하므로 건전지 사용량이 2 만큼 듭니다.
# 위의 3가지 경우 거리가 5만큼 떨어져 있는 장소로 가기 위해서 3번째 경우가 건전지 사용량이 가장 적으므로 답은 2가 됩니다.
# 제한 사항
# 숫자 N: 1 이상 10억 이하의 자연수
# 숫자 K: 1 이상의 자연수

def solution(n):
    return bin(n).count('1')

# 1부터 n까지 번호가 붙어있는 n명의 사람이 영어 끝말잇기를 하고 있습니다. 영어 끝말잇기는 다음과 같은 규칙으로 진행됩니다.
# 1번부터 번호 순서대로 한 사람씩 차례대로 단어를 말합니다.
# 마지막 사람이 단어를 말한 다음에는 다시 1번부터 시작합니다.
# 앞사람이 말한 단어의 마지막 문자로 시작하는 단어를 말해야 합니다.
# 이전에 등장했던 단어는 사용할 수 없습니다.
# 한 글자인 단어는 인정되지 않습니다.
# 다음은 3명이 끝말잇기를 하는 상황을 나타냅니다.
# tank → kick → know → wheel → land → dream → mother → robot → tank
# 위 끝말잇기는 다음과 같이 진행됩니다.
# 1번 사람이 자신의 첫 번째 차례에 tank를 말합니다.
# 2번 사람이 자신의 첫 번째 차례에 kick을 말합니다.
# 3번 사람이 자신의 첫 번째 차례에 know를 말합니다.
# 1번 사람이 자신의 두 번째 차례에 wheel을 말합니다.
# (계속 진행)
# 끝말잇기를 계속 진행해 나가다 보면, 3번 사람이 자신의 세 번째 차례에 말한 tank 라는 단어는 이전에 등장했던 단어이므로 탈락하게 됩니다.
# 사람의 수 n과 사람들이 순서대로 말한 단어 words 가 매개변수로 주어질 때, 가장 먼저 탈락하는 사람의 번호와 그 사람이 자신의 몇 번째 차례에 탈락하는지를 구해서 return 하도록 solution 함수를 완성해주세요.

def solution(n, words):
    told_words = []
    last_word = words[0][0]
    index = 0
    for i in words:
        index += 1
        if(last_word != i[0] or i in told_words):
            return [n if index % n == 0 else index % n, (index - 1) // n + 1]
        told_words.append(i)
        last_word = i[-1]
    return [0,0]

# 무인도에 갇힌 사람들을 구명보트를 이용하여 구출하려고 합니다. 구명보트는 작아서 한 번에 최대 2명씩 밖에 탈 수 없고, 무게 제한도 있습니다.
# 예를 들어, 사람들의 몸무게가 [70kg, 50kg, 80kg, 50kg]이고 구명보트의 무게 제한이 100kg이라면 2번째 사람과 4번째 사람은 같이 탈 수 있지만 1번째 사람과 3번째 사람의 무게의 합은 150kg이므로 구명보트의 무게 제한을 초과하여 같이 탈 수 없습니다.
# 구명보트를 최대한 적게 사용하여 모든 사람을 구출하려고 합니다.
# 사람들의 몸무게를 담은 배열 people과 구명보트의 무게 제한 limit가 매개변수로 주어질 때, 모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값을 return 하도록 solution 함수를 작성해주세요.
# 제한사항
# 무인도에 갇힌 사람은 1명 이상 50,000명 이하입니다.
# 각 사람의 몸무게는 40kg 이상 240kg 이하입니다.
# 구명보트의 무게 제한은 40kg 이상 240kg 이하입니다.
# 구명보트의 무게 제한은 항상 사람들의 몸무게 중 최댓값보다 크게 주어지므로 사람들을 구출할 수 없는 경우는 없습니다.
# 입출력 예
# people	limit	return
# [70, 50, 80, 50]	100	3
# [70, 80, 50]	100	3

def solution(people, limit):
    people.sort()
    light, heavy = 0, len(people) - 1
    boat = 0
    while light <= heavy:
        if people[light] + people[heavy] <= limit:
            light += 1
        heavy -= 1
        boat += 1
    return boat

# 경화는 과수원에서 귤을 수확했습니다. 경화는 수확한 귤 중 'k'개를 골라 상자 하나에 담아 판매하려고 합니다. 그런데 수확한 귤의 크기가 일정하지 않아 보기에 좋지 않다고 생각한 경화는 귤을 크기별로 분류했을 때 서로 다른 종류의 수를 최소화하고 싶습니다.
# 예를 들어, 경화가 수확한 귤 8개의 크기가 [1, 3, 2, 5, 4, 5, 2, 3] 이라고 합시다. 경화가 귤 6개를 판매하고 싶다면, 크기가 1, 4인 귤을 제외한 여섯 개의 귤을 상자에 담으면, 귤의 크기의 종류가 2, 3, 5로 총 3가지가 되며 이때가 서로 다른 종류가 최소일 때입니다.
# 경화가 한 상자에 담으려는 귤의 개수 k와 귤의 크기를 담은 배열 tangerine이 매개변수로 주어집니다. 경화가 귤 k개를 고를 때 크기가 서로 다른 종류의 수의 최솟값을 return 하도록 solution 함수를 작성해주세요.

def solution(k, tangerine):
    tangerine
    dict = {}

    for num in tangerine:
        if num in dict:
            dict[num] += 1
        else:
            dict[num] = 1
    sorted_dict = sorted(dict.items(),key=lambda x:(x[1],x[0]),reverse=True)

    result = 0
    total = 0
    for key, value in sorted_dict:
        if total >= k:
            break
        total += value
        result += 1

    return result

# 효진이는 멀리 뛰기를 연습하고 있습니다. 효진이는 한번에 1칸, 또는 2칸을 뛸 수 있습니다. 칸이 총 4개 있을 때, 효진이는
# (1칸, 1칸, 1칸, 1칸)
# (1칸, 2칸, 1칸)
# (1칸, 1칸, 2칸)
# (2칸, 1칸, 1칸)
# (2칸, 2칸)
# 의 5가지 방법으로 맨 끝 칸에 도달할 수 있습니다. 멀리뛰기에 사용될 칸의 수 n이 주어질 때, 효진이가 끝에 도달하는 방법이 몇 가지인지 알아내, 여기에 1234567를 나눈 나머지를 리턴하는 함수, solution을 완성하세요. 예를 들어 4가 입력된다면, 5를 return하면 됩니다.

def solution(n):   
    dp = [0, 1, 2]
    for i in range(3, n+1):
        dp.append(dp[i-1] + dp[i-2])
    return dp[n] % 1234567

# △△ 게임대회가 개최되었습니다. 이 대회는 N명이 참가하고, 토너먼트 형식으로 진행됩니다. N명의 참가자는 각각 1부터 N번을 차례대로 배정받습니다. 그리고, 1번↔2번, 3번↔4번, ... , N-1번↔N번의 참가자끼리 게임을 진행합니다. 각 게임에서 이긴 사람은 다음 라운드에 진출할 수 있습니다. 이때, 다음 라운드에 진출할 참가자의 번호는 다시 1번부터 N/2번을 차례대로 배정받습니다. 만약 1번↔2번 끼리 겨루는 게임에서 2번이 승리했다면 다음 라운드에서 1번을 부여받고, 3번↔4번에서 겨루는 게임에서 3번이 승리했다면 다음 라운드에서 2번을 부여받게 됩니다. 게임은 최종 한 명이 남을 때까지 진행됩니다.
# 이때, 처음 라운드에서 A번을 가진 참가자는 경쟁자로 생각하는 B번 참가자와 몇 번째 라운드에서 만나는지 궁금해졌습니다. 게임 참가자 수 N, 참가자 번호 A, 경쟁자 번호 B가 함수 solution의 매개변수로 주어질 때, 처음 라운드에서 A번을 가진 참가자는 경쟁자로 생각하는 B번 참가자와 몇 번째 라운드에서 만나는지 return 하는 solution 함수를 완성해 주세요. 단, A번 참가자와 B번 참가자는 서로 붙게 되기 전까지 항상 이긴다고 가정합니다.
# 제한사항
# N : 21 이상 220 이하인 자연수 (2의 지수 승으로 주어지므로 부전승은 발생하지 않습니다.)
# A, B : N 이하인 자연수 (단, A ≠ B 입니다.)

def solution(n,a,b):
    answer = 0
    player1 = a
    player2 = b
    while (player1 != player2):
        player1 = (player1 + 1) // 2
        player2 = (player2 + 1) // 2
        answer += 1
    return answer

# 철호는 수열을 가지고 놀기 좋아합니다. 어느 날 철호는 어떤 자연수로 이루어진 원형 수열의 연속하는 부분 수열의 합으로 만들 수 있는 수가 모두 몇 가지인지 알아보고 싶어졌습니다. 원형 수열이란 일반적인 수열에서 처음과 끝이 연결된 형태의 수열을 말합니다. 예를 들어 수열 [7, 9, 1, 1, 4] 로 원형 수열을 만들면 다음과 같습니다.
# 원형 수열은 처음과 끝이 연결되어 끊기는 부분이 없기 때문에 연속하는 부분 수열도 일반적인 수열보다 많아집니다.
# 원형 수열의 모든 원소 elements가 순서대로 주어질 때, 원형 수열의 연속 부분 수열 합으로 만들 수 있는 수의 개수를 return 하도록 solution 함수를 완성해주세요.

def solution(elements):
    n = len(elements)
    elements = elements * 2
    set_sum = set()
    for i in range(1, n+1):
        for j in range(n):
            sub_sum = sum(elements[j:j + i])
            set_sum.add(sub_sum)
    return len(set_sum)

# XYZ 마트는 일정한 금액을 지불하면 10일 동안 회원 자격을 부여합니다. XYZ 마트에서는 회원을 대상으로 매일 한 가지 제품을 할인하는 행사를 합니다. 할인하는 제품은 하루에 하나씩만 구매할 수 있습니다. 알뜰한 정현이는 자신이 원하는 제품과 수량이 할인하는 날짜와 10일 연속으로 일치할 경우에 맞춰서 회원가입을 하려 합니다.
# 예를 들어, 정현이가 원하는 제품이 바나나 3개, 사과 2개, 쌀 2개, 돼지고기 2개, 냄비 1개이며, XYZ 마트에서 14일간 회원을 대상으로 할인하는 제품이 날짜 순서대로 치킨, 사과, 사과, 바나나, 쌀, 사과, 돼지고기, 바나나, 돼지고기, 쌀, 냄비, 바나나, 사과, 바나나인 경우에 대해 알아봅시다. 첫째 날부터 열흘 간에는 냄비가 할인하지 않기 때문에 첫째 날에는 회원가입을 하지 않습니다. 둘째 날부터 열흘 간에는 바나나를 원하는 만큼 할인구매할 수 없기 때문에 둘째 날에도 회원가입을 하지 않습니다. 셋째 날, 넷째 날, 다섯째 날부터 각각 열흘은 원하는 제품과 수량이 일치하기 때문에 셋 중 하루에 회원가입을 하려 합니다.
# 정현이가 원하는 제품을 나타내는 문자열 배열 want와 정현이가 원하는 제품의 수량을 나타내는 정수 배열 number, XYZ 마트에서 할인하는 제품을 나타내는 문자열 배열 discount가 주어졌을 때, 회원등록시 정현이가 원하는 제품을 모두 할인 받을 수 있는 회원등록 날짜의 총 일수를 return 하는 solution 함수를 완성하시오. 가능한 날이 없으면 0을 return 합니다.

def solution(want, number, discount):
    list1 = list(zip(want, number))
    answer = 0
    k = 0
    while(k+9<len(discount)):
        dict = {}
        for num in discount[k:k+10]:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1
        
        is_valid = True
        for i,j in list1:
            if (dict.get(i,0) < j):
                is_valid = False
                break
        if is_valid:
            answer += 1
        k += 1
    return answer

# 다음 규칙을 지키는 문자열을 올바른 괄호 문자열이라고 정의합니다.
# (), [], {} 는 모두 올바른 괄호 문자열입니다.
# 만약 A가 올바른 괄호 문자열이라면, (A), [A], {A} 도 올바른 괄호 문자열입니다. 예를 들어, [] 가 올바른 괄호 문자열이므로, ([]) 도 올바른 괄호 문자열입니다.
# 만약 A, B가 올바른 괄호 문자열이라면, AB 도 올바른 괄호 문자열입니다. 예를 들어, {} 와 ([]) 가 올바른 괄호 문자열이므로, {}([]) 도 올바른 괄호 문자열입니다.
# 대괄호, 중괄호, 그리고 소괄호로 이루어진 문자열 s가 매개변수로 주어집니다. 이 s를 왼쪽으로 x (0 ≤ x < (s의 길이)) 칸만큼 회전시켰을 때 s가 올바른 괄호 문자열이 되게 하는 x의 개수를 return 하도록 solution 함수를 완성해주세요.

def solution(s):
    answer = 0
    rotate = lambda s: s[1:] + s[0]
    for i in range(len(s)):
        s = rotate(s)

        list_pop = []
        is_valid = True
        for j in s:
            if j == "[" or j == "(" or j == "{":
                list_pop.append(j)
            else:
                if list_pop == []:
                    is_valid = False #유효성 검사 필요
                    break
                else:
                    if list_pop[-1] == "[" and j == "]":
                        list_pop.pop()
                    elif list_pop[-1] == "(" and j == ")":
                        list_pop.pop()
                    elif list_pop[-1] == "{" and j == "}":
                        list_pop.pop()
                    else:
                        is_valid = False #유효성 검사 필요
                        break
        if is_valid and not list_pop:
            answer += 1
    return answer

# 위와 같은 삼각형의 꼭대기에서 바닥까지 이어지는 경로 중, 거쳐간 숫자의 합이 가장 큰 경우를 찾아보려고 합니다. 아래 칸으로 이동할 때는 대각선 방향으로 한 칸 오른쪽 또는 왼쪽으로만 이동 가능합니다. 예를 들어 3에서는 그 아래칸의 8 또는 1로만 이동이 가능합니다.
# 삼각형의 정보가 담긴 배열 triangle이 매개변수로 주어질 때, 거쳐간 숫자의 최댓값을 return 하도록 solution 함수를 완성하세요.

def solution(triangle):
    for i in range(len(triangle)-2,-1,-1):
        for j in range(len(triangle[i])):
            triangle[i][j] += max(triangle[i+1][j],triangle[i+1][j+1])
    return triangle[0][0]

# 백준 단계별로 풀어보기

# 아래 예제와 같이 새싹을 출력하시오.

print("         ,r'\"7\n"+
"r`-_   ,'  ,/\n"+
" \. \". L_r'\n"+
"   `~\/\n"+
"      |\n"+
"      |\n")
