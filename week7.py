# https://programmers.co.kr/learn/courses/30/lessons/42883
# 어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.
# 예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다. 
# 이 중 가장 큰 숫자는 94 입니다.

# 문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다. 
# number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 
# 문자열 형태로 return 하도록 solution 함수를 완성하세요.

# 옮긴 숫자들 중 K개의 한하여 왼편에 가장큰 숫자를 배치하는 코드
def getResult(answer, num, k):

	#answer 리스트 내에 값이 존재하며, 왼편이 작고, K의 여유가 있을경우
    while (answer) and (int(answer[len(answer)-1]) < num) and (k > 0):
    	#리스트 맨 뒷값 제거
        answer.pop()
        #K갯수 감소 
        k-=1
    #현재 숫자를 담는다
    answer.append(num)
    return answer,k

def solution(number, k):
    answer = []
	#왼편부터 숫자를 하나씩 꺼낸다
    for num in number:
        answer,k = getResult(answer,int(num),k
        
        
	#만약 K의 여유가 남았다면, 맨뒤에서 부터뺀다(왼편이 크도록 설계되었으므로)
    for _ in range(k):
        answer.pop()
    result=""
    #출력용
    for atom in answer:
        result+=str(atom)
    return result

# https://programmers.co.kr/learn/courses/30/lessons/12906
# 배열 arr가 주어집니다. 배열 arr의 각 원소는 숫자 0부터 9까지로 이루어져 있습니다. 
# 이때, 배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거하려고 합니다. 
# 단, 제거된 후 남은 수들을 반환할 때는 배열 arr의 원소들의 순서를 유지해야 합니다. 예를 들면,
# arr = [1, 1, 3, 3, 0, 1, 1] 이면 [1, 3, 0, 1] 을 return 합니다.
# arr = [4, 4, 4, 3, 3] 이면 [4, 3] 을 return 합니다.
# 배열 arr에서 연속적으로 나타나는 숫자는 제거하고 남은 수들을 return 하는 solution 함수를 완성해 주세요.


# 1번 풀이 ( 효율성 통과 실패함 )
def solution(arr):
    num = []
    for i in range(1,len(arr)):
        if arr[i] == arr[i-1]:
            num.append(i)
            # 원소가 중복된 인덱스번호를 알아낸다 
        else:
            pass
    num.reverse()
            # 앞에서부터 지우면 인덱스번호가 바뀌어버리므로
            # 뒤에서부터 인덱스 삭제
    for i in num:
        del arr[i]
    return arr

# 2번 풀이 
def solution(arr):
    # num = arr[0]
    # for문을 두번 사용하거나 주어진 배열을 계속 바꿔버리면
    # 연산이 늘어나기 때문에 변수를 사용하기로 함
    answer = [arr[0]]
    for i in range(1,len(arr)):
        if arr[i] != arr[i-1]:
            # num = arr[i]
            answer.append(arr[i])
        # 배열에서 숫자가 바뀔때마다 바뀐 숫자로 갱신 및 추가
    return answer

# 변수를 쓰는 이유를 생각해보자


# https://programmers.co.kr/learn/courses/30/lessons/77884
# 두 정수 left와 right가 매개변수로 주어집니다. 
# left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 
# 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.


def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        # 약수의 갯수가 홀수다 : 제곱수 
        # 제곱근이 정수가 아니면 더하고 정수이면 뺌
        if int(i**(1/2)) != i**(1/2):
            answer += i
        elif int(i**(1/2)) == i**(1/2):
            answer -= i
    return answer
