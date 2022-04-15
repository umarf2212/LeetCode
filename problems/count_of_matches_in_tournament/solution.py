class Solution:
    def numberOfMatches(self, n: int) -> int:
        
        matches = 0
        
        while n > 1:
            versus = divmod(n, 2)
            n = versus[0] + versus[1]
            matches += versus[0]
                
        return matches