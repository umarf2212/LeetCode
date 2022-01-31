class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        
        c = 0
        
        d1 = Counter(words1)
        d2 = Counter(words2)
        
        for word, count in d2.items():
            if word in d1 and d1[word] == 1 and count == 1:
                c+=1
        
        return c
