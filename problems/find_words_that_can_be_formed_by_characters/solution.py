class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        res = 0
        for word in words:
            
            c = Counter(chars)
            
            for i in word:
                if i not in c or c[i] == 0:
                    break
                else:
                    c[i] -= 1
            else:
                res += len(word)
                
        
        return res