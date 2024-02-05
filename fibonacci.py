a = 7
n = 5
l = [0,1]
# nextNum = 0
# for i in range(a):
#     nextNum = l[-1] + l[-2]
#     l += [nextNum]
# print(l[n])
    
def fibo(a,n,l):
    nextNum = 0
    for i in range(a):
        nextNum = l[-1] + l[-2]
        l += [nextNum]
    return l[n]
print(fibo(a,n,l))