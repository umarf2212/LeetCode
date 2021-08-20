class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        d = Counter(words)
        
        wordCount = [(count, word) for word, count in d.items()]
        wordCount.sort(key=lambda x: x[0])
        
        # [[i, 2], [love, 2], [leetcode, 1], [coding, 1]]
        
        countWord = {}
        
        for word, count in d.items():
            if count in countWord:
                countWord[count].append(word)
            else:
                countWord[count] = [word]
        
        res = []
        for i in sorted(countWord.keys(), reverse=True):
            if k==0: break
                
            if len(countWord[i]) > k:
                res += sorted(countWord[i])[:k]
                break
            else:
                res += sorted(countWord[i])
                k -= len(countWord[i])
            
                
        return res
