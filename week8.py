#1. https://programmers.co.kr/learn/courses/30/lessons/92334


# 시간초과 나옴
def solution(id_list, report, k):
    report_set = set(report)
    report=list(report_set)
    # 중복제거
    a=[]
    answer=[0]*len(id_list) 
    for i in report:
        a.append(i.split(' ').pop())
        # 신고당한 대상만 분리
        # 신고 한 사람??? <--
    b= [i for i in id_list if a.count(i)>=k]
    # 신고 당한 횟수 k이상인 사람 고르기
    for i in range(len(id_list)):
        for j in b:
            if f'{id_list[i]} {j}' in report:
                answer[i] += 1
    # 이 부분의 연산 줄여야함
    return(answer)


#2. https://programmers.co.kr/learn/courses/30/lessons/12921

# 참고) 에라토스테네스의 체 (위키 펌)
# 범위내 소수의 목록을 return해줌
def prime_list(n):
    sieve = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:      
            for j in range(i+i, n, i):
                sieve[j] = False
    return [i for i in range(2, n) if sieve[i] == True]

# 위의 함수를 변형해보자
def primes(n):
    # 일단 전부 소수라고 가정
    # 문제에서는 n 자신도 포함해서 검사 하므로 범위를 n+1까지
    nums = [True] * (n+1)
    # 1은 제외, 2부터 루트n까지 검사
    for i in range(2, int(n**0.5)+1):
        if nums[i] == True:      
            # i의 배수들을 전부 제외한다
            for j in range(i+i, n+1, i):
                nums[j] = False
    # 소수인 i리스트의 길이가 곧 갯수가 된다
    return len([i for i in range(2, n+1) if nums[i] == True])


#3. https://programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    # 우선 문자들을 원소로하는 리스트로 변환하자
    a = list(s)
    # 1번 인덱스부터 for문 돌릴거라서 0번인덱스 따로처리해줌
    a[0] = a[0].upper()
    # 앞의 원소가 공백이면 대문자로 바꾸고, 나머지는 전부 소문자로
    for i in range(1,len(a)):
        if a[i-1]==' ':
            a[i]=a[i].upper()
        else:
            a[i]=a[i].lower()
    # 문자열로 다시 바꿔서 리턴해준다
    return(''.join(a))

# 더 짧게 만들수 있을까???
def solution(s):
    a = list(s)
    a[0] = a[0].upper()
    for i in range(1,len(a)):
        a[i]=a[i].upper() if a[i-1]==' ' else a[i].lower()
    return(''.join(a))