class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        S = set()

        for num in arr:
            if num/2 in S or num*2 in S:
                return True
            S.add(num)
        
        return False
