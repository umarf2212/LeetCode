class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:

        # abcd
        # 0 : a -> eee
        # 2 : cd -> ffff
        
        # TC: O(n), SC: O(n)
        # ops = [[indices[i], sources[i], targets[i]] for i in range(len(indices))]
        # ops.sort(key=lambda x:x[0], reverse=True)
        ops = sorted(zip(indices, sources, targets), reverse=True)

        def sourceMatchesSubstr(s, ind, source):
            sourceLen = len(source)
            if len(s)-ind < sourceLen:
                return False
                
            for i in range(ind, ind+len(source)):
                if s[i] != source[i-ind]:
                    return False
            return True


        for ind, source, target in ops:
            
            if sourceMatchesSubstr(s, ind, source):
                sourceLen = len(source)
                s = s[:ind] + target + s[ind+sourceLen:]
            
            print(s)
        
        return s

