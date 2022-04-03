class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        # ["abc", "def", "ghj", "a"]
        
        res=0
        for j in range(len(strs[0])):
            for i in range(1, len(strs)):
                if strs[i-1][j] > strs[i][j]:
                    res+=1
                    break
        
        return res