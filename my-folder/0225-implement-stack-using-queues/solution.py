from collections import deque
class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        self.queues = [self.q1, self.q2]
        

    def push(self, x: int) -> None:
        self.queues[0].append(x)

    def pop(self) -> int:
        active, inactive = self.queues

        while len(active) > 1:
            inactive.append(active.popleft())
        
        self.queues = [inactive, active]
        
        return active.pop()

    def top(self) -> int:
        active, inactive = self.queues

        while len(active) > 1:
            inactive.append(active.popleft())
        
        
        num = active.pop()
        inactive.append(num)
        self.queues = [inactive, active]
        
        return num

    def empty(self) -> bool:
        return len(self.queues[0]) == 0


# s = [1,2,3,4]

# q1 = []
# q2 = [1,2,3,4]


# 4


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
