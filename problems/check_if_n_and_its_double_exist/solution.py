class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        d = set()
        
        for num in arr:
            if num/2 in d or num*2 in d:
                return True
            else:
                d.add(num)
        
        return False