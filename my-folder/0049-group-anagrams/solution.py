from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        d = {}
        for i in range(len(strs)):
            key = ''.join(sorted(strs[i]))

            if key not in d:
                d[key] = []
            d[key].append(strs[i])
        
        return d.values()



