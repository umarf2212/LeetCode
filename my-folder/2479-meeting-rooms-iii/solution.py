class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        
        meetings.sort(key=lambda x:x[0])

        used_rooms = []
        unused_rooms = list(range(n))
        heapify(unused_rooms)
        meeting_count = [0] * n

        for start, end in meetings:

            # when no meeting is delayed
            while used_rooms and used_rooms[0][0] <= start:
                prevEnd, room = heappop(used_rooms)
                heappush(unused_rooms, room)

            if unused_rooms:
                room = heappop(unused_rooms)
                heappush(used_rooms, [end, room])
            else:
                available_at, room = heappop(used_rooms)
                heappush(
                    used_rooms, 
                    [available_at + end - start, room]
                )
            
            meeting_count[room] += 1


        maxRoomCount = 0
        maxRoom = 0
        for room in range(n):
            if meeting_count[room] > maxRoomCount:
                maxRoomCount = meeting_count[room]
                maxRoom = room
        
        return maxRoom
