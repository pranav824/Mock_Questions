# a = [7,6,4,3,1]
# max = a[0]
# min = a[0]
# profit = 0
# for i in a:
#     if i < min:
#         min = i
#         max = i
#     if i > max:
#         if profit < max:
#             max = i
# profit = max - min
# print(profit)
 
a = [7,6,4,3,1]
min = min(a)
max = 0
si = 0
profit = 0
for i in range(len(a)):
    if i == min:
        si = i
for i in range(si, len(a)):
    if a[i] > max:
        max = a[i]
    if profit < max:
        max = i
profit = max-min
print(profit)




