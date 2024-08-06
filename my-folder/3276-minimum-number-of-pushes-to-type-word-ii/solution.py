class Solution:
    def minimumPushes(self, word: str) -> int:
        
        # 1. Create a frequency map of each letter.
        # 2. Most frequent letters should be mapped to different keys individually
        # 3. 7 and 9 should have least priority as they have 4 letters

        letterCount = {}
        for letter in word:
            if letter not in letterCount:
                letterCount[letter] = 0
            letterCount[letter] += 1
    
        freq = [[letter, count] for letter, count in letterCount.items()]
        freq.sort(key=lambda x:x[1], reverse=True)

        # s = 'mississipi'
        # ['s':4, 'i':4, 'p':1, 'm':1]
        
        index = [2, 3, 4, 5, 6, 8, 7, 9]
        mappings = [[],[],[],[],[],[],[],[],[],[]]
        i = 0

        for letter, count in freq:
            ind = index[i%8]
            i += 1
            mappings[ind].append(count)
        
        # print(mappings)

        result = 0
        for numpad in mappings[2:]:
            for i in range(len(numpad)):
                count = i+1
                result += numpad[i] * count

        return result








