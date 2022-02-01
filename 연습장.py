
def solution(str1, str2):
    # 전처리
    # 두글자씩 끊고, 알파벳으로만 구성된 원소만 남긴다.
    temp1=[]
    temp2=[]
    for i in range(len(list(str1))-1):
        temp1.append(list(str1)[i]+list(str1)[i+1])
    for i in range(len(list(str2))-1):
        temp2.append(list(str2)[i]+list(str2)[i+1])
    li1 = [i.lower() for i in temp1 if i.isalpha()==True]
    li2 = [i.lower() for i in temp2 if i.isalpha()==True]

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