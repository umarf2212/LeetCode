class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        d1 = {}
        for i, letter in enumerate([i for i in pattern]):
            if letter in d1:
                d1[letter].append(i)
            else:
                d1[letter] = [i]
        
        d2 = {}
        for i, word in enumerate(s.split()):
            if word in d2:
                d2[word].append(i)
            else:
                d2[word] = [i]
              
        if len(d1.values()) != len(d2.values()): return False
        
        for i in range(len(d1.values())):
            if list(d1.values())[i] != list(d2.values())[i]:
                return False
            
        return True
