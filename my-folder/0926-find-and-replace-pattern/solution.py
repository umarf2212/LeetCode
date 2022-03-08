class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        # abab
        # 1212
        
        def patternSequence(pattern):
            c = 1
            d = {}
            sequence = ''
            for i in pattern:
                if i not in d:
                    d[i] = c
                    sequence += str(c)
                    c += 1
                else:
                    sequence += str(d[i])
                    
                sequence += '-'
            
            return sequence
        
        res = []
        pattern_Sequence = patternSequence(pattern)
        for word in words:
            if patternSequence(word) == pattern_Sequence:
                res.append(word)
        
        return res
