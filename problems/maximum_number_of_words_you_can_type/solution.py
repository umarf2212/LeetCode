class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        
        s = set(brokenLetters)
        
        count = 0
        for word in text.split():
            cannot = False
            for letter in word:
                if letter in s:
                    cannot = True
            
            if not cannot:
                count+=1
        
        return count