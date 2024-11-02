class Solution:
    def isCircularSentence(self, sentence: str) -> bool:

        words = sentence.split(' ')
        
        if words[0][0] != words[-1][-1]:
            return False
        
        for i in range(1, len(words)):
            prev = words[i-1]
            cur = words[i]

            if prev[-1] != cur[0]:
                return False
        
        return True
