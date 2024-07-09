class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        
        # waitingTime = 0
        # [1,2] -> curTime = curTime + 2 = 1+2 = 3
        # [2,5]
        # [4,3]

        n = len(customers)
        
        curTime = customers[0][0]
        waitingTime = 0
        for arrival, finish in customers:
            # customers already waiting for their orders
            if curTime >= arrival:
                curTime += finish
                waitingTime += curTime - arrival

            # no customers, chef ready to start any time
            else:
                curTime = arrival + finish
                waitingTime += finish
        
        # print(waitingTime)
        return waitingTime/n

