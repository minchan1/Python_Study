# KAKAO - 후보키
# https://programmers.co.kr/learn/courses/30/lessons/42890

# 유일성 : 모든 로우를 구별 가능해야 함
# 최소성 : 유일성을 만족하는 조합 중에서 가장 작은 것

from itertools import combinations

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
nums = []
for i in range(len(relation[0])):
    nums.append(i)
n = len(nums)
# relation의 컬럼 수 만큼 조합을 생성

combi = []
for i in range(1, n+1):
    combi.extend(combinations(nums, i))
# print(combi)
    
ans = []
for i in combi:
    tmp = [tuple([item[key] for key in i]) for item in relation]
    # print(tmp)
    if len(set(tmp)) == len(relation):
        # 유일성
        # 중복 제거한 tmp와 relation의 원소수 비교 
        for x in ans:
            if set(x).issubset(set(i)):  
                # 최소성
                # 유일성을 만족하는 튜플이 부분집합이면 최소성 탈락
                break
        # 부분집합이 아닌 경우에만 ans에 추가
        else: ans.append(i)
# print(ans)
print(len(ans))

# 조이스틱
# https://programmers.co.kr/learn/courses/30/lessons/42860


# name = "JEROEN"
# tmp = list(name)
# ans = 0
# for i in tmp:
#     k = ord(i)-65
#     ans += min(k,26-k)
# print(ans)

# def solution(name):
#     init_A = list("A"*len(name))
#     name=list(name)
#     TF=[]
#     for a,b in zip(name,init_A):
#         TF.append(a==b)  
#     count=move_count(TF,0,0)
#     for alpha in name:
#         tmp=ord(alpha)-ord("A")
#         count+=min(ord(alpha)-ord("A"),ord("Z")-ord(alpha)+1)
#     return count

# def move_count(TF,point,count):
#     if sum(TF)==len(TF):
#         return count
#     else:
#         tmp_all=[]
#         target_index=[]
#         tmp_TF=TF.copy()
#         target_index_count=0
        
#         while len(target_index) <= 1:
#             if not TF[(point+target_index_count)%len(TF)]:
#                 target_index.append((point+target_index_count)%len(TF))
#             if not TF[(point-target_index_count)%len(TF)]:
#                 target_index.append((point-target_index_count)%len(TF))
#             target_index_count+=1

#         for i in set(target_index):
#             if not TF[i]:
#                 tmp_TF=TF.copy()
#                 tmp_TF[i]=True
#                 tmp_all.append(move_count(tmp_TF,i,count+min(len(TF)-abs(point-i),abs(point-i))))
#         return min(tmp_all)