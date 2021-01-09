class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # ord('a') == 97
        # ord('z') == 122
        
        # ord('A') == 65
        # ord('Z') == 90
        
        # 0, 1, len(word)
        
        capital = 0
        
        if ord(word[0]) in range(65,91):
            capital = 1
            
            # count capital letters
            for i in range(1, len(word)):
                if ord(word[i]) in range(65,91):
                    capital += 1
            
            if capital == 1 or capital == len(word):
                return True
            else:
                return False
        else:
            for i in range(1, len(word)):
                if ord(word[i]) in range(65,91):
                    return False
            return True
