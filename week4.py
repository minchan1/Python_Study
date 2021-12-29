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