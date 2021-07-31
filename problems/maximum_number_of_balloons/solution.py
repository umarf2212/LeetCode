class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        d = {}
        letters = set({'b', 'a', 'l', 'o', 'n'})
        for i in range(len(text)):
            
            if text[i] in letters and text[i] not in d:
                d[text[i]] = 1
            if text[i] in letters and text[i] in d:
                d[text[i]] += 1
            
        
        if 'b' not in d or 'a' not in d or 'l' not in d or 'o' not in d or 'n' not in d:
            return 0
        
        count = 0
        while True:
            
            d['b'] -= 1
            d['a'] -= 1
            d['l'] -= 2
            d['o'] -= 2
            d['n'] -= 1
            
            if d['b'] <= 0 or d['a'] <= 0 or d['l'] <= 0 or d['o'] <= 0 or d['n'] <= 0:
                return count
            
        
            count += 1