import itertools

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
combi = []
count_ = []
for i in orders:
    combi += itertools.combinations(sorted(i),2)
for i in combi:
    if combi.count(i) == 1:
        pass
    elif combi.count(i) >= 2:
        print(i)
    # count_ = combi.count(i)    
# print(combi.count(combi[1]))

def solution(orders, course):
    for i in orders:
        orders[i] = sorted(i)