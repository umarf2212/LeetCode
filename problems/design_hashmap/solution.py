class MyHashMap:
    
    BUCKET_SIZE = 100000

    def __init__(self):
        self.bucket = [None] * self.BUCKET_SIZE

    def put(self, key: int, value: int) -> None:
        index = self.indexHash(key)
        self.bucket[index] = value

    def get(self, key: int) -> int:
        index = self.indexHash(key)
        if self.bucket[index] is not None:
            return self.bucket[index]
        else:
            return -1

    def remove(self, key: int) -> None:
        index = self.indexHash(key)
        self.bucket[index] = None
        
    def indexHash(self, key: int) -> int:
        return key % self.BUCKET_SIZE
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)