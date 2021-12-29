# 문제 1
# https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    answer = []
    supo1=[1,2,3,4,5]
    supo2=[2,1,2,3,2,4,2,5]
    supo3=[3,3,1,1,2,2,4,4,5,5]
    score=[0,0,0]
    while 1 :
        if len(answers) > len(supo1) :
            supo1 = supo1+supo1
        else :
            break
    for i in range(len(answers)):
        if supo1[i]==answers[i]:
            score[0]+=1
    while 2 :
        if len(answers) > len(supo2) :
            supo2 = supo2+supo2
        else :
            break
    for i in range(len(answers)):
        if supo2[i]==answers[i]:
            score[1]+=1
    while 3 :
        if len(answers) > len(supo3) :
            supo3 = supo3+supo3
        else :
            break
    for i in range(len(answers)):
        if supo3[i]==answers[i]:
            score[2]+=1

    for j in range(3):
        if score[j]==max(score):
            answer.append(j+1)
    
    return answer


# 문제 2
# https://programmers.co.kr/learn/courses/30/lessons/12954

def solution(x, n):
    answer = []
    for i in range(n):
        answer.append(x+x*i)
    return answer