# 문제 1
# https://programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    return int(s.replace('zero','0').replace('one','1').replace('two','2').replace('three','3').replace('four','4').replace('five','5').replace('six','6').replace('seven','7').replace('eight','8').replace('nine','9'))


# 문제 2
# https://programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    left=10
    right=12
    answer='' 
    for k in range(len(numbers)):
        if numbers[k]==0:
            numbers[k]=11
    for i in numbers:
        if i%3==1:
            answer += 'L'
            left=i
        elif i%3==0:
            answer += 'R'
            right=i
        elif i%3==2:
            d_L=(abs(i-left)//3) + (abs(i-left)%3)
            d_R=(abs(i-right)//3) + (abs(i-right)%3)
            if d_R>d_L:
                answer += 'L'
                left=i
            elif d_L>d_R:
                answer += 'R'
                right=i
            elif d_L==d_R:
                if hand=='left':
                    answer += 'L'
                    left=i
                elif hand=='right':
                    answer += 'R'
                    right=i
    return answer


# 문제 3
# https://programmers.co.kr/learn/courses/30/lessons/76501

def solution(absolutes, signs):
    answer=0
    for i in range(len(signs)):
        if bool(signs[i]) == False :
            answer -= absolutes[i]
        elif bool(signs[i]) == True :
            answer += absolutes[i]
    return answer