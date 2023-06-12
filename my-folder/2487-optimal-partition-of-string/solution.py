class Solution:
    def partitionString(self, s: str) -> int:

        S = set()
        j = 0
        count = 1
        for j in range(len(s)):

            if s[j] not in S:
                S.add(s[j])
            else:
                count += 1
                S = set([s[j]])
        
        return count


