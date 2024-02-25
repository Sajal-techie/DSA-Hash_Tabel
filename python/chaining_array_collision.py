class Hashtable:
    def __init__(self, size = 5):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.count = 0

    def hash_func(self, key):
        key_value = 0
        for i in str(key):
            key_value += ord(i)
        return key_value % self.size

    def insert(self, key, value):
        index = self.hash_func(key)
        self.table[index].append((key, value))

    def search(self, key):
        index = self.hash_func(key)
        for k,v in self.table[index]:

            print(k,v)
            if k == key:
                print(k, v, 'founded')
                return
        else:
            print('not found')

    def remove(self, key):
        index = self.hash_func(key)
        for i in self.table[index]:
            k, v = i
            if k == key:
                del self.table[index]
                return
        else:
            print('not element ')

    def display(self):
        print(self.table)


hash = Hashtable(6)
hash.insert('abc', 'abc')
hash.insert('abd', 'bac')
hash.insert('bac', 'sui')
hash.insert('ab', 'sui')
hash.insert('ab', 'susi')
hash.insert('jai','hid')
# hash.insert('koko', 'asdf')
hash.display()
hash.remove('abc')
hash.search('abd')

hash.display()