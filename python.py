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

print(solution("1111111"))
