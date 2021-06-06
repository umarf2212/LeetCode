class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        
        total = numBottles

        while numBottles >= numExchange:
            remaining = numBottles % numExchange
            numBottles = numBottles // numExchange
            total += numBottles
            numBottles += remaining

        return total