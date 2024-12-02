class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        
        n = len(searchWord)
        for ind, word in enumerate(sentence.split(' ')):
            if len(word) >= n:
                if word[:n] == searchWord:
                    return ind+1

        return -1
