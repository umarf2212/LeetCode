class Solution:
    def countValidWords(self, sentence: str) -> int:
        
        ar = sentence.split()
        
        count = 0
        for word in ar:
            
            if word[0] == '-' or word[-1] == '-' or word[-1].isdigit():
                continue
            
            isWord = True
            hyphen = 0
            for i in range(len(word)-2,-1,-1):
                
                if word[i] == '-':
                    if i>0 and not word[i-1].isalpha() or not word[i+1].isalpha():
                        isWord=False
                    else:
                        hyphen += 1
                    
                elif word[i].isdigit() or word[i] in '!.,':
                    isWord = False
                
            if not isWord or hyphen > 1:
                continue

            count += 1
        
        return count
