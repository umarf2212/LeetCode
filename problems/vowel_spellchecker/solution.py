class Solution:
    
    def serializeVowel(self, word):
        s = ''
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        for i in word:
            if i in vowels:
                s += '-'
            else:
                s += i
        
        return s
    
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        
        wordset = set(wordlist)
        
        lowerset = {}
        serialized = {}
        
        for word in wordlist:
            low = word.lower()
            if low not in lowerset:
                lowerset[low] = word
            
            ser = self.serializeVowel(low)
            if ser not in serialized:
                serialized[ser] = word
        
        
        res = []
        
        # print(wordset, lowerset, serialized)
        
        for word in queries:
            low = word.lower()
            ser = self.serializeVowel(low)

            if word in wordset:
                res.append(word)
            elif low in lowerset:
                res.append(lowerset[low])
            elif ser in serialized:
                res.append(serialized[ser])
            else:
                res.append("")
        
        return res