class QuickSortClass:

    def __init__(self):
        self.listObject = []

    def addItem(self, item):
        print ('adding ' + str(item))
        self.listObject.append(item)

    def setList(self, list):
        self.listObject = list

    def sort(self):
        self.listLength = len(self.listObject)
        self.doQuickSort(self.listObject, 0, self.listLength - 1)

    def doQuickSort(self, listObject, startIndex, lastIndex):
        if startIndex < lastIndex:
            pivot = self.partition(listObject, startIndex, lastIndex)
            self.doQuickSort(listObject, startIndex, pivot - 1)
            self.doQuickSort(listObject, pivot + 1, lastIndex)

    def partition(self, listObject, startIndex, lastIndex):
        pivotValue = listObject[startIndex]
        left = startIndex + 1
        right = lastIndex
        done = False

        while not done:
            while left <= right and listObject[left] <= pivotValue:
                left = left + 1
            while right >= left and listObject[right] >= pivotValue:
                right = right - 1
            
            if right < left:
                done = True
            else: 
                tmp = listObject[left]
                listObject[left] = listObject[right]
                listObject[right] = tmp
            
        
        tmp = listObject[startIndex]
        listObject[startIndex] = listObject[right]
        listObject[right] = tmp

        return right
    def printList(self):
        print(self.listObject)

someList = [22, 51, 32, 24, 26]
c = QuickSortClass()
"""for item in someList:
    c.addItem(item)

"""
c.setList(someList)
c.printList()
c.sort()
c.printList()