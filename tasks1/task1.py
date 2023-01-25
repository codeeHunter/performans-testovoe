n, m = (int(i) for i in input().split())
k = 0
a = []
b = []
b.append(1)

m -= 1
t = m


while (True):
    for i in range(0, n):
        a.append(i + 1)

    b.append(a[m])
    k += 1

    if (b[k] == 1):
        b.pop(k)
        break
    m += t 

print(*b)
