class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        less = []
        more = []
        equal = 0
        
        for num in nums:
            
            if num < pivot:
                less.append(num)
            
            elif num > pivot:
                more.append(num)
            
            else:
                equal += 1
        
        return less + [pivot for _ in range(equal)] + more
