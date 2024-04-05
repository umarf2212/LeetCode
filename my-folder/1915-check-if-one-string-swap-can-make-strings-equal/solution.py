class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        
        # 1. Check if both strings are anagrams of each other.
        #    if no -> return false right away
        # TC: O(2n) -> O(n)
        # SC: O(2n) -> O(n)

        # 2. Check if exatcly two characters in 
        #    either of the strings are displaced
        # TC: O(n)

        n = len(s1)

        # Create character count for each string
        s1_count = {}
        s2_count = {}
        for i in range(n):
            if s1[i] not in s1_count:
                s1_count[s1[i]] = 0
            s1_count[s1[i]] += 1

            if s2[i] not in s2_count:
                s2_count[s2[i]] = 0
            s2_count[s2[i]] += 1
        
        # Compare same char counts in both strings
        for ch, count in s1_count.items():
            if ch not in s2_count:
                return False
            
            if s2_count[ch] != count:
                return False
        

        # bank
        # kanb
        displaced = 0
        for i in range(n):
            if s1[i] != s2[i]:
                displaced += 1
        
        return displaced <= 2



