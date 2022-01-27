import itertools


# number = "4177252841"
# k=4
# ma = 0
# nums = list(number)
# for i in range(len(nums)):
#     nums[i] = int(nums[i])
# ans = [0]*(len(nums)-k)
# # 전처리

# for i in range(k):
#     if nums[i] > ma:
#         ma = nums[i]
# ans[0] = ma

# print(ans)

moves = [1,5,3,5,1,2,1,4]
board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
basket = []
count = 0

answer = list(map(list, zip(*board)))
print(answer)

list = [[] for i in range(len(board))]
for i in range(len(board)):
    for j in range(len(board)):
        if board[j][i] !=0:
            list[i].append(board[j][i])
# for i in moves:
#     if len(list[i-1])!=0 and len(basket)==0:
#         basket.append(list[i-1].pop(0))
#     elif len(list[i-1])!=0 and len(basket)!=0:
#         if list[i-1][0] == basket[-1]:
#             del basket[-1]
#             del list[i-1][0]
#             count += 2
#         else:
#             basket.append(list[i-1].pop(0))

print(list)