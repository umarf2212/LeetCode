class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        
        # P:
        # 1 2 3 4 5
        # 3 1 2 4 5
        # 1 3 2 4 5
        # 2 1 3 4 5
        # 1 2 3 4 5
        
        # 3 1 2 1
        # 
        
        dq = deque([i for i in range(1, m+1)])
        res = []
        
        for num in queries:
            for i in range(len(dq)):
                if dq[i] == num:
                    res.append(i)
                    del dq[i]
                    dq.appendleft(num)
        
        return res