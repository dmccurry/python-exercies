def bubble(a) :
    swap = True

    while swap:
        swap = False
        for i in range(len(a)):
            if i < len(a) - 1:
                if a[i+1] < a[i]:
                    tmp = a[i]
                    a[i] = a[i+1]
                    a[i+1] = tmp
                    swap = True
    return a

b = [41, 34, 36, 2, 35, 1]
print(b)
c = bubble(b)
print(c)