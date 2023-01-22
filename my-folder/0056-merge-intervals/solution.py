class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x:x[0])

        stack = [intervals[0]]
        for i in range(1, len(intervals)):
            #overlap
            if intervals[i][0] <= stack[-1][1]:
                new = [stack[-1][0], max(stack[-1][1], intervals[i][1])]
                stack.pop()
                stack.append(new)
            else:
                stack.append(intervals[i])

        return stack





