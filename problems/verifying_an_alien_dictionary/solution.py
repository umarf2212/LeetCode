class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        d={}
        for i in range(len(order)):
            d[order[i]] = i
        
        for i in range(1, len(words)):
            # word1 = words[i-1]
            # word2 = words[i]
            smaller = len(words[i-1]) if len(words[i-1]) < len(words[i]) else len(words[i])
            areSame = True
            for j in range(smaller):
                diff = d[words[i][j]] - d[words[i-1][j]]
                if diff < 0: 
                    return False
                if diff > 0: 
                    areSame = False
                    break
            
            if areSame and len(words[i]) < len(words[i-1]):
                return False
            
        return True
            
            
            
            
            
            

# areSame = True
# for item in letters:
#     diff = d[item[0]] - d[item[1]]
#     if diff < 0:
#         return False
#     if diff > 0:
#         areSame = False