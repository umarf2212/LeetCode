class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        
        w1 = Counter(word1)
        w2 = {}
        
        for ch in word2:
            if ch in w1:
                w1[ch] -= 1
            else:
                if ch in w2:
                    w2[ch] += 1
                else:
                    w2[ch] = 1
        
        for ch, count in w1.items():
            if count < -3 or count > 3:
                return False
        
        for ch, count in w2.items():
            if count > 3:
                return False
        
        return True