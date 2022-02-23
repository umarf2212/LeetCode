class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        c = Counter(magazine)
        
        for i in ransomNote:
            if i not in c:
                return False
            elif c[i] == 0:
                return False
            else:
                c[i] -= 1
        
        return True
