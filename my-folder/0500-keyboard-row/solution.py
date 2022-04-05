class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        
        row1 = set(['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'Q','W','E','R','T','Y','U','I','O','P'])
        row2 = set(['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l','A','S','D','F','G','H','J','K','L'])
        row3 = set(['z', 'x', 'c', 'v', 'b', 'n', 'm','Z','X','C','V','B','N','M'])
        
        res = []
        for word in words:
            if word[0] in row1:
                row = row1
            elif word[0] in row2:
                row = row2
            else:
                row = row3
            
            for i in range(1, len(word)):
                if word[i] not in row:
                    break
            else:
                res.append(word)
        
        return res
