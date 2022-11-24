# https://colab.research.google.com/drive/1QU5lj4juRxeyv4Nj2UIMEmxelvxFCGBV


# PROBLEM 2

# LINEAR PROBING
class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    def hash_function(self, key):
        summation = 0
        for char in key:
            summation += ord(char)
        return summation % self.MAX

    def collision_resolver(self, id, seed):
        return (id + seed) % self.MAX

    def __setitem__(self, key, value):
        id = self.hash_function(key)
        seed = 1
        while self.arr[id] is not None:
            id = self.collision_resolver(id, seed)
            seed += 1

        self.arr[id] = (key, value)

    def __getitem__(self, key):
        id = self.hash_function(key)
        seed = 1
        while self.arr[id] is not None and self.arr[id][0] != key:
            id = self.collision_resolver(id, seed)
            seed += 1

        return self.arr[id]

    def __delitem__(self, key):
        id = self.hash_function(key)
        seed = 1
        while self.arr[id] is not None and self.arr[id][0] != key:
            id = self.collision_resolver(id, seed)
            seed += 1

        if self.arr[id] is not None and self.arr[id][0] == key:
            self.arr[id] = None


hashTable = HashTable()
hashTable["March 6"] = 786
hashTable["March 17"] = 786
print("LINEAR PROBING")
print("March 6:", hashTable["March 6"])
print("March 17:", hashTable["March 17"])
print(hashTable.arr)
print("Deleting 'March 17'...")
del hashTable["March 17"]
print(hashTable.arr)

# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# QUADRATIC PROBING
class QuadraticProbingHashTable(HashTable):
    def __init__(self):
        super().__init__()
        self.c1 = 1
        self.c2 = 1

    def collision_resolver(self, id, seed):
        return (id + self.c1 * seed + self.c2 * seed * seed) % self.MAX


hashTable = QuadraticProbingHashTable()
hashTable["March 6"] = 786
hashTable["March 17"] = 786
print("QUADRATIC PROBING")
print("March 6:", hashTable["March 6"])
print("March 17:", hashTable["March 17"])
print(hashTable.arr)
print("Deleting 'March 17'...")
del hashTable["March 17"]
print(hashTable.arr)

# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# DOUBLE HASHING
class DoubleHashing(HashTable):
    def __init__(self):
        super().__init__()

    def hash_function_2(self, id):
        return 1 + (id % (self.MAX - 2))

    def collision_resolver(self, id, seed):
        return (id + seed * self.hash_function_2(id)) % self.MAX


hashTable = DoubleHashing()
hashTable["March 6"] = 786
hashTable["March 17"] = 786
print("DOUBLE HASHING")
print("March 6:", hashTable["March 6"])
print("March 17:", hashTable["March 17"])
print(hashTable.arr)
print("Deleting 'March 17'...")
del hashTable["March 17"]
print(hashTable.arr)
