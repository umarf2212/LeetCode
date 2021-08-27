class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        # 1 2 3
        # 1 1
        
        # 2 2 3 4 5
        # 1 5 6 6
        
        g.sort()
        s.sort()
        
        cookie = 0
        child = 0
        totalChildren = 0
        while cookie < len(s) and child < len(g):
            
            if s[cookie] >= g[child]:
                totalChildren += 1
                child += 1
                
            cookie += 1
        
        return totalChildren
