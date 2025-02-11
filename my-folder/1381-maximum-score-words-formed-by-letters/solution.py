class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        alphaIndex = {alphabets[i]:i for i in range(26)}

        counts = {}
        for letter in letters:
            if letter not in counts:
                counts[letter] = 0
            counts[letter] += 1
        

        wordScores = {}
        for word in words:
            wordScore = 0
            for letter in word:
                wordScore += score[alphaIndex[letter]]
            
            wordScores[word] = wordScore
        
        
        # print(wordScores)

        def canForm(word, counts):
            wordCounts = {}
            for c in word:
                wordCounts[c] = wordCounts.get(c, 0) + 1

                if wordCounts[c] > counts.get(c, 0):
                    return False

            return True
        
        def updateCounts(word, counts, remove):
            for c in word:
                if remove:
                    counts[c] = counts.get(c, 0) - 1
                else:
                    counts[c] = counts.get(c, 0) + 1

        def backtrack(curWordInd, countDict):
            if curWordInd == len(words):
                return 0

            # skip current word
            skip = backtrack(curWordInd + 1, countDict)

            # try to take current word if possible
            take = 0
            word = words[curWordInd]
            if canForm(word, countDict):
                # remove letters used by this word
                updateCounts(word, countDict, True)

                curScore = wordScores[word]
                take = curScore + backtrack(curWordInd+1, countDict)

                # add the letters back
                updateCounts(word, countDict, False)

            return max(skip, take)
        
        return backtrack(0, counts)



