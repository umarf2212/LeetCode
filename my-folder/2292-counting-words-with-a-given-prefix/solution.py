class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        
        def matchPref(word):
            i = 0
            while i < len(pref):
                if word[i] != pref[i]:
                    return False
                i+=1
            return True
    
        
        count = 0
        for word in words:
            if len(word) >= len(pref) and matchPref(word):
                count+=1
        
        return count
