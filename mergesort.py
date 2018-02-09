def mergesort (m) :

    if (len(m) == 1):
        return m

    left = []
    right = []

    for i in range(len(m)):
        if (i < len(m) / 2): 
            left.append(m[i])
        else:
            right.append(m[i])

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)

def merge (a, b): 
    print(a)
    print(b)
    r = []
    while len(a) is not 0 and len(b) is not 0:
        if a[0] < b[0]:
            r.append(a.pop(0))
        else:
            r.append(b.pop(0))


    while len(a) is not 0:
        r.append(a.pop(0))

    while len(b) is not 0:
        r.append(b.pop(0))

    return r

myM = [23, 35, 22, 14, 16, 23, 28, 35]
p = mergesort(myM)
print(p)