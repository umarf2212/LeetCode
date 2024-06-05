class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        N = len(words)

        result = []
        for letter in set(words[0]):
            letterCount = min([word.count(letter) for word in words])
            result += letterCount * [letter]

        return result


        
            
