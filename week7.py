# https://programmers.co.kr/learn/courses/30/lessons/42883
# 어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.
# 예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다. 
# 이 중 가장 큰 숫자는 94 입니다.

# 문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다. 
# number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 
# 문자열 형태로 return 하도록 solution 함수를 완성하세요.




# https://programmers.co.kr/learn/courses/30/lessons/12906
# 배열 arr가 주어집니다. 배열 arr의 각 원소는 숫자 0부터 9까지로 이루어져 있습니다. 
# 이때, 배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거하려고 합니다. 
# 단, 제거된 후 남은 수들을 반환할 때는 배열 arr의 원소들의 순서를 유지해야 합니다. 예를 들면,
# arr = [1, 1, 3, 3, 0, 1, 1] 이면 [1, 3, 0, 1] 을 return 합니다.
# arr = [4, 4, 4, 3, 3] 이면 [4, 3] 을 return 합니다.
# 배열 arr에서 연속적으로 나타나는 숫자는 제거하고 남은 수들을 return 하는 solution 함수를 완성해 주세요.





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
