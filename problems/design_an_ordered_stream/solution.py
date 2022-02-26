class OrderedStream:

    def __init__(self, n: int):
        self.d = {}
        self.next = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.d[idKey] = value
        
        res = []
        while self.next in self.d:
            res.append(self.d[self.next])
            self.next += 1
        
        return res


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)