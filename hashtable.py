class HashTable:
    def __init__(self):
        self.list = [[0 for x in range(0)] for y in range(10)]
    def get(self, key):
        return self.list[self.hash(key)]

    def set(self, key, value):
        key = self.hash(key)
        if (self.list[key] is None):
            self.list[key] = []
        self.list[key].append(value)

    def hash(self, key):
        total = 0
        for c in key:
            total = total + ord(c)

        return total % len(self.list)
    def print(self):
        print(self.list)

h = HashTable()
h.set('horse', 'dave')
h.set('horse', 'jude')

h.set('cat', 'river')
print(h.get('horse'))    
print(h.get('cat'))