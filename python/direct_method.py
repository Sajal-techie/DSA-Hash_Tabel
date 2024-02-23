class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * self.size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index] = value

    def search(self, key):
        index = self.hash_function(key)
        print(self.table[index])

    def remove(self, key):
        index = self.hash_function(key)
        if self.table[index]:
            self.table[index] = None

    def display(self):
        print(self.table)


hashh = HashTable(5)
hashh.insert(2,6)
hashh.insert(1,9)
hashh.insert(99,1)
hashh.search(99)
hashh.display()
hashh.insert(13,22)
hashh.display()