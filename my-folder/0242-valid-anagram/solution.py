class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        sCount = Counter(s)
        
        for i in t:
            if i not in sCount: return False
            else:
                sCount[i] -= 1
    
        return not any(sCount.values())
