class Solution:
    
    def checkPal(self, word):
            for i in range(len(word)//1):
                if word[i] != word[len(word) -1 -i]:
                    return False
            return True
    
    def firstPalindrome(self, words: List[str]) -> str:
        
        for word in words:
            if self.checkPal(word):
                return word
        
        return ""
