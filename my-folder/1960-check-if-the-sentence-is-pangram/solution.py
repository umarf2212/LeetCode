class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        a = {i:0 for i in 'abcdefghijklmnopqrstuvwxyz'}
        
        for c in sentence:
            a[c] = 1
        
        return all(a.values())
