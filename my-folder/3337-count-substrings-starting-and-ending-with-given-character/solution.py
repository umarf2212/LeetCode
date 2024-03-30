class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        
        count = 0
        for i in s:
            if i == c: count += 1
        
        return count*(count+1)//2
