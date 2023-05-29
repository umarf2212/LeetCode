class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        d = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def gen(digits, i, ar, ans):

            if i == len(digits):
                ans.append(''.join(ar))
                return

            for c in d[digits[i]]:
                ar.append(c)
                gen(digits, i+1, ar, ans)
                ar.pop()
        
        ar = []
        ans = []
        gen(digits, 0, ar, ans)
        return ans