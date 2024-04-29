import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x:x[0])
        
        pq = [intervals[0][::-1]]
        roomCount = 1

        for i in range(1, len(intervals)):
            curInterval = intervals[i]
        
            if len(pq) > 0 and pq[0][0] <= curInterval[0]:
                heapq.heappop(pq)
                heapq.heappush(pq, curInterval[::-1])
            else:
                heapq.heappush(pq, curInterval[::-1])
                roomCount = max(roomCount, len(pq))
        
        return roomCount


