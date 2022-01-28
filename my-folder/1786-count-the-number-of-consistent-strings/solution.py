class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        
        # allowed = set(allowed)
        
        count = 0
        for word in words:
            
            # word_set = list(set(word))
            for i in word:
                if i not in allowed:
                    break
            else:
                count+=1
        
        return count
