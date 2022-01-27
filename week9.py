# 크레인
# https://programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    basket = [] # 뽑은 인형을 놓을 바구니
    count = 0 # 사라진 인형 갯수
    list = [[] for i in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board)):
            if board[j][i] !=0:
                list[i].append(board[j][i])
    # 열 단위로 인형을 뽑기 때문에
    # 행,열을 바꾸고 0은 제거하여 인형만 인덱싱하기 쉽게 만듬

    for i in moves:
        if len(list[i-1])!=0 and len(basket)==0:
            basket.append(list[i-1].pop(0))
        # 해당 위치에 인형이 존재하고, 바구니가 비어 있으면
        # 딱히 고려할 것 없이 넣으면 됨
        elif len(list[i-1])!=0 and len(basket)!=0:
            if list[i-1][0] == basket[-1]:
                del basket[-1]
                del list[i-1][0]
                count += 2
        # 바구니가 비어있지 않고, 현재 바구니의 맨위의 인형이
        # 다음 뽑으려는 인형과 같으면, 둘다 삭제하고 2번 카운트함
            else:
                basket.append(list[i-1].pop(0))
    return count



# 비밀지도
# https://programmers.co.kr/learn/courses/30/lessons/17681


def solution(n, arr1, arr2):
    answer = [[' ']*n for i in range(n)]
    # 공백으로된 리스트 생성
    for i in range(n):
        # 이진법으로 바꾸고, 문자열의 길이를 n으로 맞춤
        arr1[i] = bin(arr1[i])[2:]
        if len(arr1[i])!=n:
            while len(arr1[i])!=n:
                arr1[i] = '0' + arr1[i]
        arr2[i] = bin(arr2[i])[2:]
        if len(arr2[i])!=n:
            while len(arr2[i])!=n:
                arr2[i] = '0' + arr2[i]

    for i in range(n):
        for j in range(n):
                if arr1[i][j] == str(1) or arr2[i][j]==str(1):
                    answer[i][j] = '#'
    # 1이 존재하는 위치를 #으로 바꿈

    for i in range(n):
        for j in range(1,n):
            answer[i][0] += str(answer[i][j])
        answer[i] = answer[i][0]
    # 출력 형태에 맞추기

    return(answer)



# 주차요금
# https://programmers.co.kr/learn/courses/30/lessons/92341

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
car = []
for i in records:
    car.append(i.split()[1])
car = list(set(car)) # 차번호 리스트 생성
car = sorted(car)
time = {i:0 for i in car} # 차마다 머문 누적시간 기록
# print(time)

in_out = {} # 출차내역을 기록
for i in records:
    rec = i.split(' ')
    if rec[1] not in in_out.keys():   
        in_out[rec[1]] = rec[0]  # 해당 차번호가 없으면 들어온 시간 기록
    else:
        a = int(in_out[rec[1]].split(':')[0]) * 60 + int(in_out[rec[1]].split(':')[1]) # 들어온 시간
        b = int(rec[0].split(':')[0]) * 60 + int(rec[0].split(':')[1]) # 나간 시간
        time[rec[1]] = time[rec[1]] + (b-a) 
        del in_out[rec[1]]

if len(in_out)!=0: # 23시59분 까지 안나간 차들 처리
    for i in in_out.keys():
        a = int(in_out[i].split(':')[0]) * 60 + int(in_out[i].split(':')[1]) # 들어온 시간
        b = 23*60 + 59 # 나간 시간 (23시 59분)
        time[i] = time[i] + (b-a)

total = [] # 최종 요금
for i in car: # 미리 오름차순으로 정리해놓음
    if time[i] <= fees[0]:
        total.append(fees[1])
    else :
        if (time[i]-fees[0])%fees[2]==0: # 단위시간으로 나눠떨어지면 : 기본요금 + 단위요금*시간
            total.append(fees[1]+fees[3]*((time[i]-fees[0])//fees[2]))
        else: # 아니면 : 기본요금 + 단위요금*(시간+1)
            total.append(fees[1]+fees[3]*((time[i]-fees[0])//fees[2])+fees[3])
print(total)