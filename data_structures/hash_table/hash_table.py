class HashTable:
    def __init__(self) -> None:
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    def hash_function(self, key):
        summation = 0
        for char in key:
            summation += ord(char)
        return summation % self.MAX

    # Method Overriding
    def __setitem__(self, key, value):
        self.arr.insert(self.hash_function(key), value)

    def __getitem__(self, key):
        return self.arr[self.hash_function(key)]


hashTable = HashTable()
hashTable["March_2021"] = 789
hashTable["March_2022"] = 786
print("March_2021:", hashTable["March_2021"])
print("March_2022:", hashTable["March_2022"])
print(hashTable.arr)
