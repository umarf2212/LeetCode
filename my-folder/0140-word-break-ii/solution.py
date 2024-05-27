class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        def backtrack(start, curSentence, allSentences):
            if start == len(s):
                allSentences.append(' '.join(curSentence))
                return

            # catsanddog

            for end in range(start, len(s)):
                word = s[start:end+1]
                if word in wordDict:
                    curSentence.append(word)
                    backtrack(end+1, curSentence, allSentences)
                    curSentence.pop()
        
        allSentences = []
        curSentence = []
        wordDict = set(wordDict)
        backtrack(0, curSentence, allSentences)

        return allSentences
                 

        '''
        From a starting index i, we have to check for every possible ending j
        whether [i:j] is a word or not. 
        1. If it is, then we add it to current sentence and move on with start=end+1
        2. But for any starting index, a word can be formed at multiple ending positions
           such as cat and cats, go or going, so we need to check for every ending.
           Which simply means from start, we run a for loop.
        3. For a given start, there has to be an ending, if there's not, 
           then the start is not a good point to form sentences.
        4. The starting index 0 has to have ending which leads to the end of the string.

        catsanddog

        aabcde

        a, ab, abc, bc, bcd, bcde, cde

        '''

