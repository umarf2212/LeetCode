class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        # ord(char) - 97
        trans = set()
        
        for word in words:
            
            code = ''
            for c in word:
                code += morse[ord(c) - 97]
            trans.add(code)
        
        return len(trans)