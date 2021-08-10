class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A','E','I','O','U'])
        res = []
        words = sentence.split()
        for i in range(len(words)):
            
            word = words[i]
            newWord = ''
            
            if word[0] in vowels:
                newWord += word
            else:
                newWord += word[1:] + word[0]
            
            newWord += 'ma'
            newWord += 'a' * (i+1)
        
            res.append(newWord)
        
        return ' '.join(res)