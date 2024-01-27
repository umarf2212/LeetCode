class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x:x[0])
        
        stack = [intervals[0]]
        for i in range(1, len(intervals)):
            curStart, curEnd = intervals[i]

            # overlap
            if stack[-1][1] >= curStart:
                prevStart, prevEnd = stack.pop()

                newStart = min(prevStart, curStart)
                newEnd = max(prevEnd, curEnd)

                stack.append( [newStart, newEnd] )
            
            else:
                stack.append(intervals[i])
        
        return stack

                

