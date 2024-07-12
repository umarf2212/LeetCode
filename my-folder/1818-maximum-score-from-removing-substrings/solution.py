class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        
        # ab -> x
        # ba -> y

        def countSmaller(chars, first, second):
            # ['a,a,b,b]'
            res = 0
            stack = []
            for ch in chars:
                if ch == second:
                    stack.append(ch)
                elif stack:
                    res += 1
                    stack.pop()
            return res


        if x > y:
            first = 'a'
            second = 'b'
            larger = x
            smaller = y
        else:
            first = 'b'
            second = 'a'
            larger = y
            smaller = x
        
        stack = []
        res = 0
        for ch in s:
            # print(stack, ch)
            if not stack and ch in 'ab':
                stack.append(ch)
                continue

            elif ch not in 'ab':
                res += (countSmaller(stack, first, second) * smaller)
                stack = []
                continue

            elif ch == second and stack[-1] == first:
                stack.pop()
                res += larger
            else:
                stack.append(ch)

        res += (countSmaller(stack, first, second) * smaller)
        return res




