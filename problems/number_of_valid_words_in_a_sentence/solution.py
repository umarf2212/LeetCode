class Solution:
    def countValidWords(self, sentence: str) -> int:
        
        count = 0
        punc = '.,!'
        digits = set(['0','1','2','3','4','5','6','7','8','9'])
        
        if len(sentence) == 1 and sentence[0] in punc:
            return 1
        
        for word in sentence.split(' '):
            if len(word) == 0: continue
                
            hyphen = 0
            if word[0] == '-' or word[-1] == '-':
                continue
            
            n = len(word)
            noword = False
            for i in range(n):
                
                #if any digits found, leave
                if word[i] in digits:
                    noword = True
                
                #check for hyphens, also if more than one
                if word[i] == '-':
                    hyphen += 1
                    if hyphen > 1 or word[i-1] in punc or word[i+1] in punc: 
                        noword = True
                        
                #check for punctuation in the middle
                if i < n-1 and word[i] in punc:
                    noword = True
                    
            if not noword: count += 1
            
        return count