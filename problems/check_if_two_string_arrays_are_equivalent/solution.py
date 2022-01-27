class Solution:
    def concatenate(self, arr):
        s = ''
        for word in arr: 
            s += word
        return s
    
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return self.concatenate(word1) == self.concatenate(word2)