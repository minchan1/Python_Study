# 문제 1
# https://programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    n = len(nums)/2
    m=len(set(nums))
    if m > n:
        return n
    else :
        return m


# 문제 2
# https://programmers.co.kr/learn/courses/30/lessons/12982

def solution(d, budget):
    d = sorted(d)
    n = 0
    m = 0
    if d[0] > budget:
        return 0
    for i in d:
        if m < budget:
            m += i
            n += 1
        elif m == budget:
            break
        else :
            n = n-1
            break
    return n


# 문제 3
# https://programmers.co.kr/learn/courses/30/lessons/12926

def solution(s, n):
    s=list(s)
    for i in range(len(s)):
        if ord(s[i])==32:
            pass
        elif ord(s[i])>=97:
            s[i] = chr((ord(s[i])-97+n)%26 + 97)
        elif ord(s[i])<97:
            s[i] = chr((ord(s[i])-65+n)%26 + 65)
    a=''.join(s)
    return(a)