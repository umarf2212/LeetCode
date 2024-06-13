class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        # 1. Calculate the hash sum of all the words
        # 2. Also calculate the length of each word: wordLen
        # 3. Now start with the window size equal to the size of words
        # 4. Calculate hash sums and check if the hash sums match 
        # 5. Move the window by wordLen distance at a time

        hashSum = 0
        for word in words:
            hashSum += hash(word)
        
        wordLen = len(words[0])
        windowSize = len(words) * wordLen

        if len(s) < windowSize:
            return []
        
        res = []
        for i in range(0, len(s) - windowSize+1):
            j = i + windowSize

            curHashSum = 0
            for x in range(i, j, wordLen):
                curHashSum += hash(s[x:x+wordLen])

            if curHashSum == hashSum:
                res.append(i)
        
        return res


