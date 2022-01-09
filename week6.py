# lv1
# https://programmers.co.kr/learn/courses/30/lessons/86491?language=python3

def solution(sizes):
    sizes_2 = []
    for i in range(len(sizes)):
        if sizes[i][0]>=sizes[i][1]:
            pass
        else:
            sizes[i] = [sizes[i][1],sizes[i][0]]
    for k in range(len(sizes)):
        sizes_2.append(sizes[k][1])
    max2 = max(sizes_2)
    max1 = max(sizes)[0]
    return max1*max2


# lv2 - kakao
# https://programmers.co.kr/learn/courses/30/lessons/72411?language=python3




# lv2 - 정사각형
# https://programmers.co.kr/learn/courses/30/lessons/12905?language=python3