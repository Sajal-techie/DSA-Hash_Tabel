class Hash:
    def __init__(self, size):
        self.table = [None] * size
        self.size = size
        self.count = 0
        self.threshold = .7

    def hash_func(self, key):
        key_value = 0
        for i in str(key):
            key_value += ord(i)
        print(key, key_value, 'kv')
        return key_value % self.size

    def insert(self, key, value):
        if self.count/self.size > self.threshold:
            self.resize()
        index = self.hash_func(key)
        print(key, index, "ind")
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            index = (index + 1) % self.size
            print(index, "ind2")
        self.table[index] = (key, value)
        self.count += 1

    def search(self, key):
        index = self.hash_func(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                print(self.table[index][1])
                return
            index = (index + 1) % self.size
        else:
            print("not found")

    def display(self):
        print(self.table)
        print(len(self.table))

    def remove(self, key):
        index = self.hash_func(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None
                self.count -= 1
                return
            index = (index + 1) % self.size
        else:
            print("key not found")

    def resize(self):
        new_size = self.size * 2
        new_table = [None] * new_size
        for i in self.table:
            if i is not None:
                key, value = i
                index = self.hash_func(key)
                while new_table[index] is not None:
                    index = (index + 1) % new_size
                new_table[index] = (key, value)
        self.size = new_size
        self.table = new_table


hai = Hash(5)
hai.insert('name', 'Sajal')
hai.search('name')
hai.insert('age', 11)
hai.insert('naem', 'sugu')
hai.insert('nae3m', 'sugu')
hai.insert('nae3m', 'sugu')
hai.insert('mane', 'kumar')
hai.insert('mnae', 'jiju')
hai.insert('hai','hello')
hai.insert('hais','hello')
# hai.insert('sda','asf')
hai.remove('name')
hai.display()