class MyHashSet:

    def __init__(self):
        self.bucket = [None] * 100

    def add(self, key: int) -> None:
        index = self.indexHash(key)
        
        if not self.bucket[index]:
            self.bucket[index] = [key]
        
        elif key not in self.bucket[index]:
            self.bucket[index].append(key)

    def remove(self, key: int) -> None:
        index = self.indexHash(key)
        
        if self.bucket[index] and key in self.bucket[index]:
            self.bucket[index].remove(key)
            
    def contains(self, key: int) -> bool:
        index = self.indexHash(key)
        
        if self.bucket[index] and key in self.bucket[index]:
            return True
        return False
    
    def indexHash(self, key: int) -> int:
        return key % 100


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)