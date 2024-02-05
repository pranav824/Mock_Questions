a = [12, 35, 1, 10, 34, 1]
for i in range(len(a)-1):
    b = i
    for j in range(i, len(a)):
        if a[j] < a[b]:
            b = j
    a[i], a[b] = a[b], a[i]
print(a)