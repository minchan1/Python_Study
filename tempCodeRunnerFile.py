
#     if len(list[i-1])!=0 and len(basket)==0:
#         basket.append(list[i-1].pop(0))
#     elif len(list[i-1])!=0 and len(basket)!=0:
#         if list[i-1][0] == basket[-1]:
#             del basket[-1]
#             del list[i-1][0]
#             count += 2
#         else:
#             basket.append(list[i-1].pop(0))