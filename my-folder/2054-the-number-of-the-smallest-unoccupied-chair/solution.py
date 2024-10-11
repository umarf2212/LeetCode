import heapq
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        curChair = 0
        pq = []
        availableChairs = []

        friendTimes = [[i, times[i]] for i in range(len(times))]
        friendTimes.sort(key=lambda x:x[1][0])

        for i in range(len(friendTimes)):
            friend, time = friendTimes[i]

            while pq and pq[0][0] <= time[0]:
                _, chair = heapq.heappop(pq)
                heapq.heappush(availableChairs, chair)

            if availableChairs:
                chair = heapq.heappop(availableChairs)
            else:
                chair = curChair
                curChair += 1
            
            if targetFriend == friend:
                return chair
            
            heapq.heappush(pq, [time[1], chair])



