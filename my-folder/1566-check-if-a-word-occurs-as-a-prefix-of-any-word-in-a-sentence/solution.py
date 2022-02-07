class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        
        res = -1
        ind = 1
        for word in sentence.split(' '):
            
            f = word.find(searchWord)
            if f == 0 and res == -1:
                res = ind
            
            ind += 1
        
        return res
