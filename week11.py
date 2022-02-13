# 숫자의 표현
# https://programmers.co.kr/learn/courses/30/lessons/12924

def solution(n):
    answer = 0 
    for i in range(1,n+1): 
        s = 0 
        for j in range(i,n+1):
            # i부터 자연수를 쭉 더함
            s += j
            if s == n: 
                answer += 1 
                break  
            elif s > n:
                break 
            # 합이 n과 같아지면 ans값에 1을더하고 break
            # 합이 n보다 커지면 break
    return answer


# N개의 최소공배수
# https://programmers.co.kr/learn/courses/30/lessons/12953

# 1
# math를 통해서 구하기 -> 통과 안됨
import math
def solution(arr):
    lcm = arr[0]
    for i in range(1,len(arr)):
        lcm = math.lcm(lcm,arr[i])
    return lcm
# 한번에 여러개의 숫자도 가능
# print(solution([2,6,8,14]))

# 2
# 직접 구하기

# 최대공약수 구하는 함수
def func(a,b):    
    while b:
        a,b=b,a%b
    return a # -> 두 수 a,b의 최대공약수

def solution(arr):
    a=arr[0]
    for i in range(1,len(arr)):
        b = arr[i]
        # 두 수 a,b의 최소공배수는 a*b/gcd
        gcd = func(a,b)
        lcm = a*b/gcd
        a = lcm
    return int(a)