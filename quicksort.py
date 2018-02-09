
def quicksorter(myList, first, last):

    if first < last:
        splitpoint = partition(myList, first, last)

        quicksorter(myList, first, splitpoint - 1)
        quicksorter(myList, splitpoint + 1, last)

def partition(myList, first, last):
    pivotValue = myList[first]
    leftIndex = first + 1
    rightIndex = last

    done = False

    while not done:
        while leftIndex <= rightIndex and myList[leftIndex] <= pivotValue:
            leftIndex = leftIndex + 1

        while myList[rightIndex] >= pivotValue and rightIndex >= leftIndex:
            rightIndex = rightIndex -  1

        if rightIndex < leftIndex:
            done = True
        else: 
            tmp = myList[leftIndex]
            myList[leftIndex] = myList[rightIndex]
            myList[rightIndex] = tmp

    tmp = myList[first]
    myList[first] = myList[rightIndex]
    myList[rightIndex] = tmp

    return rightIndex

myList = [54,36, 20, 21, 22, 23, 24, 44, 42, 55]
print(myList)
quicksorter(myList, 0, len(myList) - 1)
print(myList)