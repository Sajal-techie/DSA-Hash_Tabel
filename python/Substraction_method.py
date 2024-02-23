class HashTable:
    def __init__(self, size):
        self.table = [None] * size
        self.size = size

    def hash_function(self, key):
        return key - 10

    def insert(self, key, value):
        new = self.hash_function(key)
        self.table[new] = value

    def get(self, key):
        new = self.hash_function(key)
        print(self.table[new])

    def remove(self, key):
        new = self.hash_function(key)
        self.table[new] = None

    def display(self):
        print(self.table)


ha = HashTable(5)
ha.insert(12,22)
ha.insert(13, 23)
ha.insert(14, 24)
ha.get(12)
ha.remove(12)
ha.get(12)
ha.display()
