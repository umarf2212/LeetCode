from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.d = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1

        temp = self.d[key]
        del self.d[key]
        self.d[key] = temp
        # print('GET ->', self.d)
        return temp
        
    def put(self, key: int, value: int) -> None:
        
        if key in self.d:
            del self.d[key]
            self.size -= 1

        if self.size == self.capacity:
            del self.d[next(iter(self.d))]
            self.size -= 1

        
        self.d[key] = value
        self.size += 1

        # print('PUT ->', self.d)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)