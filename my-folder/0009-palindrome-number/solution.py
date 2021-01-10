class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0: return False
        
        stack = []
        X = str(x)
        i = 0
        j = len(X)-1
        
        while j > i and i != j:
            if X[i] != X[j]:
                return False
            
            i+=1
            j-=1
        
        return True
