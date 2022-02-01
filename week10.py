# 전화번호 목록
# https://programmers.co.kr/learn/courses/30/lessons/42577


#1 : 시간초과 나옴
def solution(phone_book):
    for i in phone_book:
        for j in phone_book:
            k = len(i)
            if i!=j and j[:k]==i:
            # 각 원소마다 맨앞 성분을 확인
                return False
    else:
        return True

#2 
def solution(phone_book):
    pb = sorted(phone_book)
    # 원소들이 문자열이기 때문에
    # 숫자의 크기순이 아닌, 문자열의 문자들 각각의 순서로 정렬 
    # ex) 12,123,1234,55,666 ... 
    for i in range(len(pb)-1):
        k = len(pb[i])
        if pb[i]==pb[i+1][:k]:
            return False
        # 접두사인 경우엔 바로 뒤로 오게 되기때문에
        # 뒤의 원소하고만 비교하면 됨
    else:
        return True



# 뉴스 클러스터링
# https://programmers.co.kr/learn/courses/30/lessons/17677

# 전처리 해주는 함수
# 두글자씩 끊고, 알파벳으로만 구성된 원소만 남긴다.
def func(str):
    tmp=[]
    for i in range(len(list(str))-1):
        tmp.append(list(str)[i]+list(str)[i+1])
    result = [i.lower() for i in tmp if i.isalpha()==True]
    return result

def solution(str1, str2):
    li1,li2 = func(str1),func(str2)

    # 합집합과 교집합을 구한다
    inter=[]
    for i in li1:
        if i in li2:
            inter.append(i)
            li2.remove(i)
    union = li1 + li2
    
    # 유사도 = 교집합 원소수 / 합집합 원소수
    # 교집합이 공집합인 경우 처리
    if union:
        ans = int((len(inter)/len(union))*65536)
    else:
        ans = 65536
    return ans

