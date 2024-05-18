class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        
        lastIndex = -1

        for i, num in enumerate(nums):
            if num == 1:
                if lastIndex == -1:
                    lastIndex = i
                
                elif i - lastIndex - 1 < k:
                    return False
                
                else:
                    lastIndex = i
        
        return True

'''
 1 0 0 1 0 1
 0 1 2 3 4 5




'''
