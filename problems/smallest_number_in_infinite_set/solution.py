import heapq
class SmallestInfiniteSet:

    def __init__(self):
        self.set = set([i for i in range(1, 1001)])
        self.min = list(self.set)

    def popSmallest(self) -> int:
        if self.min:
            cur = heapq.heappop(self.min)
            self.set.remove(cur)
            return cur

    def addBack(self, num: int) -> None:
        if num not in self.set:
            self.set.add(num)
            heapq.heappush(self.min, num)



# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)