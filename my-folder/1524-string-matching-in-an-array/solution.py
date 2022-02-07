class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        
        res = set([])
        for word in words:
            for substr in words:
                if len(substr) >= len(word):
                    continue
                else:
                    if substr in word:
                        res.add(substr)

        return res
