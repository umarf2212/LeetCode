class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        
        alpha = {'a': '0', 'b': '1', 'c': '2', 'd': '3', 'e': '4', 'f': '5', 'g': '6', 'h': '7', 'i': '8', 'j': '9'}
        
        f = ''
        for letter in firstWord:
            f += alpha[letter]
        
        s = ''
        for letter in secondWord:
            s += alpha[letter]
        
        t = ''
        for letter in targetWord:
            t += alpha[letter]
    
    
        return int(f)+int(s) == int(t)