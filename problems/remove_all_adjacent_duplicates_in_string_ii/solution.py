class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        # [char, count]
        
        stack = []
        for char in s:
            if stack and stack[-1][0] == char:
                pair = stack.pop()
                pair = [pair[0], pair[1]+1]
                if pair[1] < k:
                    stack.append(pair)
            else:
                stack.append([char, 1])
        
        res = ''
        for pair in stack:
            res += pair[0] * pair[1]
        
        return res