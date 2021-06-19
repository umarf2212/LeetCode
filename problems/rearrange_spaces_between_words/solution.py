class Solution:
    def reorderSpaces(self, text: str) -> str:
        
        word = ''
        words = []
        spaces = 0
        for i in range(len(text)):
            if text[i] == ' ':
                spaces += 1
                
                if word:
                    words.append(word)
                    word = ''
                
            else:
                word += text[i]
        
        if word: words.append(word)
        
        if len(words) == 1:
            return words[0] + ' ' * spaces
        
        sep = spaces//(len(words)-1)
        
        res = ''
        for i in range(len(words)-1):
            res += words[i] + ' ' * sep
        
        res += words[-1]
        
        left = spaces%(len(words)-1)
        if left > 0:
            res += ' '*left
        
        return res
        