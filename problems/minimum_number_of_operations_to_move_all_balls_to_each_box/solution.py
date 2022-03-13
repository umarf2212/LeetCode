class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        # 001011
        # 012345
        
        # 2+4+5 = 11
        # 1+3+4 = 8
        # 2+3   = 5
        # 1+1+2 = 4
        
        ar = [0,0]
        left = [0 for _ in range(len(boxes))]
        for i in range(len(boxes)):
            left[i] = [ar[0], ar[1]]  #[runningSum, count]
            
            if boxes[i] == '1':
                ar = [ar[0] + i, ar[1]+1]
        
        
        ar = [0,0]
        right = [0 for _ in range(len(boxes))]
        for i in range(len(boxes)-1,-1,-1):
            right[i] = [ar[0], ar[1]]
            
            if boxes[i] == '1':
                ar.append(i)
                ar = [ar[0]+i, ar[1]+1]
        
        res = []
        for i in range(len(boxes)):
            ar = left[i] # => [totalSum, count]
            left_moves = abs(ar[0] - (ar[1] * i))
            
            ar = right[i]
            right_moves = abs(ar[0] - (ar[1] * i))
            
            res.append(left_moves + right_moves)
        
        return res